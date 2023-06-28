import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles


__all__ = ['venn2_pretty', 'venn3_pretty']
PREF_COLORS = ["#38b5fc", "#fa8f52", "#917ad8", "#3ff44c", "#00904f", "#faff49", "#d4e7db"]


def _venn_pretty(subsets, num_circles, set_labels=('A', 'B'),  title='',
                 alpha=0.9, norm=10, lw=1.5, num_size=12, lbl_size=14, t_size=16,
                 colors=None, ax=None, border=True):
    # Ensure either a 2 or 3 circle diagram
    assert num_circles in [2, 3]

    # Get the right venn diagarm functions...
    if num_circles == 2:
        venn = venn2
        venn_circles = venn2_circles
    else:
        venn = venn3
        venn_circles = venn3_circles
    # Use preferred colors if none passed.
    if colors is None:
        colors = PREF_COLORS

    # Draw the venn diagrams
    v = venn(subsets, set_labels=set_labels, alpha=alpha, normalize_to=norm,
                ax=ax, subset_label_formatter=lambda s: '{:,}'.format(s))
    #c = venn_circles(subsets, linewidth=lw, normalize_to=norm, ax=ax)

    # Set the label sizes
    for text in v.set_labels:
        text.set_fontsize(lbl_size)
    for i, text in enumerate(v.subset_labels):
        if text is None:
            continue
        text.set_fontsize(num_size)
        if border:
            text.set_path_effects([pe.withStroke(linewidth=3, foreground='w')])

        # 2 of the default colors are darker, and require white text
        if not border and i in [2, 4]:
            text.set_color('w')
            # White looks narrower, so bold, and shift slightly
            text.set_fontweight('bold')
            text.set_position(text.get_position() + np.array([0.01, 0]))

    # change the colors of the venn diagram regions
    for i, p in enumerate(v.patches):
        if p is None:
            continue
        p.set_facecolor(colors[i])
        p.set_edgecolor(p.get_facecolor() * np.array([0.5]))
        p.set_linewidth(2)
    # Give the plot a title
    plt.title(title, size=t_size);
    return v


def venn2_pretty(subsets, set_labels=('A', 'B'),  title='',
                 alpha=0.9, norm=10, lw=1.5, num_size=12, lbl_size=12, t_size=14,
                 colors=None, ax=None, border=True):
    """
    Wrapper function for matplotlib_venn.venn2 that uses more aesthetically pleasing
    colors, text style, and line style.
    """
    return _venn_pretty(subsets, 2, set_labels, title, alpha, norm, lw, num_size, lbl_size, t_size, colors, ax, border)


def venn3_pretty(subsets, set_labels=('A', 'B', 'C'),  title='',
                 alpha=0.9, norm=1, lw=1.5, num_size=12, lbl_size=12, t_size=14,
                 colors=None, ax=None, border=True):
    """
    Wrapper function for matplotlib_venn.venn3 that uses more aesthetically pleasing
    colors, text style, and line style.
    """
    return _venn_pretty(subsets, 3, set_labels, title, alpha, norm, lw, num_size, lbl_size, t_size, colors, ax, border)

