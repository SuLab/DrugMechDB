import json
import shlex
import pandas as pd
from queue import Queue
from collections import defaultdict


def read_lines(filename):
    """Generator to read lines of a file"""
    with open(filename, 'r') as fin:
        for line in fin.readlines():
            yield line


def get_term_keys(obo_file):
    """
    Returns all the keys in terms in the .obo file.

    :param obo_file: The location of the obo file to be examined.
    :return: set, the keys for all terms within the obo file.
    """
    term_keys = set()
    is_term = False

    for line in read_lines(obo_file):
        # Determine if term or a typedef
        if '[Term]' in line:
            is_term = True
            continue
        if line == '\n':
            is_term = False

        if is_term:
            term_keys.add(line.split(':')[0])
    return term_keys


def get_prop_types(obo_file):
    """Determines all the `property_value` types within a .obo file.

    E.G. for the following line:
        property_value: http://purl.obolibrary.org/obo/chebi/inchikey "SBLSYFIUPXRQRY-UHFFFAOYSA-N" xsd:string
    The property_value wouls be http://purl.obolibrary.org/obo/chebi/inchikey

    :param obo_file: the locaiton of the obo file to examine.
    :return: set, with all the property_value predicates.
    """
    props = set()
    for line in read_lines(obo_file):
        if line.startswith('property_value'):
            props.add(parse_prop_val(line)[0])
    return props


def parse_single_value(line, key):
    """When the key is already known, returns the value as parsed from the line"""
    # Remove key from the line
    val = line.lstrip(key+':').strip()
    # Convert boolean text to values
    if val == 'true':
        val = True
    elif val == 'false':
        val = False
    return val


def parse_prop_val(line):
    """
    Parses a property_value line in an ontology. Returns property type and the value

    Examples of lines parsed:
        property_value: http://purl.obolibrary.org/obo/chebi/inchikey "SBLSYFIUPXRQRY-UHFFFAOYSA-N" xsd:string
        property_value: IAO:0000589 "cell part (CARO)" xsd:string
        property_value: IAO:0000412 http://purl.obolibrary.org/obo/caro.owl
    """

    # Shlex is too slow to run on every property_value, so only do as last resort...
    spl = line.split(' ')
    if len(spl) != 4:
        # splits on spaces if not in "quotes like this"
        spl = shlex.split(line)

    prop_type = spl[1]

    # Most property values encapsulated in quotes, but not all:
    try:
        # Removes quotes
        prop_val = eval(spl[2])
    except:
        # Keeps as-is
        prop_val = spl[2]
    return prop_type, prop_val


def get_ontology_nodes(obo_file, prefix=None, props=None):
    """
    Converts an ontology's .obo file into a DataFrame of nodes.

    :param obo_file: Location of the obofile to be read.
    :param prefix: if not none, the prefix for terms to extract as nodes. Terms with a prefix
        not matching this value will be skipped.
    :param props: List, the `property_value` properties to extract for the nodes. See `get_prop_types` to
        get a list of avaliable properties to extract.

    :return: DataFrame with ids, names xrefs, and other relevatent data for terms in an ontology.
    """
    nodes = list()
    is_term = False
    single_value = ['id','def','name', 'is_obsolete', 'creation_date']
    multi_value = ['replaced_by', 'alt_id', 'xref', 'subset']


    for line in read_lines(obo_file):
        # Terms start with specific Flag...
        if '[Term]' in line:
            is_term = True
            term = dict()
            mv_items = defaultdict(list)
            continue
        # Empty lines indicate new terms
        if line == '\n':
            if is_term:
                nodes.append({**{k: '|'.join(v) for k, v in mv_items.items()}, **term})
            is_term = False
            continue

        # Get single values
        key = line.split(':')[0]

        if key in single_value:
            # If we only want one Ontology's worth of terms,
            # ensure that the correct Prefex is on the identifier
            if prefix and key == 'id':
                _id = parse_single_value(line, key)
                if not _id.startswith(prefix):
                    is_term = False
                    continue
                else:
                    term[key] = _id
            else:
                term[key] = parse_single_value(line, key)

        if key in multi_value:
            mv_items[key].append(parse_single_value(line, key))
        if props is not None and key == 'property_value':
            prop_type, prop_val = parse_prop_val(line)
            if prop_type in props:
                term[prop_type] = prop_val

    out = pd.DataFrame(nodes)
    if 'is_obsolete' in out:
        out['is_obsolete'] = out['is_obsolete'].fillna(False)

    if prefix is None:
        out['id_src'] = out['id'].str.split(':', expand=True)[0]

    return out


def parse_edge_line(line):
    """
    Parses lines thats represent an edge in an .obo file. Returns object ID, name(if available) and predicate.
    Currently only supports edges starting with 'is_a:' and 'relationship:'

    Examples of edge test-cases parsed:
      is_a: HP:0001392 ! Abnormality of the liver
      relationship: has_component CHEBI:16412 {cardinality="2"} ! lipopolysaccharide
      relationship: has_part MOD:00160 ! N4-glycosyl-L-asparagine
      relationship: is_conjugate_base_of CHEBI:17883
    """
    line_spl = line.split(' ')

    # Get the targets name
    if '!' in line:
        name = line[line.index('!')+1:].strip()
    else:
        name = float('nan')

    # is_a relationship: 'is_a: tgt_id ! tgt_name'
    if line_spl[0] == 'is_a:':
        target = line_spl[1].strip()
        rel_type = 'is_a'
    else:
        # relationship: 'relationship: rel_type tgt_id {possible_other_junk} ! tgt_name'
        target = line_spl[2].strip()
        rel_type = line_spl[1].strip()

    return {'tgt_id': target, 'rel_type': rel_type, 'tgt_name': name}


def get_ontology_edges(obo_file, prefix=None):
    """
    Produces a DataFrame of s, p, o triples for edges in a .obo file. (Names are also returned)

    :param obo_file", file name of the obofile to be read
    :param prefix: str, ontology prefix. Will only return edges where the subject's prefix matches.
        E.G. prefix='CHEBI:' will not return any edges for Terms starting with 'BFO:'
    :return: DataFrame, cols=['src_id', 'src_name', 'rel_type', 'tgt_id', 'tgt_name']
    """
    edges = list()
    source_info = ['id', 'name']
    edge_lines = ['relationship', 'is_a']
    is_term = False
    # Just get the names for Relationship ontology terms
    is_ro_term = False
    ro_map = dict()

    for line in read_lines(obo_file):
        # Terms start with specific Flag...
        if '[Term]' in line:
            is_term = True
            term_info = dict()
            continue
        # Empty lines indicate new terms
        if line == '\n':
            is_term = False
            is_ro_term = False
            continue

        # Get single values
        key = line.split(':')[0]

        if key in source_info:
            # If we only want one Ontology's worth of terms,
            # ensure that the correct Prefex is on the identifier
            if key == 'id':
                _id = parse_single_value(line, key)
                if _id.startswith('RO:'):
                    is_ro_term = True
                elif prefix and not _id.startswith(prefix):
                    is_term = False
                    continue
                else:
                    term_info['src_'+key] = _id
            elif is_ro_term and key == 'name':
                ro_map[_id] = parse_single_value(line, key).replace(' ', '_')
            else:
                term_info['src_'+key] = parse_single_value(line, key)

        if key in edge_lines and is_term:
            edge_info = parse_edge_line(line)
            edges.append({**term_info, **edge_info})


    out = pd.DataFrame(edges)[['src_id', 'src_name', 'rel_type', 'tgt_id', 'tgt_name']]
    ro_edges = out['rel_type'].str.startswith('RO:')
    ro_edges = ro_edges[ro_edges].index

    out.loc[ro_edges, 'rel_type'] = out.loc[ro_edges, 'rel_type'].map(ro_map)

    # Get the ontology prefix for sources and targets
    out['src_src'] = out['src_id'].str.split(':', expand=True)[0]
    out['tgt_src'] = out['tgt_id'].str.split(':', expand=True)[0]

    return out


def parse_meta(meta):
    if pd.isnull(meta):
        return meta

    out = dict()

    for k, v in meta.items():
        if k in ['subsets', 'comments']:
            out[k] = '|'.join(values.split('#')[-1] for values in v)

        elif k == 'basicPropertyValues':
            for prop_val in v:
                prop = prop_val['pred'].split('#')[-1].split('/')[-1].replace('_', ':')
                val = prop_val['val']
                out[prop] = val

        elif type(v) == dict:
            out[k] = v['val']

        elif type(v) == bool:
            out[k] = v

        else:
            out[k] = '|'.join([values['val'] for values in v])

    return out


def parse_uri(uri):
    return uri.split('/')[-1].replace('_', ':')



def parse_json_nodes(json_nodes):

    json_nodes = pd.DataFrame(json_nodes)

    json_nodes['short_id'] = json_nodes['id'].apply(lambda i: i.split('/')[-1].replace('_', ':'))
    json_nodes['id_src'] = json_nodes['short_id'].str.split(':', expand=True)[0]
    json_nodes['id_src'].unique()

    col_order = [c for c in json_nodes.columns.tolist() if c != 'meta']

    if 'meta' in json_nodes.columns:
        parsed = json_nodes['meta'].apply(parse_meta).dropna()
        meta = pd.DataFrame(parsed.tolist(), parsed.index)
        # put the more inmportant columns first
        col_order += [c for c in ['xrefs', 'deprecated', 'date', 'definition', 'subsets', 'synonyms'] if c in meta.columns]
        col_order += [c for c in meta.columns if c not in col_order]

        json_nodes = pd.merge(json_nodes, meta, how='outer', left_index=True, right_index=True).drop('meta', axis=1)

    return json_nodes[col_order]


def parse_json_edges(json_edges, json_nodes):
    json_edges = pd.DataFrame(json_edges)
    rel_types = json_edges['pred'].apply(lambda s: s.split('/')[-1]).apply(lambda s: s.split('_')[0]).unique()
    rel_map = json_nodes.query('id_src in @rel_types').set_index('short_id')['lbl'].str.replace(' ', '_').to_dict()

    # some relations contain a # (e.g. doid#shorter_than)
    # Get the part after the #
    try:
        json_edges['rel_type'] = json_edges['pred'].str.split('#', expand=True)[1].dropna()
    except:
        # Sometimes there is no #, so just fill with placeholder NA
        json_edges['rel_type'] = float('nan')

    # Some preds are URIs... We just want the last bit so we can map to a name
    try:
        rels = json_edges['pred'].str.split('/', expand=True)[4].str.replace('_', ':').map(rel_map)
    except:
        # Sometimes no URIs so fill with placeholder NA
        rels = float('nan')

    json_edges['rel_type'] = json_edges['rel_type'].fillna(rels)

    json_edges['rel_type'] = json_edges['rel_type'].fillna(json_edges['pred'])
    id_to_name = json_nodes.set_index('short_id')['lbl'].to_dict()

    json_edges['src_id'] = json_edges['sub'].apply(parse_uri)
    json_edges['src_src'] = json_edges['src_id'].str.split(':', expand=True)[0]
    json_edges['src_name'] = json_edges['src_id'].map(id_to_name)
    json_edges['tgt_id'] = json_edges['obj'].apply(parse_uri)
    json_edges['tgt_src'] = json_edges['tgt_id'].str.split(':', expand=True)[0]
    json_edges['tgt_name'] = json_edges['tgt_id'].map(id_to_name)
    return json_edges


def parse_json_graph(json_graph):
    """
    Parse an ontology's json "graph" into separate nodes and edges DataFrames.

    Tested on GO.json and DOID.json
    """
    json_nodes = json_graph['nodes']
    json_edges = json_graph['edges']

    json_nodes = parse_json_nodes(json_nodes)
    json_edges = parse_json_edges(json_edges, json_nodes)

    json_nodes = json_nodes.drop('id', axis=1).rename(columns={'short_id': 'id', 'lbl': 'name'})
    json_edges = json_edges.drop(['obj', 'pred', 'sub'], axis=1)

    return json_nodes, json_edges


def get_go_nodes_and_edges(go_json_file):
    go = json.load(open(go_json_file, 'r'))
    go = go['graphs'][0]

    go_nodes = go['nodes']
    go_edges = go['edges']

    go_nodes = pd.DataFrame(go_nodes)
    go_edges = pd.DataFrame(go_edges)

    go_nodes['short_id'] = go_nodes['id'].apply(lambda i: i.split('/')[-1].replace('_', ':'))
    go_nodes['id_src'] = go_nodes['short_id'].str.split(':', expand=True)[0]
    go_nodes['id_src'].unique()

    parsed = go_nodes['meta'].apply(parse_meta).dropna()
    meta = pd.DataFrame(parsed.tolist(), parsed.index)

    col_order = go_nodes.columns.tolist() + \
                ['xrefs', 'deprecated', 'date', 'definition', 'subsets', 'synonyms']
    col_order += [c for c in meta.columns if c not in col_order]

    go_nodes = pd.merge(go_nodes, meta, how='outer', left_index=True, right_index=True)[col_order].drop('meta', axis=1)

    rel_types = ['BFO', 'BSPO', 'GOREL', 'RO']
    rel_map = go_nodes.query('id_src == @rel_types').set_index('short_id')['lbl'].str.replace(' ', '_').to_dict()

    go_edges['rel_type'] = go_edges['pred'].str.split('#', expand=True)[1].dropna()

    rels = go_edges['pred'].str.split('/', expand=True)[4].str.replace('_', ':').map(rel_map)
    go_edges['rel_type'] = go_edges['rel_type'].fillna(rels)

    go_edges['rel_type'] = go_edges['rel_type'].fillna(go_edges['pred'])
    id_to_name = go_nodes.set_index('short_id')['lbl'].to_dict()

    go_edges['src_id'] = go_edges['sub'].apply(parse_uri)
    go_edges['src_src'] = go_edges['src_id'].str.split(':', expand=True)[0]
    go_edges['src_name'] = go_edges['src_id'].map(id_to_name)
    go_edges['tgt_id'] = go_edges['obj'].apply(parse_uri)
    go_edges['tgt_src'] = go_edges['tgt_id'].str.split(':', expand=True)[0]
    go_edges['tgt_name'] = go_edges['tgt_id'].map(id_to_name)

    go_nodes = go_nodes.drop('id', axis=1).rename(columns={'short_id': 'id', 'lbl': 'name'})
    go_edges = go_edges.drop(['obj', 'pred', 'sub'], axis=1)

    return go_nodes, go_edges


def get_lineage(edges, nid, c2p_rel='is_a', rel_col='rel_type', c_col='src_id', p_col='tgt_id'):
    """
    Get the ancestors of a node in an ontology. Include the node itself in the result.

    :param edges: DataFrame, edges in the ontology. See `get_ontology_edges` method.
    :param nid: str, the identifier for the node to get ancestors of.
    :param direct_only: bool, if `True` returns only direct children of the given node.
    :param c2p_rel: str, the name for the relation that links a parent to a child.
        if only Child to Parent edges, reverse the c_col and p_col variables...
    :param rel_col: str, the name of the DataFrame column that contains the relationship types (predicates)
    :param c_col: str, the name of the DataFrame column that contains Children in the relationship
    :param p_col: str, the name of the DataFrame column that contains PARENTS in the relationship

    :return: set, all parents, and parents of parents up to the root node.
    """
    # Set initial Conditions
    prev_ancestors = 0
    ancestors = {nid}

    # Reduce the amount of items being queried...
    sub_q = edges.query('{} == @c2p_rel'.format(rel_col))

    # Only when no new elements added kick out of loop
    while len(ancestors) != prev_ancestors:
        # Store the preious amount for end condition check.
        prev_ancestors = len(ancestors)

        # Query for all parents of current ancestors...
        ancestors.update(sub_q.query('{} in @ancestors'.format(c_col))[p_col].unique())

    return ancestors


def get_children(edges, nid, only_direct=False, c2p_rel='is_a', rel_col='rel_type', c_col='src_id', p_col='tgt_id'):
    """
    Get the decendents of a node in an ontology.

    :param edges: DataFrame, edges in the ontology. See `get_ontology_edges` method.
    :param nid: str, the identifier for the node to get children of.
    :param direct_only: bool, if `True` returns only direct children of the given node.
    :param c2p_rel: str, the name for the relation that links a parent to a child.
        if only Child to Parent edges, reverse the c_col and p_col variables...
    :param rel_col: str, the name of the DataFrame column that contains the relationship types (predicates)
    :param c_col: str, the name of the DataFrame column that contains Children in the relationship
    :param p_col: str, the name of the DataFrame column that contains PARENTS in the relationship

    :return: set, all children of the given node, down to leaf nodes.
    """
    # Set initial Conditions
    prev_children = 0
    children = {nid}

    # Reduce the amount of items being queried...
    sub_q = edges.query('{} == @c2p_rel'.format(rel_col))

    # Only get the direct decendents
    if only_direct:
        return set(sub_q.query('{} in @children'.format(p_col))[c_col].unique())

    # Only when no new elements added kick out of loop
    while len(children) != prev_children:
        # Store the preious amount for end condition check.
        prev_children = len(children)

        # Query for all children of current children...
        children.update(sub_q.query('{} in @children'.format(p_col))[c_col].unique())

    # A node is not a child of itself...
    children.remove(nid)
    return children


def get_relation_map(edges, relation, c2p_rel='is_a', rel_col='rel_type', c_col='src_id', p_col='tgt_id'):
    """
    Make a dictionary from a given node in ontology to either the root or leaves.

    :param edges: DataFrame, edges in the ontology. See `get_ontology_edges` method.
    :param relation: str, either `'descendents'` or `'ancestors'`, determines wheather to look up or down the tree.
    :param c2p_rel: str, the name for the relation that links a parent to a child.
        if only Child to Parent edges, reverse the c_col and p_col variables...
    :param rel_col: str, the name of the DataFrame column that contains the relationship types (predicates)
    :param c_col: str, the name of the DataFrame column that contains Children in the relationship
    :param p_col: str, the name of the DataFrame column that contains PARENTS in the relationship

    :return: dict, map from a node to either the root or leaf nodes depending on `relation`.
    """
    # Make sure we're mapping to either ancestors or descendents
    assert relation in ['descendents', 'ancestors']

    if relation == 'descendents':
        # Descendents map from parent to child
        from_col = p_col
        to_col = c_col
    else:
        # Ancestors map from child to parent
        from_col = c_col
        to_col = p_col

    # Initialize variables and reduce search space
    adj_map = defaultdict(set)
    q = Queue()
    sub_q = edges.query('{} == @c2p_rel'.format(rel_col))

    # Build the adjecny list
    for row in sub_q.itertuples():
        start = getattr(row, from_col)
        end = getattr(row, to_col)

        adj_map[start].add(end)

    # Perfrom a BFS on the adjcency list to generate the map
    out = defaultdict(set)
    for start, ends in adj_map.items():
        out[start] = ends
        for end in ends:
            q.put(end)

        while not q.empty():
            relative = q.get()
            new = adj_map.get(relative, set()) - out[start]
            for n in new:
                q.put(n)
                out[start].add(n)

    return out


def get_lineage_map(edges, c2p_rel='is_a', rel_col='rel_type', c_col='src_id', p_col='tgt_id'):
    """
    Make a dictionary from a given node in ontology to all parents up to the root node.

    :param edges: DataFrame, edges in the ontology. See `get_ontology_edges` method.
    :param c2p_rel: str, the name for the relation that links a parent to a child.
        if only Child to Parent edges, reverse the c_col and p_col variables...
    :param rel_col: str, the name of the DataFrame column that contains the relationship types (predicates)
    :param c_col: str, the name of the DataFrame column that contains Children in the relationship
    :param p_col: str, the name of the DataFrame column that contains PARENTS in the relationship

    :return: dict, map from a node to all parents all the way up to the root node.
    """
    return get_relation_map(edges, 'ancestors', c2p_rel, rel_col, c_col, p_col)


def get_children_map(edges, c2p_rel='is_a', rel_col='rel_type', c_col='src_id', p_col='tgt_id'):
    """
    Make a dictionary from a given node in ontology to all childern and descendets to a leaf nodes.

    :param edges: DataFrame, edges in the ontology. See `get_ontology_edges` method.
    :param c2p_rel: str, the name for the relation that links a parent to a child.
        if only Child to Parent edges, reverse the c_col and p_col variables...
    :param rel_col: str, the name of the DataFrame column that contains the relationship types (predicates)
    :param c_col: str, the name of the DataFrame column that contains Children in the relationship
    :param p_col: str, the name of the DataFrame column that contains PARENTS in the relationship

    :return: dict, map from a node to all children of that node, continuing to leaf nodes.
    """
    return get_relation_map(edges, 'descendents', c2p_rel, rel_col, c_col, p_col)
