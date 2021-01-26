from itertools import chain
import matplotlib.pyplot as plt
import data_tools.plotting as pt


node_color_map = {'Protein': '#e71761',
                 'Disease': '#70c6ca',
                 'Pathway': '#b1d34f',
                 'PhenotypicFeature': '#154e56',
                 'ChemicalSubstance': '#01c472',
                 'GeneFamily': '#5a3386',
                 'Drug': '#01c472',
                 'GrossAnatomicalStructure': '#8c88d7',
                 'Cell': '#8c88d7',
                 'CellularComponent': '#8c88d7',
                 'BiologicalProcess': '#b75970',
                 'MolecularActivity': '#b75970',
                 'OrganismTaxon': '#e9bf98',
                 'INVALID': '#2e21d0'}


def plot_node_legend():
    """Plots the color legened for the different node types in DrugMechDB"""

    f = lambda m,c: plt.plot([],[],marker=m, color=c, ls="none")[0]

    fig, ax = plt.subplots()

    labels = sorted(list(node_color_map.keys()))
    colors = [node_color_map[l] for l in labels]

    # Put INVALID at end
    idx = labels.index('INVALID')
    labels.append(labels[idx])
    colors.append(colors[idx])
    labels = labels[:idx] + labels[idx+1:]
    colors = colors[:idx] + colors[idx+1:]

    handles = [f("s", c) for c in colors]

    legend = plt.legend(handles, labels, loc=3, framealpha=1, frameon=False, fontsize='x-large')

    for hndl in legend.legendHandles:
        hndl._legmarker.set_markersize(12)

    fig.patch.set_visible(False)
    ax.axis('off')
    fig.canvas.draw()
    bbox  = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    return fig


def plot_path(path):
    """
    Plots a path as series of nodes and edges. Takes `path` variable as json
    formatted DrugMechDB path.
    """
    
    id_to_label = {n['id']: n['label'] for n in path['nodes']}
    id_to_name = {n['id']: n['name'] for n in path['nodes']}

    ids = [path['links'][0]['source']] + [link['target'] for link in path['links']]
    names = [id_to_name[i] for i in ids]
    labels = [id_to_label[i] for i in ids]

    id_to_text = {i: n+'\n'+i+'\n'+l for n, l, i in zip(names, labels, ids)}

    edges = [pt.prep_node_labels(link['key'], 15) for link in path['links']]
    
    nid_to_color = {i: node_color_map.get(id_to_label[i], node_color_map['INVALID']) for i in ids}

    xscale=10 + ((len(edges) - 2) * 2)
    
    this_paths = [[]]
    preds = [[]]

    drug_id = path['graph']['drug_mesh']
    dis_id = path['graph']['disease_mesh']

    for j, link in enumerate(path['links']):
        kind = pt.prep_node_labels(link['key'], 15)
        start = link['source']
        end = link['target']

        # Fist link, initialize things
        if len(this_paths[0]) == 0:
            this_paths[0].append(start)
            this_paths[0].append(end)
            preds[0].append(kind)

            continue

        # Add new edges where needed
        paths_to_add = []
        preds_to_add = []

        for i, p in enumerate(this_paths):
            if p[-1] == start:
                this_paths[i].append(end)
                preds[i].append(kind)

            # This node seen elswhere, need to branch the path
            elif start in p:
                idx = p.index(start)
                new_path = p[:idx+1]
                new_path.append(end)

                new_preds = preds[i][:idx]
                new_preds.append(kind)

                # add as a tuple for de-duplication
                paths_to_add.append(tuple(new_path))
                preds_to_add.append(tuple(new_preds))


        # Deduplicate on extension
        this_paths.extend([list(t) for t in set(paths_to_add)])
        preds.extend([list(t) for t in set(preds_to_add)])

    G = pt.build_explanitory_graph(this_paths, preds, node_id_to_color=nid_to_color)
    fig = pt.draw_explanitory_graph(G, title=False, node_id_to_name=id_to_text, n_paths=2+(3*len(this_paths)),
                              xscale=xscale, node_size=11000)

    return fig