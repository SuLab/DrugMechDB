import sys
import string
import simplejson
import pandas as pd
import networkx as nx
from itertools import chain
from yaml.scanner import ScannerError
from collections import defaultdict, Counter

# Multiple imports depending on if command line or import from script
try:
    from pathtester import PathTester, ALLOWED_CURIS, BL_NODES, BL_PREDS
except ModuleNotFoundError:
    from utils.pathtester import PathTester, ALLOWED_CURIS, BL_NODES, BL_PREDS

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
        nodes_out = []
        for j, node in enumerate(path['nodes']):
            fixed_node = fix_node_val_swaps(node)
            # Check for duplications
            if fixed_node not in nodes_out:
                nodes_out.append(fixed_node)

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


def build_base_id(path):
    drugbank = path['graph']['drugbank']
    c_mesh = path['graph']['drug_mesh']
    d_mesh = path['graph']['disease_mesh']

    base_id = ''

    if not pd.isnull(drugbank):
        assert ',' not in drugbank, 'Multiple Identifers not allowed in Drugbank ID'
        base_id += drugbank.split(':')[-1]
        base_id += '_'

    else:
        assert ',' not in c_mesh, 'Mutiple Identfier not allowed in MESH ID when Drugbank ID is missing'
        base_id += c_mesh.replace(':', '_')
        base_id += '_'

    assert not pd.isnull(d_mesh), 'Disease Identifier is missing'
    assert ',' not in d_mesh, 'Multiple Disease Identifiers are not allowed'

    base_id += d_mesh.replace(':', '_')
    return base_id


def get_id_num(path_id):
    return int(path_id.split('_')[-1])


def get_base_id(path_id):
    return '_'.join(path_id.split('_')[:-1])

def read_deprecated_ids():
    try:
        dep_ids = pd.read_csv('utils/deprecated_ids.txt', header=None)[0].tolist()
    except pd.errors.EmptyDataError:
        dep_ids = []
    return dep_ids

def filter_deprecated_ids(indications):
    dep_ids = read_deprecated_ids()
    return [ind for ind in indications if ind['graph']['_id'] not in dep_ids]

def get_max_ids(indications):
    # need to keep track of deprecated identifiers so nothing is repeated
    dep_ids = read_deprecated_ids()
    max_id = defaultdict(int)

    path_ids = [p['graph'].get('_id', None) for p in indications]

    for path_id in path_ids+dep_ids:
        if path_id is not None:
            id_num = get_id_num(path_id)
            base_id = get_base_id(path_id)

            if id_num > max_id[base_id]:
                max_id[base_id] = id_num

    return max_id


def create_ids(indications):

    max_id = get_max_ids(indications)

    for path in indications:
        if path['graph'].get('_id', None) is None:
            base_id = build_base_id(path)
            max_id[base_id] += 1
            path['graph']['_id'] = base_id + '_{}'.format(max_id[base_id])
    return indications


def is_same_path(path_a, path_b):
    """Compares everything except the _id field. If the same, returns True, otherwise False"""
    for k, v in path_a.items():
        if k == 'graph':
            for k1, v1 in v.items():
                if k1 == '_id':
                    pass
                elif v1 != path_b[k].get(k1):
                    return False
        elif v != path_b.get(k):
            return False
    return True

def is_path_in_paths(path, paths):
    """Checks to see if the current path is in the list of paths, ignoring identifiers"""
    for p in paths:
        if is_same_path(p, path):
            return True
    return False


def references_to_list(path):
    ref = path.get('reference', None)

    if type(ref) == str:
        return [r for r in ref.split(' ') if r != '']
    if type(ref) == list:
        return [r for r in ref if r != '']
    return ref


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

    # Ensure that we have a list for all references
    for path in indications:
        if path.get('reference'):
            path['reference'] = references_to_list(path)

    if errors:
        print('Build Unsuccessful')
        print('There were {} paths that produced errors'.format(len(errors)))
        print('Please see error messages below\n')
        for error in errors:
            print(error,end='\n\n')
        sys.exit(400)
    else:
        print('Successful Submission Validation')
        return indications


def add_new_submission(submission, outname='indication_paths.yaml'):

    if submission is not None:
        print('Building Indications...')

        indications = nx.read_yaml('indication_paths.yaml')
        out = []

        # Ensure nothing is duplicated
        for path in indications + submission:

            # Ensure that we have a list for all references
            if path.get('reference'):
                path['reference'] = references_to_list(path)

            if not is_path_in_paths(path, out):
                out.append(path)

        out = create_ids(out)
        out = filter_deprecated_ids(out)
        nx.write_yaml(out, outname, indent=4)
        print('Build Successful')
    else:
        sys.exit(125)


def validate_path_id(_id, record):
    base_id = build_base_id(record)
    # base_id of DB00257_MESH_D000152_1 is DB00257_MESH_D000152
    assert base_id == '_'.join(_id.split('_')[:-1]), "Identifier {0!r:} is not valid for path '{1:} - {2:}'".format(
                                                     _id, record['graph']['drug'], record['graph']['disease'])


def update_existing_records(submission, outname='indication_paths.yaml'):

    if submission is not None:
        print('Updating Indications...')

        indications = nx.read_yaml('indication_paths.yaml')

        current_ids = [ind['graph']['_id'] for ind in indications]
        submission_prepped = {rec['graph']['_id']: rec for rec in submission}

        # Make sure new recrods have unique IDs
        if len(submission_prepped) != len(submission):
            submitted_id_counts = Counter([rec['graph']['_id'] for rec in submission])
            duplicated = [k for k, v in submitted_id_counts.items() if v > 1]
            print('Error, the folling identifiers were used for multiple paths:\n{}'.format(', '.join(duplicated)))
            sys.exit(400)


        # Make sure the Updated records exist
        diff = set(submission_prepped.keys()) - set(current_ids)
        if diff:
            print("Error, the following path id's submitted for update do not exist:\n{}".format(', '.join(diff)))
            sys.exit(400)

        out = []
        errors = []
        for ind in indications:
            _id = ind['graph']['_id']

            if _id in submission_prepped.keys():
                # Previous checks will have ensured that the `graph` data matches the `nodes` and `links` data
                # To ensure that we're updating the right path we can simply check that the identifier
                # is correct for the info found in `graph`
                try:
                    validate_path_id(_id, submission_prepped[_id])
                    out.append(submission_prepped[_id])
                except AssertionError as ae:
                    errors.append(ae)
            else:
                out.append(ind)

        if errors:
            print('Update Unsuccessful')
            print('There were {} paths that produced errors'.format(len(errors)))
            print('Please see error messages below\n')
            for error in errors:
                print(error,end='\n\n')
            sys.exit(400)
        else:
            out = filter_deprecated_ids(out)
            print('Update Successful')
            nx.write_yaml(out, outname, indent=4)


def main(inname='submission.yaml'):
    try:
        submission = nx.read_yaml(inname)
    except ScannerError as se:
        print('Unable to read file: {} Please ensure file has properly formatted YAML.'.format(inname))
        print(se)
        sys.exit(125)

    # No submission, case of an update to deprecated IDs
    if submission is None:
        indications = nx.read_yaml('indication_paths.yaml')
        indications = filter_deprecated_ids(indications)
        nx.write_yaml(indications, 'indication_paths.yaml', indent=4)
        print('Paths writen successfully with deprecated IDs removed')
        sys.exit(0)

    # Prep the submission fixing simple common errors and throwing excptions when not simple fixes
    submission = test_and_fix(submission)

    # Determine if Update or new submission
    has_identifier = ['_id' in rec['graph'].keys() for rec in submission]
    if all(has_identifier):

        update_existing_records(submission)
    elif any(has_identifier):
        print('Mixed submissions and updates are not allowed. Please ensure that either all records ' +\
              'contain an `_id` feild in the `graph` feild if updating, or none contain the `_id` ' +\
              'field if submitting new records')
        sys.exit(400)

    else:
        add_new_submission(submission)

if __name__ == '__main__':
    main()
