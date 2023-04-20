import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


__all__ = ['count_plot_h']

def count_plot_h(data, annotate=True, order=None, annot_params=None, **params):
    
    
    
    """
    Wrapper for seaborn's Barpolot with horizontal result. Functions like sns.countplot(), but also allows for
    the result of Series.value_counts() to be passed as an argument.

    :param data: Pandas Series, either the data to be counted, or the result of value_counts() output
        (Or value counts with further data manipulation, (i.e. convert to percentages))
    :param annotate: Boolean, dict, or Series. If `True` will plot the counts at the end of the bars. If `False`,
        no annotations will be plotted. If a Series or dict, annotations other than the values can be passed
        and plotted at the end of the bars.  (e.g. plot percentages, but annotate with counts).
    :param order: list, override the most-to-least (top to bottom) order with a user supplied order.
    :**params: Other arguments to be passed to Seaborn's Barplot function.
    """
    # TODO: Better checks (does't work if obj type and/or nan values)
    # Do the value counts if not already done....
    if data.dtype not in [int, float]:
        data = data.value_counts()

    # Ensure the data is properly sorted
    data = data.sort_values(ascending=False)

    # Allow for numeric indices (sometimes we want counts of counts)
    if data.index.dtype in [int, float]:
        data.index = data.index.astype(str)
        y = pd.Categorical(data.index)
    else:
        y = data.index

    # Allow for a user supplied order
    if order is None:
        order = y

    # Plot the data orderred from most to least frequent

    splot = sns.barplot(x=data,
                        y=y,
                        order=order,
                        **params, 
                       palette = "Set3")




    # Allow a series to be passed, to annotate with different values
    if type(annotate) == pd.Series:
        # Ensure numeric keys are converted to strings
        if annotate.index.dtype in [int, float]:
            annotate.index = annotate.index.astype(str)
        annotate = annotate.to_dict()

    # Optionally Print the counts at the end of the data
    if annotate:
        if annot_params is None or type(annot_params) != dict:
            annot_params = dict()

        # Allow for user-passed annotation map, or simply annotate the values
        if type(annotate) == bool:
            annotate = data.to_dict()

        # Esnure proper formmating for printing integers...
        if pd.Series(annotate).dtype == int:
            f = lambda v: int(v)
            fs = '{:,}'
        elif pd.Series(annotate).dtype == float:
            f = lambda v: v
            fs = '{:,.2}'
        else:
            f = lambda v: v
            fs = '{}'

        for (p, n) in zip(splot.patches, splot.get_yticklabels()):
            annotation = annotate[n.get_text()]
            splot.annotate(fs.format(f(annotation)), 
                           (p.get_width(), p.get_y() + p.get_height()),
                           ha = 'left', 
                           va = 'center_baseline', 
                           xytext = (0, 10), 
                           textcoords = 'offset points',
                           **annot_params)
    return splot

