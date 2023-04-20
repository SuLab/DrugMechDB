import pandas as _pd
from tqdm import tqdm as _tqdm
from ._graphs import combine_nodes_and_edges
from hetnetpy.abbreviation import find_abbrevs as _find_abbrevs


__all__ = ['change_edge_type', 'map_edge_types_from_file', 'remove_edges', 'add_abbrevs']


def remove_edges(to_remove, edges, target_type):
    """
    Removes a subset of edges of a given type from an edge dataframe.
    Generally used in the context of machine learning for holdout edges from a gold standard.
    """

    # Separate the edge type to filter
    keep_edges = edges.query('type != @target_type')
    to_filter_edges = edges.query('type == @target_type')

    # Create a set of edges for set operations
    remove_pairs = set([(tup.start_id, tup.end_id) for tup in to_remove.itertuples()])
    target_pairs = set([(tup.start_id, tup.end_id) for tup in to_filter_edges.itertuples()])

    remaining_edges = target_pairs - remove_pairs

    # Make the filtered results into a dataframe
    out = pd.DataFrame({'start_id': [tup[0] for tup in remaining_edges],
                        'end_id': [tup[1] for tup in remaining_edges],
                        'type': target_type})

    # Return the results
    return pd.concat([keep_edges, out], sort=False, ignore_index=True)


def add_abbrevs(nodes, edges, kind_to_abbrev=None, type_to_dir=None):
    """
    Generates and adds abbrevations to a DataFrame of edges.

    :param nodes: DataFrame of node information (standard format)
    :param edges: DataFrane of edges (standard format)
    :param kind_to_abbrev: dict, map from `label` (for nodes) or `type` (for edges) to abbrevation
        if None is passed, unique abbreviations will be generated, but the simple generation algorithm will
        potentailly generate un-necessarily long abbrevations. It is best practives to select your own
        abbrevations and pass them as a value here.
    :param type_to_dir: dict, map from edge `type` to boolean, True if the edge is directed, False if the edge is not.
        Will only add directed syntax to edges that pass to the same metanode (e.g. Reaction preceeds Reaction)

    :return: DataFrame, edges with an added abbrev column containing the abbreviation for the edge.
    """

    # Get all the types and labels to ensure that all are mapped
    all_kinds = nodes['label'].unique().tolist() + edges['type'].unique().tolist()

    # Make sure all edge types are classifiable as directed or not. If missing, throw an error
    # before doing any expenive mappings
    if type_to_dir is not None:
        assert len(set(edges['type']) - set(type_to_dir.keys())) == 0

    # Do simple abbreviation generation if not passed
    if kind_to_abbrev is None:
        kind_to_abbrev = _find_abbrevs(all_kinds)

    # Ensure all the kinds are mappable to an abbrevation
    elif len(set(all_kinds) - set(kind_to_abbrev.keys())) != 0:
        # Keep original abbrevs, adding in new missing ones
        # find_abbrevs() guarntees unique abbrevations (though some may be unnessarily long)
        kind_to_abbrev = {**_find_abbrevs(all_kinds), **kind_to_abbrev}

    # Generate a map for all nodes
    id_to_abbrev = nodes.set_index('id')['label'].map(kind_to_abbrev).to_dict()

    # map the nodes
    edges['start_abbv'] = edges['start_id'].map(id_to_abbrev)
    edges['end_abbv'] = edges['end_id'].map(id_to_abbrev)

    # Build the full edge abbrevation from the node abbrevs and the edge type
    edges['abbrev'] = edges['start_abbv'] + edges['type'].map(kind_to_abbrev) + edges['end_abbv']

    # Account for directed edges
    if type_to_dir is not None:
        # Find where directed and start type == end type
        directed_idx = (edges['start_abbv'] == edges['end_abbv']) & edges['type'].map(type_to_dir)
        directed_idx = directed_idx[directed_idx].index

        edges.loc[directed_idx, 'abbrev'] = edges['start_abbv'] + edges['type'].map(kind_to_abbrev) + '>' + edges['end_abbv']

    return edges.drop(['start_abbv', 'end_abbv'], axis=1)


def change_edge_type(edges, idx, new_type, swap=False):
    """
    In-place change of an edge type in a hetnet file.
    """
    edges.loc[idx, 'type'] = new_type
    if swap:
        tmp = edges.loc[idx, 'start_id']
        edges.loc[idx, 'start_id'] = edges.loc[idx, 'end_id']
        edges.loc[idx, 'end_id'] = tmp


def map_edge_types_from_file(edges, map_df, orig_type='type', new_type='new_type',
                              swap_label='reverse_node_labels', nodes=None,
                              start_label='start_label', end_label='end_label',
                              prog=True):
    """
    In-place updater of Edge Types from a mapping dataframe
    """

    # Option to strictly enforce node typing
    if nodes is not None:
        combo = combine_nodes_and_edges(nodes, edges)

    def inner_func():

        # Strict type encforment if all variables there (allows for sloppy edge abbreviations)
        if nodes is not None:
            sl = getattr(row, start_label)
            el = getattr(row, end_label)
            from_type = getattr(row, orig_type)

            to_change = combo.query('start_label == @sl and end_label == @el and type == @from_type').index
        else:
            from_type = getattr(row, orig_type)
            to_change = edges.query('type == @from_type').index

        to_type = getattr(row, new_type)
        swap = getattr(row, swap_label)
        if _pd.isnull(swap):
            swap = False

        change_edge_type(edges, to_change, to_type, swap)

    if prog:
        for row in _tqdm(map_df.itertuples(), total=len(map_df)):
            inner_func()
    else:
        for row in map_df.itertuples():
            inner_func()

    edges.dropna(subset=['type'], inplace=True)
    edges.reset_index(drop=True, inplace=True)

