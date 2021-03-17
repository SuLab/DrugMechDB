---
title: "avibactam - Pyelonephritis"
sidebar: mydoc_sidebar
permalink: avibactampyelonephritis.html
toc: false 
---

{% include image.html url="images/avibactampyelonephritis.png" file="avibactampyelonephritis.png" alt="avibactampyelonephritis" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C543519 | avibactam | Drug |
| UniProt:P0A9Z7 | Beta-lactamase SHV-2 | Protein |
| UniProt:P0AD63 | Beta-lactamase SHV-1 | Protein |
| UniProt:P62593 | Beta-lactamase TEM | Protein |
| GO:0008800 | beta-lactamase activity | MolecularActivity |
| NCBITaxon:562 | Escherichia coli | OrganismTaxon |
| MESH:D011704 | Pyelonephritis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Avibactam | NEGATIVELY REGULATES | Beta-Lactamase Shv-2 |
| Avibactam | NEGATIVELY REGULATES | Beta-Lactamase Shv-1 |
| Avibactam | NEGATIVELY REGULATES | Beta-Lactamase Tem |
| Beta-Lactamase Shv-2 | POSITIVELY REGULATES | Beta-Lactamase Activity |
| Beta-Lactamase Shv-1 | POSITIVELY REGULATES | Beta-Lactamase Activity |
| Beta-Lactamase Tem | POSITIVELY REGULATES | Beta-Lactamase Activity |
| Beta-Lactamase Activity | IN TAXON | Escherichia Coli |
| Escherichia Coli | CAUSES | Pyelonephritis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB09060#mechanism-of-action](https://go.drugbank.com/drugs/DB09060#mechanism-of-action){:target="_blank"}