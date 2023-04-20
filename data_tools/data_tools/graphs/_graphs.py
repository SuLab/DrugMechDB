import random as _random
import pandas as _pd
from collections import OrderedDict as _oDict
from ..df_processing import combine_group_cols_on_char

__all__ = ['get_direction_from_abbrev', 'get_edge_name', 'map_id_to_value',
            'parse_edge_abbrev', 'get_abbrev_dict_and_edge_tuples', 'combine_nodes_and_edges',
            'get_node_degrees', 'add_colons', 'remove_colons', 'determine_split_string',
            'order_cols', 're_id_nodes', 're_id_edges', 'prune_leaf_nodes', 'get_core_network',
            'permute_edges', 'permute_graph']


def get_direction_from_abbrev(abbrev):
    """Finds the direction of a metaedge from its abbreviaton"""
    if '>' in abbrev:
        return 'forward'
    elif '<' in abbrev:
        return 'backward'
    else:
        return 'both'


def get_edge_name(edge):
    """Separates the edge name from its abbreviation"""
    # the true edge name is everything before the final '_' character
    # so if we have PROCESS_OF_PpoP, we still want to keep 'PROCESS_OF' with the underscores intact.
    return '_'.join(edge.split('_')[:-1])


def map_id_to_value(nodes, value):
    """Maps Node id to another value"""
    return remove_colons(nodes).set_index('id')[value].to_dict()


def parse_edge_abbrev(edge_abbrev):
    """
    Splits an edge abbrevation into subject abbrev, predicate abbrev, object abbrev.
    e.g. 'CbG' returns ('C', 'b', 'G') or 'CDreg>CD' returns ('CD', 'reg', 'CD')

    param: edge_abbrev, string, the abbreviation for the edge type

    return: tuple of strings, each of the type abbrevatinos in the subeject predicate object triple.
    """
    ## TODO Compare to regex impolementation. see: https://github.com/hetio/hetnetpy/blob/master/hetnetpy/abbreviation.py#L164

    e_type_abbrev = ''
    start_abbrev = ''
    end_abbrev = ''

    start = True
    for char in edge_abbrev:
        # Direction is not in abbreviations, skip to next character
        if char == '>' or char == '<':
            continue

        # When the abbreviation is in uppercase, abbreviating for node type
        if char == char.upper():
            if start:
                start_abbrev += char
            else:
                end_abbrev += char

        # When abbreviation is lowercase, you have the abbreviation for the edge
        if char == char.lower():
            # now no longer on the start nodetype, so set to false
            start = False
            e_type_abbrev += char

    return (start_abbrev, e_type_abbrev, end_abbrev)


def get_abbrev_dict_and_edge_tuples(nodes, edges):
    """
    Returns an abbreviation dictionary generated from class variables.
    Required input for metagraph functions in the hetnetpy package.

    Edge types are formatted as such:
        edge-name_{START_NODE_ABBREV}{edge_abbrev}{END_NODE_ABBREV}
        e.g. Compound-binds-Gene is: binds_CbG

    Therefore, abbreviations for edge and node types can be extracted from the full edge name.
    """
    nodes = remove_colons(nodes)
    edges = remove_colons(edges)

    id_to_kind = nodes.set_index('id')['label'].to_dict()

    node_kinds = nodes['label'].unique()
    edge_kinds = edges['type'].unique()

    # If we have a lot of edges, lets reduce to one of each type for faster queries later.
    edge_kinds_df = edges.drop_duplicates(subset=['type'])

    # Extract just the abbreviation portion
    edge_abbrevs = [e.split('_')[-1] for e in edge_kinds]

    # Initialize the abbreviation dict (key = fullname, value = abbreviation)
    node_abbrev_dict = dict()
    edge_abbrev_dict = dict()
    metaedge_tuples = []

    for i, kind in enumerate(edge_kinds):
        edge_name = get_edge_name(kind)
        start_abbrev, edge_abbrev, end_abbrev = parse_edge_abbrev(edge_abbrevs[i])

        # Have proper edge abbreviation
        edge_abbrev_dict[edge_name] = edge_abbrev

        # Have abbreviations, but need to get corresponding types for start and end nodes
        edge = edge_kinds_df.query('type == @kind').iloc[0]
        start_kind = id_to_kind[edge['start_id']]
        end_kind = id_to_kind[edge['end_id']]

        node_abbrev_dict[start_kind] = start_abbrev
        node_abbrev_dict[end_kind] = end_abbrev

        direction = get_direction_from_abbrev(kind)
        edge_tuple = (start_kind, end_kind, edge_name, direction)
        metaedge_tuples.append(edge_tuple)

    return {**node_abbrev_dict, **edge_abbrev_dict}, metaedge_tuples


def combine_nodes_and_edges(nodes, edges):
    """Combines data from nodes and edges frames into a single dataframe"""

    nodes = remove_colons(nodes)
    edges = remove_colons(edges)

    id_to_name = map_id_to_value(nodes, 'name')
    id_to_label = map_id_to_value(nodes, 'label')

    out_df = edges.copy()

    out_df['start_name'] = out_df['start_id'].apply(lambda i: id_to_name[i])
    out_df['end_name'] = out_df['end_id'].apply(lambda i: id_to_name[i])

    out_df['start_label'] = out_df['start_id'].apply(lambda i: id_to_label[i])
    out_df['end_label'] = out_df['end_id'].apply(lambda i: id_to_label[i])

    return out_df


def get_node_degrees(edges):
    """Determines the degrees for all nodes"""
    return _pd.concat([remove_colons(edges)['start_id'], remove_colons(edges)['end_id']]).value_counts()


def add_colons(df, id_name='', col_types={}):
    """
    Adds the colons to column names before neo4j import (presumably removed by `remove_colons` to make queryable).
    User can also specify  a name for the ':ID' column and data types for property columns.

    :param df: DataFrame, the neo4j import data without colons in it (e.g. to make it queryable).
    :param id_name: String, name for the id property.  If importing a CSV into neo4j without this property,
                    Neo4j mayuse its own internal id's losing this property.
    :param col_types: dict, data types for other columns in the form of column_name:data_type
    :return: DataFrame, with neo4j compatible column headings
    """
    reserved_cols = ['id', 'label', 'start_id', 'end_id', 'type']

    # Get the reserved column names that need to be changed
    to_change = [c for c in df.columns if c.lower() in reserved_cols]
    if not to_change:
        raise ValueError("Neo4j Reserved columns (['id', 'label' 'start_id', 'end_id', 'type'] not " +
                         "found in DataFrame")

    # Add any column names that need to be types
    to_change += [c for c in df.columns if c in col_types.keys()]

    change_dict = {}
    for name in to_change:
        # Reserved column names go after the colon
        if name.lower() in reserved_cols:
            if name.lower() == 'id':
                new_name = id_name + ':' + name.upper()
            else:
                new_name = ':' + name.upper()
        else:
            # Data types go after the colon, while names go before.
            new_name = name + ':' + col_types[name].upper()
        change_dict.update({name: new_name})

    return df.rename(columns=change_dict)


def remove_colons(df):
    """
    Removes colons from column headers formatted for neo4j import to make them queryable

    :param df: DataFrame, formatted for neo4j import (column lables ':ID', ':LABEL, 'name:STRING' etc).
    :return: DataFrame, with column names that are queryable (e.g. 'id', 'label', 'name').
    """
    # Figure out which columns have : in them
    to_change = [c for c in df.columns if ':' in str(c)]
    new_labels = [c.lower().split(':') for c in to_change]

    # keep the reserved types, or names
    reserved_cols = ['id', 'label', 'start_id', 'end_id', 'type']
    new_labels = [l[1] if l[1] in reserved_cols else l[0] for l in new_labels]

    # return the DataFrame with the new column headers
    change_dict = {k: v for k, v in zip(to_change, new_labels)}
    return df.rename(columns=change_dict)


def determine_split_string(edge):
    """
    Determines the correct character to split a string representation of an edge into [node1, edge, node2].

    e.g. 'Node1 - links_to - Node2' will return ' - '
         'Node3 > part_of > Node2' will return ' > '
    """
    if '-' in edge:
        return ' - '
    elif '>' in edge:
        return ' > '
    elif '<' in edge:
        return ' < '


def order_cols(df):
    """
    Given a DataFrame representation of Nodes or Edges (or a combo) will standardize column order with IDs first.
    """
    order = ['id', 'name', 'label', 'start_id', 'end_id',
             'start_name', 'type', 'end_name', 'start_label',
             'end_label']
    order = [o for o in order if o in df.columns]
    return df[order + [c for c in df.columns if c not in order]]


def re_id_edges(edges, id_map_df, old_id_col=0, new_id_col=1):
    """
    Changes identifiers in an edge DataFrame. Uses merge so 1 to many and many to many mappings are preserved.

    :param edges: DataFrame, edges to be modified
    :param id_map_df: DataFrame, the mappings from old to new ID. By default column 0 is the old ID and column 1
        is the new ID.
    :param old_id_col: int or string, name or index of column of original identifiers.
    :param new_id_col: int or string, name or index of column of new identifier.

    :return: DataFrame with the new identifiers
    """

    # If integers passed for columns, reindex to integers
    if old_id_col in [0, 1] and new_id_col in [0,1]:
        id_map_df.columns = [0, 1]

    old_ids = id_map_df[old_id_col].values

    # Query for the edges that will not be altered
    untouched_edges = edges.query('start_id not in @old_ids and end_id not in @old_ids')

    # Change the start edge Identifiers
    start_edges = edges.query('start_id in @old_ids')
    start_edges_out = start_edges.merge(id_map_df, left_on='start_id', right_on=old_id_col, how='left')
    start_edges_out = start_edges_out.drop(['start_id', old_id_col], axis=1).rename(columns={new_id_col: 'start_id'})

    # Edges with both ids needing changes
    both_edges = start_edges_out.query('end_id in @old_ids')
    start_edges_out = start_edges_out.query('end_id not in @old_ids')

    # Change the end edge Identifiers
    end_edges = edges.query('end_id in @old_ids and start_id not in @old_ids')
    end_edges = _pd.concat([end_edges, both_edges], sort=False)
    end_edges_out = end_edges.merge(id_map_df, left_on='end_id', right_on=old_id_col, how='left')
    end_edges_out = end_edges_out.drop(['end_id', old_id_col], axis=1).rename(columns={new_id_col: 'end_id'})

    # Concat and return
    return _pd.concat([untouched_edges, start_edges_out, end_edges_out], sort=False, ignore_index=True)


def re_id_nodes(nodes, id_map_df, old_id_col, new_id_col, new_first=True):
    """
    Changes identifiers of a Node DataFrame.

    :param nodes: The nodes with the old identifier map
    :param id_map_df: DataFrame, the mappings from old to new ID.
    :param old_id_col, str, the name of the column containing the original identifiers.
    :param new_id_col, str, the name of the column containing the new identifiers.
    :para new_first: bool, only important if 'id_map_df' contains additional column information like 'name'
        or 'label.' If True, will use the values in `id_map_df` and fill in missing values with those from `nodes`,
        if False, will use values from `nodes` before `id_map_df`

    :return: DataFrame of nodes with the updated identifiers
    """
    old_ids = id_map_df[old_id_col].values

    untouched_nodes = nodes.query('id not in @old_ids')

    change_nodes = nodes.query('id in @old_ids')
    change_nodes = change_nodes.merge(id_map_df[[old_id_col, new_id_col]], how='left', left_on='id', right_on=old_id_col)
    change_nodes = change_nodes.drop(['id', old_id_col], axis=1).rename(columns={new_id_col: 'id'})

    # if new node info is passed (besides the ID), hang on to it.
    new_node_info = id_map_df[[new_id_col] + [c for c in ['name', 'label', 'xrefs'] if c in id_map_df.columns]]
    new_node_info = new_node_info.rename(columns={new_id_col: 'id'})

    # Xref Accounting: any mappings performed should be saved into the 'xrefs' column
    xref_accounting = id_map_df[[new_id_col, old_id_col]].rename(columns={new_id_col: 'id', old_id_col: 'xrefs'})

    if new_first:
        out_nodes = [new_node_info, change_nodes, xref_accounting]
    else:
        out_nodes = [change_nodes, new_node_info, xref_accounting]

    out_nodes = _pd.concat(out_nodes, ignore_index=True, sort=False)
    out_nodes = combine_group_cols_on_char(out_nodes, ['id'], ['xrefs'], sort=True, prog=False)

    return _pd.concat([untouched_nodes, out_nodes], sort=False).sort_values(['label', 'id']).reset_index(drop=True)


def prune_leaf_nodes(nodes, edges, allow_types=None, allow_ids=None):
    """
    Remove leaf nodes from a network. allow_types lists node types ignore pruning, allow_ids ignores individal nodes.
    """

    if allow_types is None:
        allow_types = []
    if allow_ids is None:
        allow_ids = []

    to_prune = edges[['start_id', 'end_id']].stack().value_counts() == 1
    to_prune = to_prune[to_prune].index

    to_prune = set(nodes.query('id in @to_prune and label not in @allow_types')['id'])
    to_prune = to_prune - set(allow_ids)

    new_nodes = nodes.query('id not in @to_prune').copy()
    new_edges = edges.query('start_id not in @to_prune and end_id not in @to_prune').copy()

    return new_nodes, new_edges


def get_core_network(nodes, edges, allow_types=None, allow_ids=None):
    """
    Returns a 'core network' where all nodes are doubly connected (degree >= 2) through successive leaf pruning.

    :param nodes: DataFrame, the nodes for the network
    :param edges: DataFrame, the edges for the network
    :param allow_types: list of str, Node types (`label` column) to allow leaves (degree 1).
    :param allow_ids: list of str, node identifiers for nodes to not remove even if they have degree 1

    :returns: core_nodes, core_edges, DataFrames with all nodes degree >= 2 (excpet for allow arugments)
    """

    if allow_types is None:
        allow_types = []
    if allow_ids is None:
        allow_ids = set()
    elif type(allow_ids) != set:
        allow_ids = set(allow_ids)

    nodes_out = nodes.copy()
    edges_out = edges.copy()

    new_nodes_out, new_edges_out = prune_leaf_nodes(nodes_out, edges_out, allow_types, allow_ids)

    while(len(new_nodes_out) != len(nodes_out)):
        nodes_out = new_nodes_out.copy()
        edges_out = new_edges_out.copy()
        new_nodes_out, new_edges_out = prune_leaf_nodes(nodes_out, edges_out, allow_types, allow_ids)

    return nodes_out.reset_index(drop=True), edges_out.reset_index(drop=True)


def permute_edges(edges, directed=False, multiplier=10, excluded_edges=None, seed=0):
    """
    Permutes the edges of one metaedge in a graph while preserving the degree of each node.

    :param edges: DataFrame, edges information
    :param directed: bool, whether or not the edge is directed
    :param multiplier: int, governs the number of permutations, multiplied by number of edges
    :param excluded_edges: DataFrame, edges to exclude from final permuted edges
    :param seed: int, random state for analysis

    :return permuted_edges, stats: DataFrame, DataFrame - the permuted start and end ids, the permutation stats.
    """
    _random.seed(seed)

    orig_columns = edges.columns
    edges = remove_colons(edges)
    col_name_mapper = {k: v for k, v in zip(edges.columns, orig_columns)}

    # There shouldn't be any duplicate edges in the grpah, but throw error just in case
    assert len(edges) == len(edges.drop_duplicates(subset=['start_id', 'end_id']))

    # Ensure only 1 edge type was passed
    assert edges['type'].nunique() == 1
    e_type = edges['type'].unique()[0]

    edge_list = [(e.start_id, e.end_id) for e in edges.itertuples(index=False)]
    edge_set = set(edge_list)
    orig_edge_set = edge_set.copy()

    if excluded_edges is not None:
        excluded_edge_set = set([(e.start_id, e.end_id) for e in excluded_edges.itertuples(index=False)])
    else:
        excluded_edge_set = set()

    edge_number = len(edges)
    n_perm = int(edge_number * multiplier)

    # Initialize some perumtation stats
    count_self_loop = 0
    count_duplicate = 0
    count_undir_dup = 0
    count_excluded = 0

    step = max(1, n_perm // 10)
    print_at = list(range(step, n_perm, step)) + [n_perm - 1]

    stats = list()

    for i in range(n_perm):

        # Same two random edges without replacement
        i_0 = _random.randrange(edge_number)
        i_1 = i_0
        while i_0 == i_1:
            i_1 = _random.randrange(edge_number)

        edge_0 = edge_list[i_0]
        edge_1 = edge_list[i_1]

        unaltered_edges = [edge_0, edge_1]
        swapped_edges = [(edge_0[0], edge_1[1]), (edge_1[0], edge_0[1])]

        # Validate the new paring
        valid = False
        for edge in swapped_edges:
            # Self Loops
            if edge[0] == edge[1]:
                count_self_loop += 1
                break
                # Duplicate Edges
            if edge in edge_set:
                count_duplicate += 1
                break
                # Duplicate Undirected Edges
            if not directed and (edge[1], edge[0]) in edge_set:
                count_undir_dup += 1
                break
                # Edge is excluded
            if edge in excluded_edge_set:
                count_excluded += 1
                break
                # If we made it here, we have a valid edge
        else:
            valid = True

        # If BOTH new edges are valid
        if valid:

            # Change the edge list
            edge_list[i_0] = swapped_edges[0]
            edge_list[i_1] = swapped_edges[1]

            # Fix the sets for quick hashing
            for edge in unaltered_edges:
                edge_set.remove(edge)
            for edge in swapped_edges:
                edge_set.add(edge)

        if i in print_at:
            stat = _oDict()
            stat['cumulative_attempts'] = i
            index = print_at.index(i)
            stat['attempts'] = print_at[index] + 1 if index == 0 else print_at[index] - print_at[index - 1]
            stat['complete'] = (i + 1) / n_perm
            stat['unchanged'] = len(orig_edge_set & edge_set) / len(edges)
            stat['self_loop'] = count_self_loop / stat['attempts']
            stat['duplicate'] = count_duplicate / stat['attempts']
            stat['undirected_duplicate'] = count_undir_dup / stat['attempts']
            stat['excluded'] = count_excluded / stat['attempts']
            stats.append(stat)

            count_self_loop = 0
            count_duplicate = 0
            count_undir_dup = 0
            count_excluded = 0

    assert len(edge_list) == edge_number
    out_edges = _pd.DataFrame({'start_id': [edge[0] for edge in edge_list],
                              'end_id': [edge[1] for edge in edge_list],
                              'type': [e_type] * edge_number})

    out_edges = out_edges.rename(columns=col_name_mapper)

    return out_edges, _pd.DataFrame(stats)


def permute_graph(edges, multiplier=10, excluded_edges=None, seed=0):
    """
    Permutes the all of the metaedges types for those given in a graph file.

    :param edges: DataFrame, the edges to be permuted
    :param multiplier: int, governs the number of permutations to be performed
    :param excluded_edges: DataFrame, edges to be disallowed from final permutations
    :param seed: int, random state for analysis for reproduciability

    :return permuted_graph, stats: DataFrame, DataFrame - the edges of the graph permuted,
                                   stats on the permutations.
    """
    # Change columns names to pandas standard
    orig_columns = edges.columns
    edges = remove_colons(edges)
    col_name_mapper = {k: v for k, v in zip(edges.columns, orig_columns)}

    edge_types = edges['type'].unique()

    edge_stats = []
    permuted_edges = []
    for i, etype in enumerate(edge_types):
        to_permute = edges.query('type == @etype').copy()

        directed = '>' in etype or '<' in etype
        pedge, stats = permute_edges(to_permute, directed=directed, multiplier=multiplier,
                                     excluded_edges=excluded_edges, seed=seed + len(to_permute))

        permuted_edges.append(pedge)

        stats['etype'] = etype
        edge_stats.append(stats)

    stats = _pd.concat(edge_stats)
    permuted_graph = _pd.concat(permuted_edges)

    # Return column names to neo4j standards if applicable
    permuted_graph = permuted_graph.rename(columns=col_name_mapper)

    return permuted_graph, stats

