import pytest
import networkx as nx

indications = nx.read_yaml('indication_paths.yaml')


def validate_dict_keys(to_val, req_keys):
    for req_key in req_keys:
        assert req_key in to_val, 'Key {0!r:} not in {1:}'.format(req_key, to_val.keys())

def validate_node(nodes, identifier):
    node_ids = [node['id'] for node in nodes]
    assert identifier in node_ids, 'ID {0!r:} not in {1:}'.format(identifier, node_ids)

def validate_nodes(nodes, identifiers):
    node_ids = [node['id'] for node in nodes]
    assert len(set(node_ids) | set(identifiers)) > 0, 'ID {0!r:} not in {1:}'.format(identifiers, node_ids)


class PathTester:
    def __init__(self, path):
        self.path = path

    def get_drugs(self):
        return [self.path['graph']['drug_mesh'], self.path['graph']['drugbank']]

    ### Ensure all required Keys are present
    def test_path_keys(self):
        validate_dict_keys(self.path, ['directed', 'graph', 'links', 'multigraph', 'nodes'])

    def test_graph_keys(self):
        validate_dict_keys(self.path['graph'], ['drug', 'disease', 'drugbank', 'drug_mesh', 'disease_mesh'])

    def test_node_keys(self):
        for node in self.path['nodes']:
            validate_dict_keys(node, ['id', 'name', 'label'])

    def test_link_keys(self):
        for link in self.path['links']:
            validate_dict_keys(link, ['source', 'target', 'key'])

    ### Ensure consistency between nodes and links
    def test_drug_in_nodes(self):
        validate_nodes(self.path['nodes'], self.get_drugs())

    def test_disease_in_nodes(self):
        validate_node(self.path['nodes'], self.path['graph']['disease_mesh'])

    def test_links_in_nodes(self):
        for link in self.path['links']:
            validate_node(self.path['nodes'], link['source'])
            validate_node(self.path['nodes'], link['target'])

    def test_nodes_in_links(self):
        sources = [link['source'] for link in self.path['links']]
        targets = [link['target'] for link in self.path['links']]

        link_ids = set(sources) | set(targets)

        for node in self.path['nodes']:
            assert node['id'] in link_ids, 'Node {0!r:} not in {1:}'.format(node['id'], link_ids)

    ### Ensure path consistency
    def test_start_end_drug_disease(self):
        drugs = self.get_drugs()
        disease = self.path['graph']['disease_mesh']

        assert self.path['links'][0]['source'] in drugs
        assert self.path['links'][-1]['target'] == disease

    def test_all_links_connected(self):
        drugs = self.get_drugs()
        disease = self.path['graph']['disease_mesh']

        sources = [link['source'] for link in self.path['links'] if link['source'] not in drugs]
        targets = [link['target'] for link in self.path['links'] if link['target'] != disease]

        leaves = set(sources).symmetric_difference(set(targets))

        assert len(leaves) == 0, 'Internal node(s) {0!r:} are leaf nodes (missing as a source or target)'.format(leaves)

    def run_tests(self):

        ### Ensure all required Keys are present
        self.test_path_keys()
        self.test_graph_keys()
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


@pytest.mark.parametrize('path', indications)
def test_paths(path):
    test_path = PathTester(path)
    test_path.run_tests()
