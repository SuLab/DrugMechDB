---
title: "cefixime - Gonorrhea"
sidebar: mydoc_sidebar
permalink: cefiximegonorrhea.html
toc: false 
---

{% include image.html url="images/cefiximegonorrhea.png" file="cefiximegonorrhea.png" alt="cefiximegonorrhea" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D020682 | cefixime | Drug |
| UniProt:P44469 | penicillin-binding protein | Protein |
| GO:0009273 | mucopeptide synthesis | BiologicalProcess |
| UniProt:O30554 | autolysin | Protein |
| GO:0042546 | cell wall synthesis | BiologicalProcess |
| NCBITaxon:485 | Neisseria gonorrhoeae | OrganismTaxon |
| MESH:D006069 | Gonorrhea | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Cefixime | INCREASES ACTIVITY OF | Penicillin-Binding Protein |
| Penicillin-Binding Protein | NEGATIVELY REGULATES | Mucopeptide Synthesis |
| Mucopeptide Synthesis | POSITIVELY REGULATES | Autolysin |
| Autolysin | PREVENTS | Cell Wall Synthesis |
| Cell Wall Synthesis | IN TAXON | Neisseria Gonorrhoeae |
| Neisseria Gonorrhoeae | CAUSES | Gonorrhea |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00671#mechanism-of-action](https://go.drugbank.com/drugs/DB00671#mechanism-of-action){:target="_blank"}