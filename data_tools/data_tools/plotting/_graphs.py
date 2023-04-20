import numpy as np
import pandas as pd
import seaborn as sns
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from collections import defaultdict
from scipy.spatial import distance


__all__ = ['shift_centers_to_min_distance', 'darken_hex_color', 'determine_text_color',
    'prep_node_labels', 'determine_node_position', 'parse_metapath_to_edge_names',
    'get_edge_weights_from_path_weights', 'build_subgraph_from_paths', 'highlight_path_of_interest',
    'build_explanitory_graph', 'draw_explanitory_graph']


def shift_centers_to_min_distance(center_data, min_distance=1.2):
    """
    Given x,y positions, changes the positions until `min_distance` apart.
    Two elements that are closer than `min_distance` apart, will be pushed in opposite directions
    a distance of 2*(`min_distance` - their current distance).  This will be iteratively
    performed on all elements until all are at minimum `min_distance` apart.

    :param center_data: DataFrame, with columns ['x', 'y'], float values
        corresponding to x and y positions.
    :param min_distance: float, the minimum distance all rows will be in x,y space after shifting
        their positions.

    :return: DataFrame, with same data as `center_data` but ['x', 'y'] columns updated.
    """


    shifts_made = True

    while shifts_made:
        shifts_made = False
        d = distance.cdist(center_data.loc[:, ['x', 'y']].values, center_data.loc[:, ['x', 'y']].values)

        # Determine nodes that are too close
        c1_ix, c2_ix = np.where(d < min_distance)

        done = []

        for i1, i2 in zip(c1_ix, c2_ix):

            if i1 == i2 or (i1, i2) in done:
                continue
            c1, c2 = center_data.loc[[i1, i2], ['x', 'y']].values
            done.append((i1, i2))
            done.append((i2, i1))

            # Calculate how far and what direction to shift circle centers
            dx, dy = np.abs(c2 - c1)
            dist = np.sqrt(dx**2 + dy**2)

            # Sin opp / hypo
            if dist == 0:
                sin_theta = 1
            else:
                sin_theta = np.abs(dy / dist)

            # cos = sqrt (1 - sin^2)
            cos_theta = np.sqrt(1 - sin_theta**2)

            shift_dist = min_distance - dist

            shift_x = cos_theta*shift_dist
            shift_y = sin_theta*shift_dist

            # Make the shifts
            if c1[0] >= c2[0]:
                center_data.loc[i1, 'x'] += shift_x
                center_data.loc[i2, 'x'] -= shift_x
            else:
                center_data.loc[i1, 'x'] -= shift_x
                center_data.loc[i2, 'x'] += shift_x

            if c1[1] >= c2[1]:
                center_data.loc[i1, 'y'] += shift_y
                center_data.loc[i2, 'y'] -= shift_y
            else:
                center_data.loc[i1, 'y'] -= shift_y
                center_data.loc[i2, 'y'] += shift_y

            shifts_made = True

    return center_data


def darken_hex_color(hex_color, strength=.3):
    """
    Given a color in hex, decrease the luminance by a factor of strength.
    The closer to 0 strength is, the darker the result.
    """
    rgb_color = sns.color_palette([hex_color])[0]
    darkened_rgb = np.array(rgb_color) * strength
    darkened_hex = sns.color_palette([darkened_rgb]).as_hex()[0]
    return darkened_hex


def determine_text_color(hex_color, max_luminance=.5):
    """
    Given a color in hex, if the color's luminance is greater than max_luminance,
    return 'k' for black, else 'w' for white.
    """

    # RGB, Huyman eye favors green color...
    color_wt = [0.299, 0.587, 0.114]

    rgb_color = np.array(sns.color_palette([hex_color])[0])
    luminance = (color_wt * rgb_color).sum()

    if luminance > max_luminance:
        return 'k'
    else:
        return 'w'


def prep_node_labels(label, max_line_len, spl_chars=None):
    """
    Adds new-line characters to node labels approximately every `max_line_len` characters. Only
    adds new-lines after characters contained in spl_chars.

    :param label: str, the string to add newline characters to
    :param max_line_len: int, the approximate number of characters before adding a newline
    :param spl_chars: list, the characters to add newlines after.

    :return: str, the label with newline characteres added
    """

    spl_chars = [' ', '-', ']', ')', '\n']
    out = ''
    start = 0

    # Add an absolute maximum for the labels.
    for i in range(len(label)):
        end = start + max_line_len

        # Youve got a subset that longer than the line length, so break
        if end > len(label):
            break

        # Look for split characters in the current substring, if not,
        # Extend the substring 1 character at a time until a split character is found
        spl_idxs = []
        while len(spl_idxs) == 0 and end != len(label):
            for char in spl_chars:
                try:
                    spl_idxs.append(label[start:end][::-1].index(char))
                except:
                    pass
            if len(spl_idxs) == 0:
                end += 1

        # if multiple split characters found, split on the one that makes the current line longest.
        if len(spl_idxs) > 0:
            spl_idx = min(spl_idxs)
            out += label[start: end-spl_idx].rstrip(' ').rstrip('\n') + '\n'
            start = end-spl_idx
            end = start + max_line_len

    # Add back in the last section of the string
    out += label[start:]
    return out


def determine_node_position(list_of_paths, node_id_to_label=None, xscale=10, min_dist=1.2):
    """
    Determines the positions for nodes in an explanitory graph

    :param list_of_paths: list of list, inner list contains node ids within a single path,
        outer list is a list of these paths
    :param node_id_to_label: dict, Optional. Maps node identifers to node types. This only becomes important
        if the same identifier is used with different labels.
            e.g. Using names as identifiers, Alzheimer's could be both a Disease and a Phenotype, and must be
                treated as distinct entities.
    :param xscale: int, the scaling factor for x positions. The scaling factor for y is the number of paths passed.
    :param min_dist: float, the minimum distance node centers must be from each other in xscale,yscale space.

    :return: dict, node_id as key, tuple of (x_pos, y_pos) as values.
    """

    node_positions = defaultdict(list)
    num_paths = len(list_of_paths)
    yscale = num_paths * min_dist

    # Keep track of nodes that appear first for better positioning
    node_num = 0
    dof = max(num_paths-1, 1) # Prevent divide by zero errors
    for n, path in enumerate(list_of_paths):
        for i, node in enumerate(path):
            node_positions['node'].append(node)
            if node_id_to_label is not None:
                node_positions['label'].append(node_id_to_label[node])
            else:
                node_positions['label'].append('NA')
            node_positions['x'].append((i / (len(path) - 1)) * xscale)
            node_positions['y'].append((1 - (n / dof)) * yscale)
            node_positions['node_num'].append(node_num)
            node_num += 1

    node_positions = pd.DataFrame(node_positions)

    # Nodes to appear first will retain their positions, helps keep compound and disease of interest grounded
    node_nums = node_positions.groupby(['node', 'label'])['node_num'].min().reset_index()
    node_positions = pd.merge(node_positions.drop('node_num', axis=1), node_nums, on=['node', 'label'])

    # For nodes that appear more than once, take their average position
    node_positions = node_positions.groupby(['node', 'label']).mean().reset_index()
    node_positions = node_positions.sort_values('node_num').reset_index(drop=True)

    # Shift nodes to minimize overlaps
    node_positions = shift_centers_to_min_distance(node_positions, min_dist)
    return node_positions.set_index('node')[['x', 'y']].apply(tuple, axis=1).to_dict()


def parse_metapath_to_edge_names(mp_abbrev, mp_info, inv_map=None):
    """
    Turns a metapath abbrevation into a list of names

    :param mp_abbrev: str, the abbreviation of the metapath
    :param mp_info: dict, key: metapath abbrevation, value: hetnetpy.hetnet.MetaPath. allows the metapath
        to be parsed
    :param inv_map: dict, a map for edge semmantic changes if the edge is inverted.
        e.g. inv_map['inhibits'] = 'inhibited_by'

    :return: list, the names of each edge in the metapath in order of appearance
    """


    edge_names = []

    this_mp = mp_info[mp_abbrev]

    for edge in this_mp.edges:
        if inv_map is not None and edge.inverted:
            edge_names.append(inv_map[edge.kind])
        else:
            edge_names.append(edge.kind)

    return edge_names


def get_edge_weights_from_path_weights(list_of_paths, path_weights, list_of_edges=None):
    """
    Determines weights for each edge in a list of paths from weights for the total path

    :param list_of_paths: list of lists, inner list contains node ids within a single path,
        outer list is a list of these paths
    :param path_weights: list of float, requred to be same length as list_of_paths. Weights should be between 0 and 1.
    :param list_of_edges: list of lists, Optional. Inner list is the semmantic type for each edge in a path,
        outer list is a list of these paths. Requred to be same length as list_of_paths.

    :return: dict, key: tuple, (source_id, target_id, [edge_semmantics]), value: float, edge_weight
    """

    edge_weights = defaultdict(list)
    grouper = ['source', 'target']
    if list_of_edges is not None:
        grouper.append('label')

    for n, (nodes, weight) in enumerate(zip(list_of_paths, path_weights)):
        for i, node in enumerate(nodes):

            try:
                edge_weights['target'].append(nodes[i+1])
                edge_weights['source'].append(node)
                edge_weights['weight'].append((1+weight)**2)
                if list_of_edges is not None:
                    edge_weights['label'].append(list_of_edges[n][i])
            except:
                pass
    edge_weights = pd.DataFrame(edge_weights)
    return edge_weights.groupby(grouper).sum().to_dict()['weight']


def build_subgraph_from_paths(list_of_paths, list_of_edges=None, path_weights=None):
    """
    Determines weights for each edge in a list of paths from weights for the total path

    :param list_of_paths: list of lists, inner list contains node ids within a single path,
        outer list is a list of these paths
    :param list_of_edges: list of lists, Optional. Inner list is the semmantic type for each edge in a path,
        outer list is a list of these paths. Requred to be same length as list_of_paths.
    :param path_weights: Optional, list of float, requred to be same length as list_of_paths.
        Weights should be between 0 and 1.

    :return: dict, key: tuple, (u_for_edge_id, v_for_edge_id, [edge_semmantics]), value: float, edge_weight
    """

    subgraph = defaultdict(list)
    grouper = ['u_for_edge', 'v_for_edge']
    if list_of_edges is not None:
        grouper.append('key')

    for n, nodes in enumerate(list_of_paths):
        for i, node in enumerate(nodes):
            try:
                subgraph['v_for_edge'].append(nodes[i+1])
                subgraph['u_for_edge'].append(node)
                if path_weights is not None:
                    subgraph['weight'].append((1+path_weights[n])**2)
                if list_of_edges is not None:
                    subgraph['key'].append(list_of_edges[n][i])
            except:
                pass
    subgraph = pd.DataFrame(subgraph)
    return subgraph.groupby(grouper).sum().reset_index()


def highlight_path_of_interest(list_of_paths, path_of_interest):
    """
    Selects a highlight color for edges in a path of interest.

    :param list_of_paths: list of lists, inner list contains node ids within a single path,
        outer list is a list of these paths
    :param path_of_interest: list, the node identifiers for nodes in a path to highlight.

    :return: dict, key: tuple (source_id, target_id) for edges, value: hex color for edges.
    """
    highlight_ec = sns.color_palette().as_hex()[1]
    default_ec = sns.color_palette().as_hex()[2]

    subgraph = build_subgraph_from_paths(list_of_paths)
    node_ids = subgraph[['u_for_edge', 'v_for_edge']].stack().unique()

    if all([p in node_ids for p in path_of_interest]):

        poi_tups = [(path_of_interest[i], path_of_interest[i+1]) for i in range(len(path_of_interest)-1)]
        subgraph['color'] = subgraph[['u_for_edge', 'v_for_edge']].apply(tuple, axis=1)
        # Use a highlight color for paths of interest, otherwise use no color
        subgraph['color'] = subgraph['color'].apply(lambda et: highlight_ec if et in poi_tups else default_ec)
    else:
        subgraph['color'] = default_ec

    return subgraph.set_index([c for c in subgraph.columns if c != 'color'])['color'].to_dict()


def build_explanitory_graph(list_of_paths, list_of_edges=None, path_weights=None, edge_weights=None,
                            node_id_to_color=None, node_id_to_label=None, edge_id_to_color=None,
                            min_dist=1.2, xscale=10):
    """
    Builds an explantory graph from minimally a list of paths. More parameters can be passed to build a more
    complete and expressive graph.

    :param list_of_paths: list of lists, inner list contains node ids within a single path,
        outer list is a list of these paths
    :param list_of_edges: list of lists, Optional. Inner list is the semmantic type for each edge in a path,
        outer list is a list of these paths. Requred to be same length as list_of_paths.
    :param path_weights: list of float, Optional. requred to be same length as list_of_paths.
        Weights should be between 0 and 1. Should not be used with `edge_weights`, or values
        will be overriden.
    :param edge_weights: dict, Optional. Key is edge tuple, value is weight, ideally between 0 and 1.
        If no values passed for `list_of_edges`, key must be (start_id, end_id) for an edge, or weights.
        will be igorned. If `list_of_edges` is passed, then key should be (start_id, end_id, edge_type),
        but if edge_type missing, the same wight will be applied to all edges between start_id, end_id.
        `edge_weights` will override `path_weights` if both paramaters are provided.
    :param node_id_to_color: dict, Optional. Provides color for a node. Key: node identifier,
        value: hex color for node, e.g. '#1f77b4'.
    :param node_id_to_label: dict, Optinal. Provides types or labels for nodes. Will be used to
        to color nodes by label if `node_id_to_color` is None. Colors determined by current
        seaborn.color_palette(). If palette has fewer colors than number of node labels, then
        a seaborn.hls_palette() with the numer of node labels will be utilized.
    :param edge_id_to_color: dict, Optional. Key is edge tuple, value is hex color for edge.
        If no values passed for `list_of_edges`, key must be (start_id, end_id) for an edge, or colors
        will be igorned. If `list_of_edges` is passed, then key should be (start_id, end_id, edge_type).
        Ideally, use `highlight_path_of_interest` to generate this mapping dictionay.
    :param min_dist: float, the minmum distance each node will be from each other in the final graph.
    :param xscale: a scaling factor for the width of the network. X position for paths will start at,
        0 and end at xscale. Y position is path number. `min_dist` will be is built on this scale.

    :return: networkx Graph (DiGraph or MultiDiGraph depending on whether or not `list_of_edges` was passed).
        Graph can be used on it's on as input for `draw_explanitory_graph`.
    """

    # Build node and edge data
    node_positions = determine_node_position(list_of_paths, node_id_to_label, xscale, min_dist)
    node_info = pd.DataFrame(node_positions).T.reset_index()
    node_info.columns = ['node_for_adding', 'x', 'y']

    subgraph = build_subgraph_from_paths(list_of_paths, list_of_edges, path_weights)

    # Add edge weights if passed
    if edge_weights is not None:
        first_key = list(edge_weights.keys())[0]
        # Fill weights with mapping tuple for edge
        if len(first_key) == 3 and 'key' in subgraph:
            subgraph['weight'] = subgraph[['u_for_edge', 'v_for_edge', 'key']].apply(tuple, axis=1)
        elif len(first_key) == 3:
            print('Provided edge weights with edge types,  but no edge types in graph. Ignoring weights.')
        else:
            subgraph['weight'] = subgraph[['u_for_edge', 'v_for_edge']].apply(tuple, axis=1)
        # Map the edge key to the weight
        if 'weight' in subgraph:
            subgraph['weight'] = subgraph['weight'].map(edge_weights)

    # Set default edge weight if none passed
    if 'weight' not in subgraph:
        subgraph['weight'] = 1

    # Set node colors
    if node_id_to_color is None:
        # If we can map nodes to types, color by type
        if node_id_to_label is not None:
            node_labels = sorted(list(set(node_id_to_label.values())))
            n_labels = len(node_labels)
            colors = sns.color_palette().as_hex()

            # Make sure there's enough unique colors
            if len(colors) < n_labels:
                colors = sns.hls_palette(n_labels, l=.6).as_hex()
            node_label_to_color = {l: c for l, c in zip(node_labels, colors)}

            # Create a color map for the nodes
            node_id_to_color = {n: node_label_to_color[node_id_to_label[n]] for n in node_info['node_for_adding']}

        # if no node typing select default color
        else:
            color = sns.color_palette().as_hex()[-1]
            node_id_to_color = {n: color for n in node_info['node_for_adding']}

    # Apply the colors
    node_info['color'] = node_info['node_for_adding'].map(node_id_to_color)

    # Set edge colors
    if edge_id_to_color is not None:
        first_key = list(edge_id_to_color.keys())[0]
        # Fill colors with mapping tuple for edge
        if len(first_key) == 3 and 'key' in subgraph:
            subgraph['color'] = subgraph[['u_for_edge', 'v_for_edge', 'key']].apply(tuple, axis=1)
        else:
            subgraph['color'] = subgraph[['u_for_edge', 'v_for_edge']].apply(tuple, axis=1)
        # Map the edge key to the color
        if 'color' in subgraph:
            subgraph['color'] = subgraph['color'].map(edge_id_to_color)
    else:
        subgraph['color'] = sns.color_palette().as_hex()[2]

    # Build the graph
    if 'key' in subgraph:
        G = nx.MultiDiGraph()
    else:
        subgraph = subgraph.rename(columns={'u_for_edge': 'u_of_edge', 'v_for_edge': 'v_of_edge'})
        G = nx.DiGraph()

    for n in node_info.T.to_dict().values():
        G.add_node(**n)
    for e in subgraph.T.to_dict().values():
        G.add_edge(**e)
    return G


def draw_explanitory_graph(G, node_id_to_name=None, proba=None, n_paths=None, xscale=10, max_line_len=15, title=True,
                           node_size=6000):
    """
    Funciton to draw an explanatory graph. Ideally the graph should be genrated from the fucntion
    `build_explanitory_graph`.  All required values for plotting will be added by using that function.
    :param G: networkx Graph, MultiGraph, DiGraph, or MultiDigraph.  Specific values are required in the
        nodes and edges for proper drawing:
            Nodes: 'x': x position for drawing, 'y': y position for drawing, 'color': hex color for the node
            Edges: 'weight': weight for determining edge thickness, 'color': hex color for the edge
        For best results, use `build_explanitory_graph` function for producing G.
    :param node_id_to_name: dict, identifer of nodes in G to name, for printing node labels in graph
    :param proba: float, a value to be printed next to the name of the start node... primarily used for
        probability of treatment in a machine learning context. Requires title=True to appear
    :param n_paths: int, y scaling factor. Total height of the figure. If None, will use values pre-determined when
        building G.
    :param xscale: int, The scaling facor for the x axis
    :param max_line_len: int, the Maximum length of the line for node text labels
    :param title: bool, if true, will pull out the first node in the paths as a title
    :param node_size: int, allow for larger nodes to be drawn
    :return: matplotlib figure
    """

    width = 12 * xscale/10

    max_y = max([G.nodes[n]['y'] for n in G.nodes])

    if n_paths is not None:
        height = n_paths
    else:
        height= max_y

    if height / width > 1.3:
        width = height / 1.3

    fig = plt.figure(figsize=(width, height))

    # Build Node Position map
    node_pos_dict = {}
    for n in G.nodes:
        x = G.nodes[n]['x']
        y = G.nodes[n]['y']
        node_pos_dict[n] = (x, y)

    # Extract other node properties
    node_colors = [G.nodes[n]['color'] for n in G.nodes]

    # Build the edge labels if needed
    edge_label_dict = {}
    for e in G.edges:
        if len(e) == 2:
            edge_label_dict = None
            break
        edge_label_dict[(e[0], e[1])] = e[2]

    # Extract other edge properties
    edge_width = [3*G.edges[e]['weight'] for e in G.edges]
    edge_color = [G.edges[e]['color'] for e in G.edges]

    nx.draw(G, pos=node_pos_dict, node_color=node_colors, node_size=node_size,
            edge_color=edge_color, width=edge_width)

    if edge_label_dict is not None:
        nx.draw_networkx_edge_labels(G, pos=node_pos_dict, edge_labels=edge_label_dict)

    # Default to node id if no names passed
    if node_id_to_name is None:
        node_id_to_name = {n: n for n in G.nodes}

    wt_lbls = {}
    bk_lbls = {}
    for i, node in enumerate(G.nodes):
        node_color = G.nodes[node]['color']
        if determine_text_color(node_color) == 'w':
            wt_lbls[node] = prep_node_labels(node_id_to_name[node], max_line_len)
        else:
            bk_lbls[node] = prep_node_labels(node_id_to_name[node], max_line_len)

    wt_labels = nx.draw_networkx_labels(G, pos=node_pos_dict, labels=wt_lbls, font_color='w')
    bk_labels = nx.draw_networkx_labels(G, pos=node_pos_dict, labels=bk_lbls, font_color='k')

    for v in wt_labels.values():
        v.set_path_effects([pe.withStroke(linewidth=2, foreground='k')])

    if title:
        # Add probabilities
        first_node = list(G.nodes)[0]
        first_text = node_id_to_name[first_node]

        if proba is not None:
            first_text += ': {:1.3f}'.format(proba)

        # Color the same as the Node
        first_color = G.nodes[first_node]['color']
        text = plt.text(0, max_y, first_text, c=first_color, size=16, fontweight='bold')
        # If a light color, Add a dark outline for readability
        if determine_text_color(first_color, .6) == 'k':
            text.set_path_effects([pe.withStroke(linewidth=2, foreground=darken_hex_color(first_color))])

    fig.set_tight_layout(True)
    return fig
