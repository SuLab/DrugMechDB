from datetime import date
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import pandas as pd
from path_plots import dmdb_plots as dp
import re
import shutil
from yaml import safe_load


def generate_md_header(output, title, permalink, datatable=False):
    output.write("---\n")
    output.write("title: \"" + title + "\"\n")
    output.write("sidebar: mydoc_sidebar\n")
    output.write("permalink: " + permalink + ".html\n")
    output.write("toc: false \n")
    if datatable:
        output.write("datatable: true \n")
    output.write("---\n\n")


def generate_home_pages():
    with open("pages/CurationGuide.md", 'w') as output:
        generate_md_header(output, "Curation Guide", "CurationGuide2")
        with open("CurationGuide.md", 'r') as input:
            content = input.readlines()
            content.pop(0)  # title will generate from jekyll
            for line in content:
                output.write(line)
    with open("pages/index.md", 'w') as output:
        generate_md_header(
            output, "Indication Mechanism of Action Database", "index")
        with open("README.md", 'r') as input:
            content = input.readlines()
            content.pop(0)
            for line in content:
                output.write(line)


def restart_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def restart_sidebar():
    restart_file('_data/sidebars/mydoc_sidebar.yml')
    shutil.copyfile('_data/sidebars/copy_sidebar.yml',
                    '_data/sidebars/mydoc_sidebar.yml')


def read_yaml():
    stream = open("indication_paths.yaml", 'r')
    data = safe_load(stream)  # data returned as list of dictionaries
    stream.close()
    return data


def generate_path_pages():
    data = read_yaml()

    # 1. overview table metadata and header
    #restart_file("pages/mydoc/overview.md")
    with open("pages/mydoc/overview.md", "w") as output:
        generate_md_header(output=output, title="Paths Overview",
                           permalink="overview", datatable=True)
        output.write("<div class=\"datatable-begin\"></div>\n\n")
        output.write("|--------|------|-------------|--------------|--------" +
                     "-|-----------------|--------------------|-------------" +
                     "---------|\n")
        output.write("|Path ID | Drug | Drugbank ID | Drug MESH ID | Disease" +
                     " | Disease MESH ID | Number of Concepts | Num of Relat" +
                     "ionships |\n")
        output.write("|--------|------|-------------|--------------|--------" +
                     "-|-----------------|--------------------|-------------" +
                     "---------|\n")

    current_paths = []  # track drug-disease combos to avoid overwriting

    ax = plt.axes([0, 0, 1, 1], frameon=False)  # remove border
    pathid = 1
    drug_sidebar_data = {}
    disease_sidebar_data = {}

    for path in data:
        nodes = []
        edge_lookup = {}

        for node in path["nodes"]:
            nodes.append(node["name"] + "\n" +
                         node["id"] + "\n" + node["label"])
            edge_lookup[node["id"]] = nodes[len(nodes)-1]

        # 2. generate and save plots
        dp.plot_path(path)

        outfile_name = (path["graph"]["drug"] + path["graph"]["disease"])
        outfile_name = re.sub('[\W_]+', '', outfile_name).lower()
        if outfile_name not in current_paths:  # number paths with same drug & dis
            current_paths.append(outfile_name)
        else:
            o_count = len([i for i in current_paths if outfile_name in i])
            outfile_name += str(o_count + 1)
            current_paths.append(outfile_name)

        if os.path.exists("images/" + outfile_name + ".png"):
            os.remove("images/" + outfile_name + ".png")
        plt.savefig("images/" + outfile_name + ".png")

        plt.close(fig=None)
        ax.clear()

        # 3. generate pathway pages
        restart_file("pages/mydoc/" + outfile_name + ".md")

        with open("pages/mydoc/" + outfile_name + ".md", "w") as output:
            path_title = (path["graph"]["drug"] + " - " +
                          path["graph"]["disease"])

            # required header for format
            generate_md_header(
                output=output, title=path_title, permalink=outfile_name)
            
            output.write('{% include image.html url="' + outfile_name + '.png" ' +
                         'file="' + outfile_name + '.png" alt="' +
                         outfile_name + '" %}\n\n')

            output.write("## Concepts\n\n")
            output.write("|------------|------|---------|\n")
            output.write("| Identifier | Name | Type    |\n")
            output.write("|------------|------|---------|\n")
            for node in path['nodes']:
                output.write("| " + node["id"] + " | " + node["name"] + " | "
                             + node["label"] + " |\n")
            output.write("|------------|------|---------|\n")

            output.write("\n## Relationships\n\n")
            output.write("|---------|-----------|---------|\n")
            output.write("| Subject | Predicate | Object  |\n")
            output.write("|---------|-----------|---------|\n")
            for edge in path["links"]:
                output.write("| " + edge_lookup[edge["source"]].split('\n')[0].title() + " | "
                             + edge["key"].upper() + " | "
                             + edge_lookup[edge["target"]].split('\n')[0].title() + " |\n")
            output.write("|---------|-----------|---------|\n")

            if 'comment' in path:  # Display Comment if available
                if path["comment"] is not None:
                    url = path["commnet"]
                    output.write("\nComment: " + Comment + "](" + url +
                                 "){:target=\"_blank\"}")
            
            if 'drugbank' in path["graph"]:  # generate drugbank url if available
                if path["graph"]['drugbank'] is not None:
                    url = ("https://go.drugbank.com/drugs/" +
                           path['graph']['drugbank'].split(':', 1)[1] +
                           "#mechanism-of-action")
                    output.write("\nReference: [" + url + "](" + url +
                                 "){:target=\"_blank\"}")

        # 4. save sidebar info for later generation
        if path["graph"]["drug"] not in drug_sidebar_data:
            drug_sidebar_data[path["graph"]["drug"]] = {
                str(pathid) + " - " + path_title: outfile_name}
        else:
            drug_sidebar_data[path["graph"]["drug"]][str(
                pathid) + " - " + path_title] = outfile_name

        if path["graph"]["disease"] not in disease_sidebar_data:
            disease_sidebar_data[path["graph"]["disease"]] = {
                str(pathid) + " - " + path_title: outfile_name}
        else:
            disease_sidebar_data[path["graph"]["disease"]][str(
                pathid) + " - " + path_title] = outfile_name

        # 5. add entry to jquery table for overview page
        with open("pages/mydoc/overview.md", "a") as output:
            output.write("| [" + str(pathid) + "](" + outfile_name + ".html" + ") | "
                         + path["graph"]["drug"] + " | "
                         + str(path["graph"]["drugbank"]) + " | "
                         + str(path["graph"]["drug_mesh"]) + " | "
                         + path["graph"]["disease"] + " | "
                         + str(path["graph"]["disease_mesh"]) + " | "
                         + str(len(path["nodes"])) + " | "
                         + str(len(path["links"])) + " |\n")
        pathid += 1

    # 6. generate footer for overview table
    with open("pages/mydoc/overview.md", "a") as output:
        output.write("|--------|-----|-------------|--------------|---------" +
                     "|-----------------|--------------------|--------------" +
                     "--------|\n\n")
        output.write("<div class=\"datatable-end\"></div>\n")
    return drug_sidebar_data, disease_sidebar_data


def generate_sidebar(drug_sidebar_data, disease_sidebar_data):
    restart_sidebar()
    with open("_data/sidebars/mydoc_sidebar.yml", 'a') as sidebar:
        sidebar.write("      subfolders:\n")
        for key, value in drug_sidebar_data.items():
            sidebar.write("      - title: " + key + "\n")
            sidebar.write("        output: web\n")
            sidebar.write("        subfolderitems:\n\n")
            for k, v in value.items():
                sidebar.write("        - title: " + k + "\n")
                sidebar.write("          url: /" + v + ".html\n")
                sidebar.write("          output: web\n\n")
        sidebar.write("  - title: Diseases\n")
        sidebar.write("    output: web\n")
        sidebar.write("    folderitems:\n\n")
        sidebar.write("    - title: Paths Overview\n")
        sidebar.write("      url: /overview.html\n")
        sidebar.write("      output: web, pdf\n\n")
        sidebar.write("      subfolders:\n")
        for key, value in disease_sidebar_data.items():
            sidebar.write("      - title: " + key + "\n")
            sidebar.write("        output: web\n")
            sidebar.write("        subfolderitems:\n\n")
            for k, v in value.items():
                sidebar.write("        - title: " + k + "\n")
                sidebar.write("          url: /" + v + ".html\n")
                sidebar.write("          output: web\n\n")


def main():
    generate_home_pages()
    drug_sidebar_data, disease_sidebar_data = generate_path_pages()
    generate_sidebar(drug_sidebar_data, disease_sidebar_data)


main()
