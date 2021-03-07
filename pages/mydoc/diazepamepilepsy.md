---
title: "diazepam - Epilepsy"
sidebar: mydoc_sidebar
permalink: diazepamepilepsy.html
toc: false 
---

{% include image.html file="diazepamepilepsy.png" alt="diazepamepilepsy" %}![Path Visualization](/images/diazepamepilepsy.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D003975 | Diazepam | Drug |
| GO:0016917 | GABA receptor activity | MolecularActivity |
| GO:0022851 | GABA-gated chloride ion channel activity | BiologicalProcess |
| GO:0019228 | Neuronal action potential | BiologicalProcess |
| GO:0061535 | Glutamate secretion, neurotransmission | BiologicalProcess |
| MESH:D004827 | Epilepsy | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Diazepam | POSITIVELY REGULATES | Gaba Receptor Activity |
| Gaba Receptor Activity | POSITIVELY REGULATES | Gaba-Gated Chloride Ion Channel Activity |
| Gaba-Gated Chloride Ion Channel Activity | NEGATIVELY REGULATES | Neuronal Action Potential |
| Neuronal Action Potential | POSITIVELY REGULATES | Glutamate Secretion, Neurotransmission |
| Glutamate Secretion, Neurotransmission | POSITIVELY CORRELATED WITH | Epilepsy |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB00829#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB00829#mechanism-of-action){:target="_blank"}