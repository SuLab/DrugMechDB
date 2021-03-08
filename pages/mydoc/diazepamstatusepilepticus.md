---
title: "diazepam - Status epilepticus"
sidebar: mydoc_sidebar
permalink: diazepamstatusepilepticus.html
toc: false 
---

{% include image.html url="images/diazepamstatusepilepticus.png" file="diazepamstatusepilepticus.png" alt="diazepamstatusepilepticus" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D003975 | Diazepam | Drug |
| GO:0016917 | GABA receptor activity | MolecularActivity |
| GO:0022851 | GABA-gated chloride ion channel activity | BiologicalProcess |
| GO:0019228 | Neuronal action potential | BiologicalProcess |
| GO:0061535 | Glutamate secretion, neurotransmission | BiologicalProcess |
| MESH:D013226 | Status epilepticus | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Diazepam | POSITIVELY REGULATES | Gaba Receptor Activity |
| Gaba Receptor Activity | POSITIVELY REGULATES | Gaba-Gated Chloride Ion Channel Activity |
| Gaba-Gated Chloride Ion Channel Activity | NEGATIVELY REGULATES | Neuronal Action Potential |
| Neuronal Action Potential | POSITIVELY REGULATES | Glutamate Secretion, Neurotransmission |
| Glutamate Secretion, Neurotransmission | POSITIVELY CORRELATED WITH | Status Epilepticus |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00829#mechanism-of-action](https://go.drugbank.com/drugs/DB00829#mechanism-of-action){:target="_blank"}