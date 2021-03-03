import sys
import string
import simplejson
import pandas as pd
import networkx as nx
from itertools import chain
from collections import defaultdict

# Multiple imports depending on if command line or import from script
try:
    from test_indications import PathTester, ALLOWED_CURIS, BL_NODES, BL_PREDS
except ModuleNotFoundError:
    from utils.test_indications import PathTester, ALLOWED_CURIS, BL_NODES, BL_PREDS

# Define some globals for use in this script
bl_map = pd.read_csv('utils/dmdb_to_bl_map.csv')

def normalize_string(text):
    return ''.join([c for c in text.lower() if c not in string.punctuation+' '])

lower_to_final =  {normalize_string(l): l for l in BL_NODES}
norm_curis = {normalize_string(c) for c in ALLOWED_CURIS}
pred_lower_to_final = {normalize_string(t): t for t in BL_PREDS}

# Update to allow for mappting from older Node Types
old_to_bl = {**bl_map.set_index('start_label')['start_bl'].to_dict(),
             **bl_map.set_index('end_label')['end_bl'].to_dict()}
old_to_bl = {normalize_string(k): v for k, v in old_to_bl.items()}
lower_to_final = {**old_to_bl, **lower_to_final}

# Make a map for mapping from older predicates
bl_pred_map = (bl_map[['start_bl', 'end_bl', 'sem_type', 'type_bl']].applymap(normalize_string)
                     .set_index(['start_bl', 'end_bl', 'sem_type'])['type_bl'].to_dict())



def normalize_string(text):
    return ''.join([c for c in text.lower() if c not in string.punctuation+' '])


def convert_all_nodelabels(indications):
    for path in indications:
        for node in path.get('nodes', []):
            label_lower = normalize_string(node['label'])
            node['label'] = lower_to_final[label_lower]


def prep_predicates(indications):
    for path in indications:
        for edge in path['links']:
            key = edge['key'].replace('\xa0', ' ')
            lower_key = normalize_string(key)
            edge['key'] = pred_lower_to_final.get(lower_key, key)



def insert_drugbank_curi(indications):

    drugbank_keys = [('graph', 'drugbank'), ('nodes', 'id'), ('links', 'source'), ('links', 'target')]

    for i, ind in enumerate(indications):
        for key in drugbank_keys:
            outer = ind[key[0]]

            if isinstance(outer, list):
                for j, item in enumerate(outer):
                    identifier = item[key[1]]

                    #### DB003142 becomes DB:DB003142
                    if identifier.startswith('DB') and not identifier.startswith('DB:'):
                        indications[i][key[0]][j][key[1]] = 'DB:' + identifier

            elif isinstance(outer, dict):
                identifier = outer[key[1]]

                # Drugbank can be Nonetype
                if identifier is not None and\
                   identifier.startswith('DB') and \
                   not identifier.startswith('DB:'):

                    indications[i][key[0]][key[1]] = 'DB:' + identifier

            else:
                pass

    return indications


def convert_all_predicates(indications):

    for path in indications:
        id_to_kind = {n['id']: normalize_string(n['label']) for n in path['nodes']}

        for edge in path['links']:
            s_kind = id_to_kind[edge['source']]
            t_kind = id_to_kind[edge['target']]
            key = normalize_string(edge['key'])

            new_key = bl_pred_map.get((s_kind, t_kind, key), key)
            new_key = pred_lower_to_final.get(new_key, edge['key'])

            edge['key'] = new_key


def find_groups(all_items):

    count = defaultdict(list)

    for i, item in enumerate(all_items):
        count[item].append(i)

    return [idx for idx in count.values() if len(idx)>1]


def merge_branching_paths(indications):

    graphs = [(path['graph']['drugbank'], path['graph']['disease_mesh']) for path in indications]
    groups = find_groups(graphs)

    to_group = list(chain(*groups))
    grouped = []
    out_items = []

    for i, indication in enumerate(indications):
        # Add paths with single instance
        if i not in to_group:
            out_items.append(indication)
            continue

        # Skip paths that have already been grouped
        elif i in grouped:
            continue

        # Group paths that need it
        this_group = [g for g in groups if i in g][0]
        grouped.extend(this_group)  # those about to be grouped shouldn't be grouped on future iterations

        to_merge = []
        all_nodes = {}

        # prep the links to merge
        for g in this_group:
            # Group the links
            to_merge.append(indications[g]['links'])
            # Map from id to info for all nodes in the parallel paths
            all_nodes = {**{n['id']: n for n in indications[g]['nodes']}, **all_nodes}

        n_groups = len(this_group)
        to_merge = sorted(to_merge, reverse=True, key=lambda m: len(m))

        out_links = []
        for i, link in enumerate(to_merge[0]):
            # Add new links
            if link not in out_links:
                out_links.append(link)


            # Check parallel paths to ensure link is same
            for j in range(1, n_groups):
                try:
                    parallel_link = to_merge[j][i]
                    # Only add parallel links in not in original (ensures disease at end of path)
                    # In the case that parallel paths are of shorter length
                    if parallel_link not in out_links and parallel_link not in to_merge[0]:
                        out_links.append(parallel_link)
                except IndexError:
                    pass


        out_nodes = []
        for e in out_links:
            this_node = all_nodes[e['source']]
            if this_node not in out_nodes:
                out_nodes.append(this_node)
        else:
            out_nodes.append(all_nodes[e['target']])

        out_path = indications[this_group[0]].copy()
        out_path['links'] = out_links
        out_path['nodes'] = out_nodes

        out_items.append(out_path)

    return out_items

def is_valid_curi(node_id):
    if ':' not in node_id:
        return False
    curi = node_id.split(':')[0]

    return normalize_string(curi) in norm_curis

def validate_node_info(indications):
    for i, path in enumerate(indications):
        for j, node in enumerate(path['nodes']):
            indications[i]['nodes'][j] = fix_node_val_swaps(node)

def fix_node_val_swaps(node):
    """
    Checks a node for common value swaps (e.g. 'name' in ID field and ID in 'name' field)
    Returns unswapped node.
    """

    # See if the node ID is elsewhere...
    if not is_valid_curi(node['id']):

        # Swapped with NAME?
        if normalize_string(node['label']) in lower_to_final.keys() and is_valid_curi(node['name']):
            tmp = node['id']
            node['id'] = node['name']
            node['name'] = tmp
            return node

        # Swapped with LABEL?
        if normalize_string(node['id']) in lower_to_final.keys() and is_valid_curi(node['label']):
            tmp = node['id']
            node['id'] = node['label']
            node['label'] = tmp
            return node

    ## If node ID is ok, but Label is not, test to see if name and label are swapped
    if normalize_string(node['name']) in lower_to_final.keys() and \
       normalize_string(node['label']) not in lower_to_final.keys():
            tmp = node['label']
            node['label'] = node['name']
            node['name'] = tmp
            return node

    return node

def update_curi(old_curi, new_curi, indications):

    for i, path in enumerate(indications):
        for j, n in enumerate(path['nodes']):
            if n['id'].split(':')[0] == old_curi:
                indications[i]['nodes'][j]['id'] = indications[i]['nodes'][j]['id'].replace(old_curi+':', new_curi+':')

                for k, e in enumerate(path['links']):
                    if e['source'].split(':')[0] == old_curi:
                        indications[i]['links'][k]['source'] = indications[i]['links'][k]['source'].replace(old_curi+':', new_curi+':')
                    if e['target'].split(':')[0] == old_curi:
                        indications[i]['links'][k]['target'] = indications[i]['links'][k]['target'].replace(old_curi+':', new_curi+':')

def update_id(old_id, new_id, paths):

    for i, path in enumerate(paths):
        for j, n in enumerate(path['nodes']):
            if n['id'] == old_id:
                paths[i]['nodes'][j]['id'] = new_id

                for k, e in enumerate(path['links']):
                    if e['source'] == old_id:
                        paths[i]['links'][k]['source'] = new_id
                    if e['target'] == old_id:
                        paths[i]['links'][k]['target'] = new_id

def fix_multi_drug(indications):
    for path in indications:

        mesh_drug_id = path['graph']['drug_mesh']
        drugbank_id = path['graph']['drugbank']

        # See if the mesh is a multi-compound drug and make sure drugbank exists
        if mesh_drug_id is not None and ',' in path['graph']['drug_mesh'] and drugbank_id is not None:
            node_ids = [n['id'] for n in path['nodes']]

            # If the path/node uses the multiple MESH ids then set all instances to the drugbank id
            if mesh_drug_id in node_ids:
                new_drug_id = path['graph']['drugbank']
                update_id(mesh_drug_id, drugbank_id, indications)


def fix_id_swap(indications):
    for i, path in enumerate(indications):

        mesh_drug_id = path['graph']['drug_mesh']
        drugbank_id = path['graph']['drugbank']

        # Make sure they're both present
        if mesh_drug_id is not None and drugbank_id is not None:
            # See if they're swapped
            if mesh_drug_id.startswith('DB:') and drugbank_id.startswith('MESH:'):
                indications[i]['graph']['drugbank'] = mesh_drug_id
                indications[i]['graph']['drug_mesh'] = drugbank_id


def update_predicate(old_pred, new_pred, indications):

    for i, path in enumerate(indications):
        for j, link in enumerate(path['links']):
            if link['key'] == old_pred:
                indications[i]['links'][j]['key'] = new_pred

def lower_keys(in_dict):
    if type(in_dict) == list:
        return [lower_keys(i) for i in in_dict]
    elif type(in_dict) != dict:
        return in_dict

    return {k.lower() : lower_keys(v) for k, v in in_dict.items()}


def test_and_fix(indications):

    common_curi_problems = [('Uniprot', 'UniProt')]

    errors = []
    to_remove = []

    # Initial data key sanitization
    indications = [lower_keys(path) for path in indications]

    # Run initial tests for Format
    for i, path in enumerate(indications):
        test_path = PathTester(path)
        try:
            test_path.run_format_tests()
        except AssertionError as ae:
            errors.append(ae)
            to_remove.append(i)
            continue
        except AttributeError as ae1:
            errors.append(ae1)
            to_remove.append(i)
            continue
        except TypeError as te:
            errors.append(te)
            to_remove.append(i)
            continue

    ## Remove problems and Continue
    for index in to_remove[::-1]:
        indications.remove(indications[index])
    to_remove = []

    ## Clean up drugbank IDs
    indications = insert_drugbank_curi(indications)

    # Test Nodes
    for i, path in enumerate(indications):
        test_path = PathTester(path)
        test_path.set_message()

        try:
            test_path.run_identifier_tests()
        except AssertionError as ae:
            ## Seen many cases of 'id' and 'name' swaps...
            for j, node in enumerate(path['nodes']):
                indications[i]['nodes'][j] = fix_node_val_swaps(node)

            path = indications[i]
            test_path = PathTester(path)
            test_path.set_message()
            try:
                test_path.run_identifier_tests()
            except AssertionError as ae1:
                errors.append(ae1)
                to_remove.append(i)

    ## Remove problems and Continue
    for index in to_remove[::-1]:
        indications.remove(indications[index])
    to_remove = []

    ## Run Path Consistency Tests
    for i, path in enumerate(indications):
        test_path = PathTester(path)
        test_path.set_message()
        try:
            test_path.run_consistency_tests()
        except AssertionError as ae:
            errors.append(ae)
            to_remove.append(i)
            continue

    ## Remove problems and Continue
    for index in to_remove[::-1]:
        indications.remove(indications[index])
    to_remove = []

    validate_node_info(indications)
    convert_all_nodelabels(indications)
    prep_predicates(indications)
    convert_all_predicates(indications)
    fix_multi_drug(indications)
    fix_id_swap(indications)

    for bad_curi, good_curi in common_curi_problems:
        update_curi(bad_curi, good_curi, indications)

    ## Run tests for Biolink consistency
    for path in indications:
        test_path = PathTester(path)
        test_path.set_message()
        try:
            test_path.run_data_model_tests()
        except AssertionError as ae:
            errors.append(ae)

    if errors:
        print('Build Unsuccessful')
        print('There were {} paths that produced errors'.format(len(errors)))
        print('Please see error messages below\n')
        for error in errors:
            print(error,end='\n\n')
    else:
       print('Build Successful')
       return indications


def run_tests_fix_and_write(inname='indication_paths.yaml', outname='test_out.yaml'):

    try:
        indications = nx.read_yaml(inname)
    except:
        print('Unable to read file: {} Please ensure file has properly formatted YAML.'.format(inname))
        return

    indications = test_and_fix(indications)
    if indications is not None:
        nx.write_yaml(indications, outname, indent=4)


if __name__ == '__main__':
    run_tests_fix_and_write()

