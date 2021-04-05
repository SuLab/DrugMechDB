---
title: "Enviomycin - Pulmonary tuberculosis"
sidebar: mydoc_sidebar
permalink: enviomycinpulmonarytuberculosis.html
toc: false 
---

{% include image.html url="images/enviomycinpulmonarytuberculosis.png" file="enviomycinpulmonarytuberculosis.png" alt="enviomycinpulmonarytuberculosis" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D004776 | Enviomycin | Drug |
| GO:0005840 | Ribosome | CellularComponent |
| GO:0006412 | Translation | BiologicalProcess |
| NCBITaxon:1773 | Mycobacterium tuberculosis | OrganismTaxon |
| MESH:D014397 | Pulmonary tuberculosis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Enviomycin | DECREASES ACTIVITY OF | Ribosome |
| Ribosome | PARTICIPATES IN | Translation |
| Translation | IN TAXON | Mycobacterium Tuberculosis |
| Mycobacterium Tuberculosis | CAUSES | Pulmonary Tuberculosis |
|---------|-----------|---------|

Comment: Enviomycin share the same binding site on the bacterial ribosome and have effects on bacterial cells similar to those of viomycin [https://pubmed.ncbi.nlm.nih.gov/26755601/](https://pubmed.ncbi.nlm.nih.gov/26755601/)

Reference: [https://go.drugbank.com/drugs/DB08993#mechanism-of-action](https://go.drugbank.com/drugs/DB08993#mechanism-of-action){:target="_blank"}