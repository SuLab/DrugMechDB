---
title: "diazepam - Tetanus"
sidebar: mydoc_sidebar
permalink: diazepamtetanus.html
toc: false 
---

{% include image.html file="diazepamtetanus.png" alt="diazepamtetanus" %}![Path Visualization](/images/diazepamtetanus.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D003975 | Diazepam | Drug |
| GO:0016917 | GABA receptor activity | MolecularActivity |
| GO:0061534 | Gamma-aminobutyric acid secretion, neurotransmission | BiologicalProcess |
| GO:0090075 | Relaxation of muscle | BiologicalProcess |
| MESH:D009128 | Muscle Spasticity | Disease |
| MESH:D013742 | Tetanus | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Diazepam | POSITIVELY REGULATES | Gaba Receptor Activity |
| Gaba Receptor Activity | POSITIVELY CORRELATED WITH | Gamma-Aminobutyric Acid Secretion, Neurotransmission |
| Gamma-Aminobutyric Acid Secretion, Neurotransmission | POSITIVELY REGULATES | Relaxation Of Muscle |
| Relaxation Of Muscle | NEGATIVELY CORRELATED WITH | Muscle Spasticity |
| Muscle Spasticity | MANIFESTATION OF | Tetanus |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB00829#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB00829#mechanism-of-action){:target="_blank"}