import pandas as pd
import networkx as nx
from collections import defaultdict
import re
__all__ = ["path_to_tup","path_to_G", "get_all_paths", "get_id_to_type", "get_id_to_name", "get_id_to_name", "add_metaedges",
           "add_meanode_pairs", "get_targets", "get_target_metaedges", "get_metapath_node", "get_metapath_edges"]

def path_to_tup(path):
    return (path['graph']['drugbank'], path['graph']['disease_mesh'])

def path_to_G(path):
    return nx.node_link_graph(path)                                                                                        

def get_all_paths(path):
    source_id = path['links'][0]['source']                                                                              
    target_ids = list(set([l['target'] for l in path['links']]) - set([l['source'] for l in path['links']]))
    G = path_to_G(path)
    this_paths = [list(nx.all_simple_paths(G, source_id, target_id)) for target_id in target_ids]         
    return this_paths

def get_id_to_type(G):
    id_to_type = {}
    for n in G.nodes.data():
        id_to_type[n[0]] = n[1]['label']
    return id_to_type

def get_id_to_name(G):
    id_to_name = {}
    for n in G.nodes.data():
        id_to_name[n[0]] = n[1]['name']
    return id_to_name

def add_metaedges(G):
    id_to_type = get_id_to_type(G)
    for e in G.edges:
        G.edges[e]['metaedge'] = id_to_type[e[0]] + ' - ' + e[2] + ' - ' + id_to_type[e[1]]
    return G

def add_meanode_pairs(G):
    id_to_type = get_id_to_type(G)
    for e in G.edges:
        G.edges[e]['mn_pair'] = id_to_type[e[0]] + ' - ' + id_to_type[e[1]]
    return G

def get_targets(G):
    drug = list(G.edges)[0][0]
    targets = []
    for e in G.edges:
        if e[0] == drug:
            targets.append(e[1])
    return targets

def get_target_metaedges(G):
    drug = list(G.edges)[0][0]
    target_mes = []
    if 'metaedge' not in G.edges[list(G.edges)[0]]:
        G = add_metaedges(G)
    
    for e in G.edges:
        if e[0] == drug:
            target_mes.append(G.edges[e]['metaedge'])
    return target_mes


def get_metapath_node(ind):
    """Lets get metapaths (only include nodes)"""
    all_metapath_nodes = defaultdict(list)
    for i, p in enumerate(ind):
        _id = (p["graph"]["_id"])

        drug_id, dis_id = path_to_tup(p)
        paths = get_all_paths(p)
        G = path_to_G(p)

        G = add_metaedges(G)
        G = add_meanode_pairs(G)

        this_metaedges = [G.edges[e]['metaedge'] for e in G.edges]

        #lets construct a graph for each path
        graph = nx.DiGraph()
        for rel in this_metaedges:
            rel = rel.split(" - ")
            graph.add_edge(rel[0], rel[2], weight =rel[1]) #Add nodes and edges 

        edge_labels = nx.get_edge_attributes(graph,'weight') #Edge labels


        #Extrtact meta-path (nodes)
        try:
            st = 'Drug'  #start node
            end = 'Disease'  #end node
            for mp in nx.all_simple_paths(graph, st, end):
                mp_str = (" - ".join(mp))
                all_metapath_nodes[_id].append(mp_str)
        except:
            continue
        
    return all_metapath_nodes

    
def get_metapath_edges(ind):
    """Lets get metapaths ( include edges)"""    
    all_metapath_edges = defaultdict(list)
    for i, p in enumerate(ind):
        _id = (p["graph"]["_id"])

        drug_id, dis_id = path_to_tup(p)
        paths = get_all_paths(p)
        G = path_to_G(p)

        G = add_metaedges(G)
        G = add_meanode_pairs(G)

        this_metaedges = [G.edges[e]['metaedge'] for e in G.edges]



        #lets construct a graph for path
        graph = nx.DiGraph()
        for rel in this_metaedges:
            rel = rel.split(" - ")
            graph.add_edge(rel[0], rel[2], weight =rel[1]) #Add nodes and edges 

        edge_labels = nx.get_edge_attributes(graph,'weight') #set edge labels


        #get paths (nodes) and #add the edges     
        try:
            st = 'Drug'  #start node
            end = 'Disease'  #end node
            meta_path=[]
            for mp in nx.all_simple_paths(graph, st, end):

                metaedge =[]

                #for value in mp 
                for n in range(len(mp)):
                    if n == (len(mp)-1):
                        continue

                    else:
                         result = (mp[n] + " - " + edge_labels.get((mp[n], (mp[n+1])))+ " - ")
                         metaedge.append(result)

                me = ("".join(metaedge)+ "Disease")
                all_metapath_edges[_id].append(me)

        except:
            continue
    return all_metapath_edges
