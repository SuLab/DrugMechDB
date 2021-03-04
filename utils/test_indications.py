import pytest
import networkx as nx

try:
    from pathtester import PathTester
except ModuleNotFoundError:
    from utils.pathtester import PathTester

indications = nx.read_yaml('indication_paths.yaml')

@pytest.mark.parametrize('path', indications)
def test_paths(path):
    test_path = PathTester(path)
    test_path.run_tests(environment='pytest')
