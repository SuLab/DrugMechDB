---
title: "naproxen - Pain"
sidebar: mydoc_sidebar
permalink: naproxenpain.html
toc: false 
---

{% include image.html file="naproxenpain.png" alt="naproxenpain" %}![Path Visualization](/images/naproxenpain.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D009288 | naproxen | Drug |
| UniProt:P35354 | Cox-2 | Protein |
| MESH:D011453 | Prostaglandins | ChemicalSubstance |
| GO:0006954 | Inflammation | BiologicalProcess |
| MESH:D010146 | Pain | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Naproxen | DECREASES ACTIVITY OF | Cox-2 |
| Cox-2 | INCREASES ABUNDANCE OF | Prostaglandins |
| Prostaglandins | PARTICIPATES IN | Inflammation |
| Inflammation | CAUSES | Pain |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB00788#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB00788#mechanism-of-action){:target="_blank"}