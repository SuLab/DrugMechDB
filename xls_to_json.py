import simplejson
import numpy as np
import pandas as pd
import networkx as nx

from biothings_client import get_client
mg = get_client('gene')

file_location = "https://zenodo.org/record/3515518/files/indication_MOA_paths.xlsx?download=1"
all_sheets = pd.read_excel(file_location, None)

# Dereference each sheet into an individual variable
moa_inds = all_sheets['sample_indications']
moa_paths = all_sheets['paths']
moa_metapaths = all_sheets['metapaths']
moa_ids = all_sheets['node_ids']

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
    c_name = moa_inds.loc[i, 'name']
    d_name = moa_inds.loc[i, 'disease_name']
    db = moa_inds.loc[i, 'db_id']
    c_mesh = moa_inds.loc[i, 'comp_mesh_ids']
    d_mesh = moa_inds.loc[i, 'dis_mesh_id']

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
        edge = moa_paths.iloc[row_numb, j+1]

        if not (start_id, end_id, edge) in G.edges:
            G.add_edge(start_id, end_id, key=edge)

    return G


if __name__ == "__main__":

    n_cols = [c for c in moa_ids.columns if c.startswith('n')]
    e_cols = [c for c in moa_paths.columns if c.startswith('e')]

    indication_paths = []

    for i in range(len(moa_paths)):
        G = create_graph(i)
        G = add_nodes_to_graph(i, G)
        G = add_edges_to_graph(i, G)

        indication_paths.append(nx.json_graph.node_link_data(G))

    simplejson.dump(indication_paths, open('indication_paths.json', 'w'), indent=2, ignore_nan=True)

