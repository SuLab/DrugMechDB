---
title: "cefixime - Pharyngitis"
sidebar: mydoc_sidebar
permalink: cefiximepharyngitis.html
toc: false 
---

{% include image.html url="cefiximepharyngitis.png" file="cefiximepharyngitis.png" alt="cefiximepharyngitis" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D020682 | cefixime | Drug |
| UniProt:P44469 | penicillin-binding protein | Protein |
| GO:0009273 | mucopeptide synthesis | BiologicalProcess |
| UniProt:O30554 | autolysin | Protein |
| GO:0042546 | cell wall synthesis | BiologicalProcess |
| NCBITaxon:1314 | Streptococcus pyogenes | OrganismTaxon |
| MESH:D010612 | Pharyngitis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Cefixime | INCREASES ACTIVITY OF | Penicillin-Binding Protein |
| Penicillin-Binding Protein | NEGATIVELY REGULATES | Mucopeptide Synthesis |
| Mucopeptide Synthesis | POSITIVELY REGULATES | Autolysin |
| Autolysin | PREVENTS | Cell Wall Synthesis |
| Cell Wall Synthesis | IN TAXON | Streptococcus Pyogenes |
| Streptococcus Pyogenes | CAUSES | Pharyngitis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00671#mechanism-of-action](https://go.drugbank.com/drugs/DB00671#mechanism-of-action){:target="_blank"}