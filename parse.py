from datetime import date
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import pandas as pd
import difflib
from path_plots import dmdb_plots as dp
import re
import shutil
from yaml import safe_load
from utils.build_indications import get_id_num, read_deprecated_ids


def generate_md_header(output, title, permalink, datatable=False):
    output.write("---\n")
    output.write("title: \"" + title + "\"\n")
    output.write("sidebar: mydoc_sidebar\n")
    output.write("permalink: " + permalink + ".html\n")
    output.write("toc: false \n")
    if datatable:
        output.write("datatable: true \n")
    output.write("---\n\n")


def generate_out_dirs():
    to_make = ['pages/mydoc',
               'images',
               '_data/sidebars']

    for d in to_make:
        os.makedirs(d, exist_ok=True)

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
    deprecated_ids = read_deprecated_ids()

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

    ax = plt.axes([0, 0, 1, 1], frameon=False)  # remove border
    drug_sidebar_data = {}
    disease_sidebar_data = {}

    for path in data:
        new_path = True
        pathid = path['graph']['_id']
        pathid_num = get_id_num(pathid)
        nodes = []
        edge_lookup = {}

        for node in path["nodes"]:
            nodes.append(node["name"] + "\n" +
                         node["id"] + "\n" + node["label"])
            edge_lookup[node["id"]] = nodes[len(nodes)-1]


        # 2. generate pathway pages
        outfile_name = pathid
        outfile_name = pathid.replace('_', '-').lower()

        # Check for deprecation and delete if true
        if pathid in deprecated_ids:
            # delete the webpage
            if os.path.exists("pages/mydoc/" + outfile_name + ".md"):
                os.remove("pages/mydoc/" + outfile_name + ".md")
            # delete the image
            if os.path.exists("images/" + outfile_name + ".png"):
                os.remove("images/" + outfile_name + ".png")
            # Jump to next iteration
            continue


        # Check to see if the file already exists
        if os.path.exists("pages/mydoc/" + outfile_name + ".md"):
            with open("pages/mydoc/" + outfile_name + ".md", 'r') as in_file:
                old_file = in_file.readlines()
        else:
            old_file = []

        # Generate the new content
        restart_file("pages/mydoc/" + outfile_name + ".md")
        with open("pages/mydoc/" + outfile_name + ".md", "w") as output:
            path_title = (path["graph"]["drug"].title() + " - " +
                          path["graph"]["disease"].title())

            # Add numbers to title if multiple paths fo the indications
            if pathid_num != 1:
                path_title += ' - ' + str(pathid_num)

            # required header for format
            generate_md_header(
                output=output, title=path_title, permalink=outfile_name)

            output.write("\nPath ID: `" + pathid + "`\n")

            output.write('{% include image.html url="images/' + outfile_name + '.png" ' +
                         'file="' + outfile_name + '.png" alt="' +
                         outfile_name + '" %}\n\n')

            output.write("## Concepts\n\n")
            output.write("|------------|------|---------|\n")
            output.write("| Identifier | Name | Type    |\n")
            output.write("|------------|------|---------|\n")
            for node in path['nodes']:
                output.write("| <a href=\"https://identifiers.org/" + node["id"] + "\">" + node["id"] + " </a> | " + node["name"] + " | "
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
                    comment = add_md_hyperlink(path["comment"])
                    output.write("\nComment: " + comment + "\n")

            # Add references from path info if available
            if 'reference' in path:
                ref_out = "\n  - " + "\n  - ".join([add_md_hyperlink(r) for r in path['reference']])
                output.write("\nReference: " + ref_out + "\n")

            elif 'drugbank' in path["graph"]:  # generate drugbank url if no ref present
                if path["graph"]['drugbank'] is not None:
                    url = ("https://go.drugbank.com/drugs/" +
                           path['graph']['drugbank'].split(':', 1)[1] +
                           "#mechanism-of-action")
                    output.write("\nReference:\n  - [" + url + "](" + url +
                                 "){:target=\"_blank\"}")

        # Compare the new content with the old content
        with open("pages/mydoc/" + outfile_name + ".md", 'r') as in_file:
            new_file = in_file.readlines()

        delta = list(difflib.unified_diff(old_file, new_file))
        if delta == []:
            new_file = False

        # 3. generate and save plots

        # Only remake if the files the page is new and/or different
        # or if the image is missing
        if new_file or not os.path.exists("images/" + outfile_name + ".png"):
            print('Building new page: ' + path_title)

            if os.path.exists("images/" + outfile_name + ".png"):
                os.remove("images/" + outfile_name + ".png")

            dp.plot_path(path)
            plt.savefig("images/" + outfile_name + ".png")

            plt.close(fig=None)
            ax.clear()

        # 4. save sidebar info for later generation
        if path["graph"]["drug"].title() not in drug_sidebar_data:
            drug_sidebar_data[path["graph"]["drug"].title()] = {
                path_title: outfile_name}
        else:
            drug_sidebar_data[path["graph"]["drug"].title()][
                path_title] = outfile_name

        if path["graph"]["disease"].title() not in disease_sidebar_data:
            disease_sidebar_data[path["graph"]["disease"].title()] = {
                path_title: outfile_name}
        else:
            disease_sidebar_data[path["graph"]["disease"].title()][
                path_title] = outfile_name

        # 5. add entry to jquery table for overview page
        with open("pages/mydoc/overview.md", "a") as output:
            output.write("| [" + pathid + "](" + outfile_name + ".html" + ") | "
                         + path["graph"]["drug"] + " | "
                         + str(path["graph"]["drugbank"]) + " | "
                         + str(path["graph"]["drug_mesh"]) + " | "
                         + path["graph"]["disease"] + " | "
                         + str(path["graph"]["disease_mesh"]) + " | "
                         + str(len(path["nodes"])) + " | "
                         + str(len(path["links"])) + " |\n")

    # 6. generate footer for overview table
    with open("pages/mydoc/overview.md", "a") as output:
        output.write("|--------|-----|-------------|--------------|---------" +
                     "|-----------------|--------------------|--------------" +
                     "--------|\n\n")
        output.write("<div class=\"datatable-end\"></div>\n")
    return drug_sidebar_data, disease_sidebar_data


def add_md_hyperlink(text):
    # Split across spaces to separate words
    text_split = text.split(' ')
    out_text = []

    # check each word to see if it's a hyperlink
    # (current logic is very basic, just checks for http)
    for word in text_split:
        if word.startswith('http'):
            out_text.append('['+ word +'](' + word + ')')
        else:
            out_text.append(word)
    return ' '.join(out_text)

def generate_sidebar(drug_sidebar_data, disease_sidebar_data):
    restart_sidebar()
    with open("_data/sidebars/mydoc_sidebar.yml", 'a') as sidebar:
        sidebar.write("      subfolders:\n")
        # Sort alpha so easier to find
        sorted_drug_keys = sorted(drug_sidebar_data.keys())
        for key in sorted_drug_keys:
            value = drug_sidebar_data[key]
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
        # Sort Alpha so easy to find
        sorted_disease_keys = sorted(disease_sidebar_data.keys())
        for key in sorted_disease_keys:
            value = disease_sidebar_data[key]
            sidebar.write("      - title: " + key + "\n")
            sidebar.write("        output: web\n")
            sidebar.write("        subfolderitems:\n\n")
            for k, v in value.items():
                sidebar.write("        - title: " + k + "\n")
                sidebar.write("          url: /" + v + ".html\n")
                sidebar.write("          output: web\n\n")


def main():
    generate_out_dirs()
    generate_home_pages()
    drug_sidebar_data, disease_sidebar_data = generate_path_pages()
    generate_sidebar(drug_sidebar_data, disease_sidebar_data)


main()
