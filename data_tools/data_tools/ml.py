import numpy as np
import pandas as pd
from copy import deepcopy
from tqdm.auto import tqdm
from sklearn.base import TransformerMixin
from scipy.sparse import csc_matrix, csr_matrix, issparse

def add_percentile_for_grp(in_df, group_col, new_col, sort_col='prediction'):

    grpd = in_df.groupby(group_col)
    out_dfs = []

    for grp, df1 in grpd:
        df = df1.copy()

        total = df.shape[0]

        df.sort_values(sort_col, inplace=True)
        order = df.reset_index(drop=True).index.values

        percentile = (order+1) / total
        df[new_col] = percentile

        out_dfs.append(df)

    return pd.concat(out_dfs, sort=False, ignore_index=True)


def get_model_coefs(model, X, f_names):
    """Helper Function to quickly return the model coefs and correspoding fetaure names"""

    # Ensure we have a numpy array for the features
    if type(X) == pd.DataFrame:
        X = X.values

    # Grab the coeffiencts
    coef = model.coef_
    # Some models return a double dimension array, others only a single
    if len(coef) != len(f_names):
        coef = coef[0]

    # insert the intercept
    coef = np.insert(coef, 0, model.intercept_)
    names = np.insert(f_names, 0, 'intercept')

    # Calculate z-score scaled coefficients based on the features
    if issparse(X):
        if type(X) != csc_matrix:
            X = X.tocoo().tocsc()
        z_intercept = coef[0] + sum(coef[1:] * X.mean(axis=0).A[0])
        z_coef = coef[1:] * sparse_std(X, axis=1)
        z_coef = np.insert(z_coef, 0, z_intercept)
    else:
        z_intercept = coef[0] + sum(coef[1:] * X.mean(axis=0))
        z_coef = coef[1:] * X.std(axis=0)
        z_coef = np.insert(z_coef, 0, z_intercept)

    # Return
    return pd.DataFrame([names, coef, z_coef]).T.rename(columns={0:'feature', 1:'coef', 2:'zcoef'})


def sparse_std(data, axis=1):
    """Take the standard deviation of a sparse matrix. axis=0 is Rows, axis=1 is columns."""

    def get_vec_std(vec):
        return vec.A.std(ddof=1)

    stds = []

    # ensure the correct matrix type for easy row or column subsetting
    if axis==1 and type(data) != csc_matrix:
        data = data.tocoo().tocsc()
    if axis==0 and type(data) != csr_matrix:
        data = data.tocoo().tocsr()

    # Get the std for each vector along the given axis individually
    for i in range(data.shape[axis]):
        if axis==1:
            stds.append(get_vec_std(data.getcol(i)))
        elif axis==0:
            stds.append(get_vec_std(data.getrow(i)))

    return np.array(stds)


class MeanScaledArcsinhTransformer(TransformerMixin):

    def fit(self, X, y=None):
        if issparse(X):
            self.initial_mean_ = X.tocoo().tocsc().mean(axis=0).A[0]
        else:
            self.initial_mean_ = X.mean(axis=0)

        # If input was DataFrame, Converts resultant series to ndarray
        try:
            self.initial_mean_ = self.initial_mean_.values
        except:
            pass

        # If inital mean == 0, likely all values were zero
        # this prevents issues later.
        self.initial_mean_[np.where(self.initial_mean_ == 0.0)] = 1

        return self

    def transform(self, X, y=None):
        if issparse(X):
            return np.arcsinh(X.tocoo().tocsc().multiply(self.initial_mean_**-1)).tocsc()
        return np.arcsinh(X / self.initial_mean_)


