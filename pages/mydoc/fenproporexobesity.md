---
title: "fenproporex - Obesity"
sidebar: mydoc_sidebar
permalink: fenproporexobesity.html
toc: false 
---

{% include image.html url="images/fenproporexobesity.png" file="fenproporexobesity.png" alt="fenproporexobesity" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C026013 | fenproporex | Drug |
| MESH:D000661 | Amphetamine | ChemicalSubstance |
| GO:0004936 | alpha-adrenergic receptor activity | MolecularActivity |
| GO:0004939 | beta-adrenergic receptor activity | MolecularActivity |
| GO:0032100 | appetite stimulation | BiologicalProcess |
| MESH:D009765 | Obesity | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Fenproporex | PRODUCES | Amphetamine |
| Amphetamine | POSITIVELY REGULATES | Alpha-Adrenergic Receptor Activity |
| Amphetamine | POSITIVELY REGULATES | Beta-Adrenergic Receptor Activity |
| Alpha-Adrenergic Receptor Activity | NEGATIVELY REGULATES | Appetite Stimulation |
| Beta-Adrenergic Receptor Activity | NEGATIVELY REGULATES | Appetite Stimulation |
| Appetite Stimulation | POSITIVELY CORRELATED WITH | Obesity |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01550#mechanism-of-action](https://go.drugbank.com/drugs/DB01550#mechanism-of-action){:target="_blank"}