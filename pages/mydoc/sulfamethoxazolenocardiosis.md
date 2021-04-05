---
title: "Sulfamethoxazole - Nocardiosis"
sidebar: mydoc_sidebar
permalink: sulfamethoxazolenocardiosis.html
toc: false 
---

{% include image.html url="images/sulfamethoxazolenocardiosis.png" file="sulfamethoxazolenocardiosis.png" alt="sulfamethoxazolenocardiosis" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D013420 | Sulfamethoxazole | Drug |
| UniProt:U5EHR3 | Dihydropteroate synthase | Protein |
| MESH:D005492 | Folic acid | ChemicalSubstance |
| GO:0071897 | DNA synthesis | BiologicalProcess |
| NCBITaxon:1824 | Nocardia asteroides | OrganismTaxon |
| MESH:D009617 | Nocardiosis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Sulfamethoxazole | DECREASES ACTIVITY OF | Dihydropteroate Synthase |
| Dihydropteroate Synthase | DECREASES ABUNDANCE OF | Folic Acid |
| Folic Acid | PREVENTS | Dna Synthesis |
| Dna Synthesis | IN TAXON | Nocardia Asteroides |
| Nocardia Asteroides | CAUSES | Nocardiosis |
|---------|-----------|---------|

Comment: Sulfamethoxazole is given in combination with trimethoprim

Reference: [https://go.drugbank.com/drugs/DB01015#mechanism-of-action](https://go.drugbank.com/drugs/DB01015#mechanism-of-action){:target="_blank"}