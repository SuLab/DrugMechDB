import re as _re
from collections import Counter as _Counter
from collections import defaultdict as _defaultdict
from hetnetpy.hetnet import MetaGraph as _MetaGraph, MetaEdge as _MetaEdge, MetaPath as _MetaPath
from ._graphs import get_abbrev_dict_and_edge_tuples


__all__ = ['dataframes_to_metagraph', 'metapaths_to_json', 'get_mn_abbrevs', 'get_e_type_abbrev',
           'extract_mp_edges', 'extract_mp_nodes', 'nodes_and_edges_to_path', 'metapath_to_list',
           'print_path_list', 'print_metapath', 'is_directed', 'find_inverted_edges', 'find_directed_inversion',
           'get_direction', 'find_node_index', 'inv_target', 'is_similarity', 'subset_mps_by_node_count']


def dataframes_to_metagraph(nodes, edges):
    """Converts Nodes and Edges DataFrame to a hetnetpy.hetnet.MetaGraph"""
    abbrev_dict, edge_tuples = get_abbrev_dict_and_edge_tuples(nodes, edges)
    return _MetaGraph.from_edge_tuples(edge_tuples, abbrev_dict)


def metapaths_to_json(metapaths):
    """
    Takes a list of objects of hetnetpy.hetnet.MetaPath, and extracts relevant info to a json (dict) structure
    """
    metapaths_out = dict()

    for mp in metapaths:
        if len(mp) == 1:
            continue
        mp_info = dict()
        mp_info['length'] = len(mp)
        mp_info['edges'] = [str(x) for x in mp.edges]
        mp_info['edge_abbreviations'] = [x.get_abbrev() for x in mp.edges]
        mp_info['standard_edge_abbreviations'] = [x.get_standard_abbrev() for x in mp.edges]

        metapaths_out[str(mp)] = mp_info
    return metapaths_out


def get_mn_abbrevs(me_abbrev):
    return _re.split('[a-z<>]', _re.sub("[<>]", "", me_abbrev))


def get_e_type_abbrev(me_abbrev):
    return _re.search("[a-z]+", _re.sub("[<>]", "", me_abbrev)).group()


def extract_mp_edges(mp, rev_map=None, abbrevs=False):
    """
    For a metapath, extracts the edge names and returns as a list.

    :param mp: hetnetpy.hetnet.MetaPath or json represntation (see `metapaths_to_json`), the MetaPath to extract.
    :param rev_map: dict, mapping from forward to reverse edge semmantics.
    :param abbrevs: bool, if True, will only return the abberevations for the edges rather than full names:

    :return: list of strings, the edge names in the metapath, in order of appearance
    """
    # Allow for hetnetpy.hetnet.MetaPath
    if type(mp) == _MetaPath:

        if abbrevs:
            edges = [_re.sub("[<>]", "", e.kind_abbrev) for e in mp.edges]
            return edges

        else:
            edges = [e.kind for e in mp.edges]

    # Also allow dict representation
    elif type(mp) == dict:
        if abbrevs and 'edge_abbreviations' in mp:
            edges = [get_e_type_abbrev(e) for e in mp['edge_abbreviations']]
            return edges

        # Getting the full names is a bit trickier
        elif 'edges' in mp:
            edges = mp['edges']
            # Extract the edge names only
            edges = [e.replace('>', '-').replace('<', '-').split(' - ')[1] for e in edges]

    else:
        raise TypeError

    # Get proper reversed edges in there if applicable
    if rev_map is not None:
        rev = find_inverted_edges(mp)
        edges = [rev_map[e] if r else e for r, e in zip(rev, edges)]

    return edges


def extract_mp_nodes(mp, abbrevs=False):
    """
    For a metapath, extracts the node names and returns as a list.

    :param mp: hetnetpy.hetnet.MetaPath or json represntation (see `metapaths_to_json`), the MetaPath to extract.
    :param abbrevs: bool, if True, will only return the abberevations for the nodes rather than full names:

    :return: list of strings, the node names in the metapath, in order of appearance
    """

    # Allow for hetnetpy.hetnet.MetaPath
    if type(mp) == _MetaPath:
        nodes = [e.source for e in mp.edges] + [mp.edges[-1].target]
        if not abbrevs:
            return [str(n) for n in nodes]
        else:
            return [n.abbrev for n in nodes]

    # Also allow dict representation
    elif type(mp) == dict:
        if not abbrevs and 'edges' in mp:
            edges = mp['edges']

            nodes = [e.replace('>', '-').replace('<', '-').split(' - ')[0] for e in edges] + \
                        [edges[-1].replace('>', '-').replace('<', '-').split(' - ')[-1]]
            return nodes
        elif abbrevs and 'edge_abbreviations' in mp:
            edges = mp['edge_abbreviations']
            nodes = [get_mn_abbrevs(abbrev)[0] for abbrev in edges] + [get_mn_abbrevs(edges[-1])[-1]]
            return nodes

    else:
        raise TypeError


def nodes_and_edges_to_path(nodes, edges):
    """Combine a list of nodes and edges into a single list for a path"""
    out = []
    for i in range(len(nodes)-1):
        out.append(nodes[i])
        out.append(edges[i])
    else:
        out.append(nodes[-1])
    return out


def metapath_to_list(mp, rev_map=None, n_abbv=False, e_abbv=False):
    """
    For a metapath, extracts the node and edge names and returns as a list.

    :param mp: hetnetpy.hetnet.MetaPath or json represntation (see `metapaths_to_json`), the MetaPath to extract.
    :param rev_map: dict, mapping from forward to reverse edge semmantics.
    :param n_abbv: bool, if True, will only return the abberevations for the nodes rather than full names:
    :param n_abbv: bool, if True, will only return the abberevations for the edges rather than full names:

    :return: list of strings, the node and edge names in the metapath, in order of appearance
    """

    edges = extract_mp_edges(mp, rev_map, e_abbv)
    nodes = extract_mp_nodes(mp, n_abbv)

    return nodes_and_edges_to_path(nodes, edges)


def print_path_list(path, lines='multi'):
    """Prints the items in a path, `lines` must be either 'multi' or 'one'"""

    assert lines in ['one', 'multi']

    if lines == 'multi':
        for i, item in enumerate(path[:-1:2]):
            print('({}) - [{}] - ({})'.format(path[i*2], path[(i*2)+1].upper(), path[(i*2)+2]))

    else:
        for i, item in enumerate(path[:-1:2]):
            if i == 0:
                print('({})'.format(path[i*2]), end='')
            print(' - [{}] - ({})'.format(path[(i*2)+1].upper(), path[(i*2)+2]), end='')
        print('')


def print_metapath(mp, rev_map, n_abbv=False, e_abbv=False, lines='multi'):
    """
    For a metapath, prints the path to screen.

    :param mp: hetnetpy.hetnet.MetaPath or json represntation (see `metapaths_to_json`), the MetaPath to extract.
    :param rev_map: dict, mapping from forward to reverse edge semmantics.
    :param n_abbv: bool, if True, will only return the abberevations for the nodes rather than full names:
    :param n_abbv: bool, if True, will only return the abberevations for the edges rather than full names:
    :param lines: string, must be in 'one', 'multi'. Whether to print the path to 1 line, or multiple.
    """
    path_list = metapath_to_list(mp, rev_map, n_abbv, e_abbv)
    print_path_list(path_list, lines)


def is_directed(mp, directed_map):
    """For a metapath, returns which edges are directed"""
    edges = extract_mp_edges(mp)
    return [directed_map[e] for e in edges]


def find_inverted_edges(mp):
    """Find the edges that are inveted within a metapath. Returns as a boolean list"""
    if type(mp) == _MetaPath:
        return [e.inverted for e in mp.edges]
    elif type(mp) == dict and 'edges' in mp:
        return [(abv != sabv) and ('>' not in abv) for abv, sabv in
                zip(mp['edge_abbreviations'], mp['standard_edge_abbreviations'])]
    else:
        raise TypeError


def find_directed_inversion(mp, directed_map):
    """For a metapah, find which edges are both directed and inverted"""
    directed = is_directed(mp, directed_map)
    inverted = find_inverted_edges(mp)

    return [d and i for d, i in zip(directed, inverted)]


def get_direction(mp, dir_map, direction_map, strict=False):
    """
    Gets the direction of influence for a metapath.  If Positive, then results
    in an increase in the final node on the path. If negative, a decrease, and
    if 0, then no change can be determined.
    """

    dir_edges = sum(gt.is_directed(mp, dir_map))
    if ((strict and dir_edges == len(mp)) or (not strict and dir_edges > 0)) and \
       (sum(gt.find_directed_inversion(mp, dir_map)) == 0):
        directions = np.array(gt.is_directed(mp, direction_map))
        return np.product(directions[np.where(directions != 0)])
    else:
        return 0


def find_node_index(mp, node_names):
    """Retruns the indicies of the nodes in a metapath of a given metanode(s)."""
    if type(node_names) == str:
        test_names = [node_names]
    else:
        test_names = node_names

    metanodes = extract_mp_nodes(mp)
    return [i for i, m_node in enumerate(metanodes) if m_node in test_names]


def inv_target(mp, directed_map, target_edges=None):
    """
    Method to reveal metapaths that contain inverted target edges

    Target edges can contain a lot of information in a mode. Inverted target edges can potentitall be
    an indicator of a similarity edge:
    E.G. compound-reduces-Gene-upregulated_in-Phenotype-Treated_by-Gene-down_regulated_in-Disease
    The treated by edge contains a lot of information potnetially making this a Phenotype-Disease
    Similarity edge
    """
    if target_edges is None:
        target_edges = ['treats', 'therapeutic', 'marker_or_mechanism', 'diagnoses', 'palliates', 'prevents']

    dir_inv = find_directed_inversion(mp, directed_map)
    for i, di in enumerate(dir_inv):
        if di and mp.edges[i].kind in target_edges:
            return True
    return False


def is_similarity(mp, node_names, directed_map, max_repeats=2, check_dir='fwd', blacklist_edges=None):
    """
    Check to see if this path expresses similarity between two concepts.  Designed and tested
    on concepts that either start or end the path, but may work on mid-path concepts.

    Similarity Examples:
        Compound-BINDS-Gene-BOUND_BY-Compound-TREATS-Disease is a similarity path
        Compound-ACTIVATES-Gene-PRODUCES-Compound-TREATS-Disease is not a similarity path.

    A more through explanation of similarity paths will be provided elsewhere.

    :param mp: hetnetpy.hetnet.MetaPath or json representation of the metapath
    :param node_names: str or list of str, the metanode(s) to be checked repeats/similarity
    :param directed_map: a dictionary of metaedge to directed (as opposed to a membership),
        so 'produces', 'inhibits', and 'treats' should be True, 'part_of', 'capable_of', or
        'associated_with' should be False
    :param max_repeats: int, the maximum number of times metanodes in `node_names` can be repeated
    :param check_dir: str, in 'fwd', 'rev', or 'both'. Some of the similarity checks are directional,
        This tells the algorithm which direction to check
    :param blacklist_edges: list of str. Blacklisted edges don't count for the directed-non-inveted edge requirment.
        target edges for machine learning may express too much information with regard to similarity, therefore may
        not be ideal as the only directed edge linking two concepts.

    :return: bool, True if the path is a similarity path (or is over the max-repeats mark).
    """

    assert check_dir in ['fwd', 'rev', 'both']
    if blacklist_edges is None:
        blacklist_edges = ['treats', 'therapeutic', 'marker_or_mechanism', 'diagnoses', 'palliates', 'prevents']

    # Get the directed edges
    dir_edges = is_directed(mp, directed_map)
    # Get the directed inversions
    dir_inv = find_directed_inversion(mp, directed_map)

    # Compute the edges that are directed but not inverted
    dir_non_inv = [d and not di for d, di in zip(dir_edges, dir_inv)]

    test_idx = find_node_index(mp, node_names)

    # Only one if the test metanode(s) so not similarity (of that metanode) by definition
    if len(test_idx) <= 1:
        return False
    # Too many repeats (may not be similairty, but doesn't pass our treshold)
    elif len(test_idx) > max_repeats:
        return True

    for idx in range(len(test_idx)-1):
        first_idx = test_idx[idx]
        second_idx = test_idx[idx + 1]

        # Make sure there's a non-inveretd directed edge between the two items of interest
        if sum(dir_non_inv[first_idx: second_idx]) == 0:
            return True

        # make sure the second instance of the test object is not preceeded by a Directed Inversion
        if check_dir in ['fwd', 'both'] and dir_inv[second_idx-1]:
            return True

        # make sure the first instance of the test object is not followed by a Directed Inversion
        if check_dir in ['rev', 'both'] and dir_inv[first_idx]:
            return True

        # ensure that there is a non-invertred directed edge is not a TREATS edge:
        is_sim = True
        for i, bool_val in enumerate(dir_non_inv):
            if i < first_idx:
                continue
            elif i >= second_idx:
                break
            if bool_val:
                # at least one needs to not be a blacklisted edge
                if mp.edges[idx].kind not in blacklist_edges:
                    is_sim = False
    return is_sim


def subset_mps_by_node_count(metapaths, max_counts=None, subset=None, default_max=1):
    """Subsets lists of metapaths by number of repeats of a metanode"""
    if max_counts is None:
        max_counts = _defaultdict(lambda:default_max)
    else:
        max_counts = _defaultdict(lambda:default_max, max_counts)

    out = []
    if subset is None:
        subset = metapaths.keys()

    for m in subset:
        # Un-direct the edges...
        no_dir_edges = [e.replace('>', '-').replace('<', '-') for e in metapaths[m]['edges']]
        path_nodes = [no_dir_edges[0].split(' - ')[0]] + [e.split(' - ')[-1] for e in no_dir_edges]
        c = _Counter(path_nodes)

        if all([v <= max_counts[k] for k,v in c.items()]):
            out.append(m)

    return out


