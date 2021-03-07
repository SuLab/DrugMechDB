---
title: "oseltamivir - Influenza"
sidebar: mydoc_sidebar
permalink: oseltamivirinfluenza.html
toc: false 
---

{% include image.html file="oseltamivirinfluenza.png" alt="oseltamivirinfluenza" %}![Path Visualization](/images/oseltamivirinfluenza.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| DB:DB00198 | Oseltamivir | Drug |
| UniProt:P11485 | Neuraminidase | Protein |
| GO:0004308 | exo-alpha-sialidase activity | BiologicalProcess |
| GO:0140374 | viral budding from plasma membrane | BiologicalProcess |
| NCBITaxon:380985 | Influenza A virus (A/Chile/1/1983(H1N1)) | OrganismTaxon |
| MESH:D007251 | Influenza | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Oseltamivir | NEGATIVELY REGULATES | Neuraminidase |
| Neuraminidase | POSITIVELY REGULATES | Exo-Alpha-Sialidase Activity |
| Exo-Alpha-Sialidase Activity | POSITIVELY CORRELATED WITH | Viral Budding From Plasma Membrane |
| Viral Budding From Plasma Membrane | IN TAXON | Influenza A Virus (A/Chile/1/1983(H1N1)) |
| Influenza A Virus (A/Chile/1/1983(H1N1)) | CAUSES | Influenza |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB00198#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB00198#mechanism-of-action){:target="_blank"}