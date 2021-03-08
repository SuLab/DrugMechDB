---
title: "cefixime - Bronchitis"
sidebar: mydoc_sidebar
permalink: cefiximebronchitis.html
toc: false 
---

{% include image.html file="cefiximebronchitis.png" alt="cefiximebronchitis" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D020682 | cefixime | Drug |
| UniProt:P44469 | penicillin-binding protein | Protein |
| GO:0009273 | mucopeptide synthesis | BiologicalProcess |
| UniProt:O30554 | autolysin | Protein |
| GO:0042546 | cell wall synthesis | BiologicalProcess |
| NCBITaxon:1313 | Streptococcus pneumoniae | OrganismTaxon |
| MESH:D001991 | Bronchitis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Cefixime | INCREASES ACTIVITY OF | Penicillin-Binding Protein |
| Penicillin-Binding Protein | NEGATIVELY REGULATES | Mucopeptide Synthesis |
| Mucopeptide Synthesis | POSITIVELY REGULATES | Autolysin |
| Autolysin | PREVENTS | Cell Wall Synthesis |
| Cell Wall Synthesis | IN TAXON | Streptococcus Pneumoniae |
| Streptococcus Pneumoniae | CAUSES | Bronchitis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00671#mechanism-of-action](https://go.drugbank.com/drugs/DB00671#mechanism-of-action){:target="_blank"}