import pytest
import pandas as pd
import networkx as nx

indications = nx.read_yaml('indication_paths.yaml')

ALLOWED_CURIS = {'CHEBI',
 'CL',
 'DB',
 'GO',
 'HP',
 'InterPro',
 'MESH',
 'NCBITaxon',
 'Protein',
 'REACT',
 'TIGR',
 'UBERON',
 'UniProt',
 'UNII'}

bl_map = pd.read_csv('utils/dmdb_to_bl_map.csv')

BL_NODES = bl_map[['start_bl', 'end_bl']].stack().unique().tolist()
BL_PREDS = pd.read_csv('utils/biolink_preds.txt', header=None)[0].str.replace('_', ' ').tolist() +\
           ['regulates', 'positively regulates', 'negatively regulates']

def validate_dict_keys(to_val, req_keys, msg=''):
    for req_key in req_keys:
        assert req_key in to_val, msg+'Key {0!r:} not in {1:}'.format(req_key, to_val.keys())


def validate_node(nodes, identifier, msg=''):
    node_ids = [node['id'] for node in nodes]
    assert identifier in node_ids, msg+'ID {0!r:} not in {1:}'.format(identifier, nodes)


def validate_nodes(nodes, identifiers, msg=''):
    node_ids = [node['id'] for node in nodes]
    assert len(set(node_ids) | set(identifiers)) > 0, msg+'ID {0!r:} not in {1:}'.format(identifiers, node_ids)


class PathTester:
    def __init__(self, path):
        self.path = path
        self.pathname = None
        self.msg = ''

    def get_drugs(self):
        return [self.path['graph']['drug_mesh'], self.path['graph']['drugbank']]

    ### Ensure all required Keys are present
    def test_path_keys(self):
        validate_dict_keys(self.path, ['directed', 'graph', 'links', 'multigraph', 'nodes'])

    def test_graph_keys(self):
        validate_dict_keys(self.path['graph'], ['drug', 'disease', 'drugbank', 'drug_mesh', 'disease_mesh'])

    def test_node_keys(self):
        for node in self.path['nodes']:
            validate_dict_keys(node, ['id', 'name', 'label'], self.msg)

    def test_link_keys(self):
        for link in self.path['links']:
            validate_dict_keys(link, ['source', 'target', 'key'], self.msg)

    ### Ensure consistency between nodes and links
    def test_drug_in_nodes(self):
        validate_nodes(self.path['nodes'], self.get_drugs(), self.msg+'Drug ')

    def test_disease_in_nodes(self):
        validate_node(self.path['nodes'], self.path['graph']['disease_mesh'], self.msg+'Disease ')

    def test_links_in_nodes(self):
        for link in self.path['links']:
            validate_node(self.path['nodes'], link['source'], self.msg+'Source ')
            validate_node(self.path['nodes'], link['target'], self.msg+'Target ')

    def test_nodes_in_links(self):
        sources = [link['source'] for link in self.path['links']]
        targets = [link['target'] for link in self.path['links']]

        link_ids = set(sources) | set(targets)

        for node in self.path['nodes']:
            assert node['id'] in link_ids, self.msg+\
                                           'Node {0!r:} not in link IDs: {1:}'.format(node['id'], link_ids)

    ### Ensure path consistency
    def test_start_end_drug_disease(self):
        drugs = self.get_drugs()
        disease = self.path['graph']['disease_mesh']

        assert self.path['links'][0]['source'] in drugs, self.msg + 'Drug identifiers {0!r:} '.format(drugs) +\
                                                         'not at start of path'
        assert self.path['links'][-1]['target'] == disease, self.msg + 'Disease identifier {0!r:} '.format(disease) +\
                                                            'not at end of path'.format(disease)

    def test_all_links_connected(self):
        drugs = self.get_drugs()
        disease = self.path['graph']['disease_mesh']

        sources = [link['source'] for link in self.path['links'] if link['source'] not in drugs]
        targets = [link['target'] for link in self.path['links'] if link['target'] != disease]

        leaves = set(sources).symmetric_difference(set(targets))

        assert len(leaves) == 0, self.msg+'Internal node(s) {0!r:} are leaf nodes '.format(leaves) +\
                                 '(missing as a source or target)'

    def test_all_curis_present(self):
        for node in self.path['nodes']:
            assert node['id'].count(':') == 1, self.msg+'CURI missing in ID for Node: {0!r:}'.format(node)

    def test_all_curis_allowed(self):
        for node in self.path['nodes']:
            assert node['id'].split(':')[0] in ALLOWED_CURIS, self.msg+'Identifier from unknown ID source ' +\
                                                              'for Node: {0!r:}'.format(node)

    def test_biolink_nodes(self):
        for node in self.path['nodes']:
            assert node['label'] in BL_NODES, self.msg+"Node 'label' is outside of biolink " + \
                                              'model for node: {}'.format(node)

    def test_biolink_predicates(self):
        for link in self.path['links']:
            assert link['key'] in BL_PREDS, self.msg+'Predicate is outside of biolink ' + \
                                            'model for link: {}'.format(link)

    def set_message(self):
        self.pathname = "{0} - {1}".format(self.path['graph']['drug'], self.path['graph']['disease'])
        self.msg = 'For path: {}\n'.format(self.pathname)


    ### Test running logic
    def run_tests(self, environment='standard'):
        ### Ensure all required Keys are present
        self.test_path_keys()
        self.test_graph_keys()

        ### Now that Initial Data Structure is Validated, use to provide more descriptive erros
        self.set_message()
        ### Pytest doesn't like multi-line error mesages
        if environment=='pytest':
            self.msg = self.msg.replace('\n', ', ')

        ### Finish assessment of required keys
        self.test_node_keys()
        self.test_link_keys()

        ### Ensure consistency between nodes and links
        self.test_drug_in_nodes()
        self.test_disease_in_nodes()
        self.test_links_in_nodes()
        self.test_nodes_in_links()

        ### Ensure path consistency
        self.test_start_end_drug_disease()
        self.test_all_links_connected()

        self.run_data_model_tests()

    ### Test running logic
    def run_format_tests(self):
        ### Ensure all required Keys are present
        self.test_path_keys()
        self.test_graph_keys()

        ### Now that Initial Data Structure is Validated, use to provide more descriptive erros
        self.set_message()

        ### Finish assessment of required keys
        self.test_node_keys()
        self.test_link_keys()


    ### Test running logic
    def run_identifier_tests(self):
        ### Ensure consistency between nodes and links
        self.test_links_in_nodes()
        self.test_nodes_in_links()
        self.test_drug_in_nodes()
        self.test_disease_in_nodes()

    def run_consistency_tests(self):
        ### Ensure path consistency
        self.test_start_end_drug_disease()
        self.test_all_links_connected()

    def run_data_model_tests(self):
        self.test_all_curis_present()
        self.test_all_curis_allowed()
        self.test_biolink_nodes()
        self.test_biolink_predicates()

@pytest.mark.parametrize('path', indications)
def test_paths(path):
    test_path = PathTester(path)
    test_path.run_tests(environment='pytest')
