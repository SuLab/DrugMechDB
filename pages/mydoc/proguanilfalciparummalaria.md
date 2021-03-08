---
title: "Proguanil - Falciparum malaria"
sidebar: mydoc_sidebar
permalink: proguanilfalciparummalaria.html
toc: false 
---

{% include image.html url="images/proguanilfalciparummalaria.png" file="proguanilfalciparummalaria.png" alt="proguanilfalciparummalaria" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D002727 | Proguanil | Drug |
| MESH:C026009 | Cycloguanil | Drug |
| UniProt:P13922 | Bifunctional dihydrofolate reductase-thymidylate synthase | Protein |
| REACT:R-HSA-8956320 | purines and pyrimidines | Pathway |
| GO:0071897 | DNA synthesis | BiologicalProcess |
| NCBITaxon:5833 | Plasmodium falciparum | OrganismTaxon |
| MESH:D016778 | Falciparum malaria | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Proguanil | HAS METABOLITE | Cycloguanil |
| Cycloguanil | DECREASES ACTIVITY OF | Bifunctional Dihydrofolate Reductase-Thymidylate Synthase |
| Bifunctional Dihydrofolate Reductase-Thymidylate Synthase | DECREASES SYNTHESIS OF | Purines And Pyrimidines |
| Purines And Pyrimidines | DISRUPTS | Dna Synthesis |
| Dna Synthesis | IN TAXON | Plasmodium Falciparum |
| Plasmodium Falciparum | CAUSES | Falciparum Malaria |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01131#mechanism-of-action](https://go.drugbank.com/drugs/DB01131#mechanism-of-action){:target="_blank"}