---
title: "Quinine - Falciparum malaria"
sidebar: mydoc_sidebar
permalink: quininefalciparummalaria2.html
toc: false 
---

{% include image.html file="quininefalciparummalaria2.png" alt="quininefalciparummalaria2" %}![Path Visualization](/images/quininefalciparummalaria2.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D011803 | Quinine | Drug |
| GO:0071897 | DNA synthesis | BiologicalProcess |
| GO:0006351 | RNA synthesis | BiologicalProcess |
| GO:0006412 | protein synthesis | BiologicalProcess |
| REACT:R-HSA-70171 | glycolysis | Pathway |
| GO:0008219 | cell death | BiologicalProcess |
| NCBITaxon:5833 | Plasmodium falciparum | OrganismTaxon |
| MESH:D016778 | Falciparum malaria | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Quinine | NEGATIVELY REGULATES | Dna Synthesis |
| Dna Synthesis | NEGATIVELY REGULATES | Cell Death |
| Quinine | NEGATIVELY REGULATES | Rna Synthesis |
| Rna Synthesis | NEGATIVELY REGULATES | Cell Death |
| Quinine | NEGATIVELY REGULATES | Protein Synthesis |
| Protein Synthesis | NEGATIVELY REGULATES | Cell Death |
| Quinine | NEGATIVELY REGULATES | Glycolysis |
| Glycolysis | ENABLES | Cell Death |
| Cell Death | IN TAXON | Plasmodium Falciparum |
| Plasmodium Falciparum | CAUSES | Falciparum Malaria |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB00468#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB00468#mechanism-of-action){:target="_blank"}