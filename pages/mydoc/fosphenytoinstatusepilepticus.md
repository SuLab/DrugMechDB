---
title: "Fosphenytoin - Status epilepticus"
sidebar: mydoc_sidebar
permalink: fosphenytoinstatusepilepticus.html
toc: false 
---

{% include image.html url="images/fosphenytoinstatusepilepticus.png" file="fosphenytoinstatusepilepticus.png" alt="fosphenytoinstatusepilepticus" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C043114 | Fosphenytoin | Drug |
| MESH:D010672 | Phenytoin | Drug |
| UniProt:Q14524 | Sodium channel protein type 5 subunit alpha | Protein |
| MESH:D012964 | Sodium | ChemicalSubstance |
| UBERON:0001384 | Primary motor cortex | GrossAnatomicalStructure |
| GO:0099611 | Action potential firing threshold | BiologicalProcess |
| HP:0001250 | Seizure | PhenotypicFeature |
| MESH:D013226 | Status epilepticus | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Fosphenytoin | DERIVES INTO | Phenytoin |
| Phenytoin | DECREASES ACTIVITY OF | Sodium Channel Protein Type 5 Subunit Alpha |
| Sodium Channel Protein Type 5 Subunit Alpha | INCREASES TRANSPORT OF | Sodium |
| Sodium | LOCATED IN | Primary Motor Cortex |
| Primary Motor Cortex | NEGATIVELY REGULATES | Action Potential Firing Threshold |
| Action Potential Firing Threshold | AMELIORATES | Seizure |
| Seizure | CAUSED BY | Status Epilepticus |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01320#mechanism-of-action](https://go.drugbank.com/drugs/DB01320#mechanism-of-action){:target="_blank"}