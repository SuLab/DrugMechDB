---
title: "cefixime - Pharyngitis"
sidebar: mydoc_sidebar
permalink: cefiximepharyngitis2.html
toc: false 
---

{% include image.html file="cefiximepharyngitis2.png" alt="cefiximepharyngitis2" %}![Path Visualization](/images/cefiximepharyngitis2.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D020682 | cefixime | Drug |
| UniProt:P44469 | penicillin-binding protein | Protein |
| GO:0005618 | cell wall | CellularComponent |
| NCBITaxon:1314 | Streptococcus pyogenes | OrganismTaxon |
| GO:0009273 | mucopeptide synthesis | BiologicalProcess |
| GO:0042546 | cell wall synthesis | BiologicalProcess |
| UniProt:Q48U47 | autolysin | Protein |
| GO:0008219 | cell death | BiologicalProcess |
| MESH:D010612 | Pharyngitis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Cefixime | MOLECULARLY INTERACTS WITH | Penicillin-Binding Protein |
| Penicillin-Binding Protein | LOCATED IN | Cell Wall |
| Cell Wall | LOCATION OF | Streptococcus Pyogenes |
| Streptococcus Pyogenes | DECREASES ACTIVITY OF | Mucopeptide Synthesis |
| Mucopeptide Synthesis | NEGATIVELY REGULATES | Cell Wall Synthesis |
| Cell Wall Synthesis | INCREASES ACTIVITY OF | Autolysin |
| Autolysin | CONTRIBUTES TO | Cell Death |
| Cell Death | TREATS | Pharyngitis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB00671#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB00671#mechanism-of-action){:target="_blank"}