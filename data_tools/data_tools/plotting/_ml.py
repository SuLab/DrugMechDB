import numpy as np
from scipy import interp
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, roc_curve, auc


__all__ = ['graph_single_roc', 'graph_single_prc', 'graph_mean_roc', 'graph_mean_prc',
            'graph_roc_boilerplate', 'graph_prc_boilerplate']


def graph_single_roc(y, y_pred, label="", lw=4, alpha=1):
    fpr, tpr, thresh = roc_curve(y, y_pred, drop_intermediate=False)
    if label:
        plt.plot(fpr, tpr, lw=lw, alpha=alpha, label=label+" (AUC = {:0.2f})".format(auc(fpr, tpr)))
    else:
        plt.plot(fpr, tpr, lw=lw, alpha=alpha)


def calc_mean_roc_auc(ys, y_preds):
    tprs = []
    aucs = []

    mean_fpr = np.linspace(0, 1, 100)

    for y, y_pred in zip(ys, y_preds):
        # Compute ROC curve and area the curve
        fpr, tpr, thresholds = roc_curve(y, y_pred, drop_intermediate=False)

        tprs.append(interp(mean_fpr, fpr, tpr))
        tprs[-1][0] = 0.0
        roc_auc = auc(fpr, tpr)
        aucs.append(roc_auc)

    # Get mean and std_dev for metrics
    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    std_auc = np.std(aucs)
    std_tpr = np.std(tprs, axis=0)

    return mean_tpr, mean_fpr, mean_auc, std_auc, std_tpr


def graph_mean_roc(ys, y_preds, label="", lw=6, alpha=.8, fill_between=True, fill_alpha=.4):

    result = calc_mean_roc_auc(ys, y_preds)
    graph_mean_roc_from_metrics(*result, label, lw, alpha, fill_between, fill_alpha)


def graph_mean_roc_from_metrics(mean_tpr, mean_fpr, mean_auc, std_auc, std_tpr, label="", lw=6, alpha=.8,
                                fill_between=True, fill_alpha=.4):
    if label:
        fig = plt.plot(mean_fpr, mean_tpr,
                       label=label + ' (AUC = %0.2f)' % mean_auc,
                       lw=lw, alpha=alpha)
    else:
        fig = plt.plot(mean_fpr, mean_tpr, color='b',
                           label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
                           lw=lw, alpha=alpha)

    if fill_between:
        tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
        tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
        plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=fill_alpha,
                         label=r'$\pm$ 1 std. dev.')
    return fig


def graph_roc_boilerplate(title, size=24, w=8, h=7, loc='best'):
    """Run this after each single ROC curve plot"""
    x = [i for i in np.arange(0.0, 1.01, .01)]

    plt.plot(x, x, 'r--', lw=1, label='Luck')

    fig = plt.gcf()
    fig.set_size_inches(w, h)
    fig.set_tight_layout(False)
    plt.xlim([-0.01, 1.01])
    plt.ylim([-0.01, 1.01])
    plt.xticks(size=size * .666667)
    plt.yticks(size=size * .666667)
    plt.xlabel('False Positive Rate', size=size * .8333)
    plt.ylabel('True Positive Rate', size=size * .8333)
    plt.title(title, size=size)
    plt.legend(loc=loc, frameon=True, shadow=True, prop={'size': size * .666667})
    return fig


def graph_single_prc(y, y_pred, label="", lw=4, alpha=1):
    pre, rec, thresh = precision_recall_curve(y, y_pred)
    if label:
        plt.plot(rec, pre, lw=lw, alpha=alpha, label=label+" (AUC = {:0.2f})".format(auc(rec, pre)))
    else:
        plt.plot(rec, pre, lw=lw, alpha=alpha)


def calc_mean_prc_auc(ys, y_preds):
    pres = []
    aucs = []

    mean_rec = np.linspace(0, 1, 100)

    for y, y_pred in zip(ys, y_preds):

        # Compute PR curve and area the curve
        pre, rec, thresholds = precision_recall_curve(y, y_pred)
        prc_auc = auc(rec, pre)
        aucs.append(prc_auc)

        pre = pre[::-1]
        rec = rec[::-1]

        pres.append(interp(mean_rec, rec, pre))

    mean_pre = np.mean(pres, axis=0)
    mean_pre[-1] = 0
    mean_auc = auc(mean_rec, mean_pre)
    std_auc = np.std(aucs)
    std_pre = np.std(pres, axis=0)

    return mean_pre, mean_rec, mean_auc, std_auc, std_pre


def graph_mean_prc(ys, y_preds, label="", lw=6, alpha=.8, fill_between=True, fill_alpha=.4):

    results = calc_mean_prc_auc(ys, y_preds)
    graph_mean_prc_from_metrics(*results, label, lw, alpha, fill_between, fill_alpha)


def graph_mean_prc_from_metrics(mean_pre, mean_rec, mean_auc, std_auc, std_pre,
                                label="", lw=6, alpha=.8, fill_between=True, fill_alpha=.4):
    if label:
        fig = plt.plot(mean_rec, mean_pre,
                       label=label+r' (AUC = %0.2f)' % mean_auc,
                       lw=lw, alpha=alpha)
    else:
        fig = plt.plot(mean_rec, mean_pre, color='b',
                       label=r'Mean PRC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
                       lw=lw, alpha=alpha)

    if fill_between:
        pres_upper = np.minimum(mean_pre + std_pre, 1)
        pres_lower = np.maximum(mean_pre - std_pre, 0)
        plt.fill_between(mean_rec, pres_upper, pres_lower, color='grey', alpha=fill_alpha,
                         label=r'$\pm$ 1 std. dev.')
    return fig


def graph_prc_boilerplate(title, size=24, w=8, h=7, loc='best'):
    """Run this after each single PRC plot"""

    fig = plt.gcf()
    fig.set_size_inches(w, h)
    fig.set_tight_layout(False)
    plt.xlim([-0.01, 1.01])
    plt.ylim([-0.01, 1.01])
    plt.xticks(size=size*.666667)
    plt.yticks(size=size*.666667)
    plt.xlabel('Recall', size=size*.8333)
    plt.ylabel('Precision', size=size*.8333)
    plt.title(title, size=size)
    plt.legend(loc=loc, frameon=True, shadow=True, prop={'size':size*.666667})
    return fig

