import simplejson
import numpy as np
import pandas as pd
import networkx as nx

from biothings_client import get_client
mg = get_client('gene')

# Change to new DOI if updates to DrugMechDB
DOI = 8139357
# set to metapaths_biolink to use biolink model
metagraph_sheet = 'metapaths'


def read_spreadsheet(location):
    global all_sheets
    global moa_inds
    global moa_paths
    global moa_metapaths
    global moa_ids
    global n_cols
    global e_cols

    all_sheets = pd.read_excel(location, None)

    # Dereference each sheet into an individual variable
    moa_inds = all_sheets['sample_indications'].dropna(how='all')
    moa_paths = all_sheets['paths'].dropna(how='all')
    moa_metapaths = all_sheets[metagraph_sheet].dropna(how='all')
    moa_ids = all_sheets['node_ids'].dropna(how='all')

    n_cols = [c for c in moa_ids.columns if c.startswith('n')]
    e_cols = [c for c in moa_paths.columns if c.startswith('e')]


def uniprot_to_entrez(uniprot):
    """Converts a Uniprot ID to an Entrez Gene ID"""
    if not uniprot.startswith('UniProt:'):
        return uniprot

    try:
        out = mg.query(uniprot.lower(), scopes='entrez')['hits'][0]['entrezgene']
    except:
        out = None

    if not out:
        out = uniprot
    return out


def create_graph(row_numb):
    """Initializes a graph based on the row number in the spreadsheet"""
    c_name = moa_inds.loc[row_numb, 'name']
    d_name = moa_inds.loc[row_numb, 'disease_name']
    db = moa_inds.loc[row_numb, 'db_id']
    c_mesh = moa_inds.loc[row_numb, 'comp_mesh_ids']
    d_mesh = moa_inds.loc[row_numb, 'dis_mesh_id']

    G = nx.MultiDiGraph(drug=c_name, disease=d_name, drugbank=db, drug_mesh=c_mesh, disease_mesh=d_mesh)
    return G


def add_nodes_to_graph(row_numb, G):
    """Adds the nodes from a row number in the spreadsheet to the graph"""
    for col_name in n_cols:
        name = moa_paths.loc[row_numb, col_name]
        kind = moa_metapaths.loc[row_numb, col_name]
        nid = moa_ids.loc[row_numb, col_name]

        if pd.isnull(name):
            break

        if nid not in G.nodes:
            G.add_node(nid, **{'id':nid, 'name':name, 'label':kind})

    return G


def add_edges_to_graph(row_numb, G):
    """Adds the edges from a row number in the spreadsheet to the graph"""
    def j_to_n(j):
        return j//2

    for j in range(0, len(moa_paths.columns) - 2, 2):
        if pd.isnull(moa_paths.iloc[row_numb, j+2]):
            break

        start_id = moa_ids.iloc[row_numb, j_to_n(j)]
        end_id = moa_ids.iloc[row_numb, j_to_n(j+2)]
        edge = moa_metapaths.iloc[row_numb, j+1]

        if not (start_id, end_id, edge) in G.edges:
            G.add_edge(start_id, end_id, key=edge)

    return G

def process_sheet():
    indication_paths = []

    for i in range(len(moa_paths)):
        G = create_graph(i)
        G = add_nodes_to_graph(i, G)
        G = add_edges_to_graph(i, G)

        indication_paths.append(nx.json_graph.node_link_data(G))

    return indication_paths


if __name__ == "__main__":

    # Get the latest iteration of DrugMech DB
    file_location = "https://zenodo.org/record/{}/files/".format(DOI) + \
                    "indication_MOA_paths.xlsx?download=1"

    read_spreadsheet(file_location)
    indication_paths = process_sheet()

    simplejson.dump(indication_paths, open('indication_paths.json', 'w'), indent=2, ignore_nan=True)

