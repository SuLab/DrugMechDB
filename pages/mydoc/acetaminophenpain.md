---
title: "acetaminophen - Pain"
sidebar: mydoc_sidebar
permalink: acetaminophenpain.html
toc: false 
---

{% include image.html url="acetaminophenpain.png" file="acetaminophenpain.png" alt="acetaminophenpain" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D000082 | acetaminophen | Drug |
| UniProt:P23219 | Cox-1 | Protein |
| UniProt:P35354 | Cox-2 | Protein |
| REACT:R-HSA-2162123 | cycloxygenaze pathways | Pathway |
| MESH:D011453 | Prostaglandins | ChemicalSubstance |
| MESH:D010146 | Pain | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Acetaminophen | DECREASES ACTIVITY OF | Cox-1 |
| Acetaminophen | DECREASES ACTIVITY OF | Cox-2 |
| Acetaminophen | NEGATIVELY REGULATES | Cycloxygenaze Pathways |
| Cox-1 | INCREASES ABUNDANCE OF | Prostaglandins |
| Cox-2 | INCREASES ABUNDANCE OF | Prostaglandins |
| Cycloxygenaze Pathways | AFFECTS RISK FOR | Pain |
| Prostaglandins | CAUSES | Pain |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00316#mechanism-of-action](https://go.drugbank.com/drugs/DB00316#mechanism-of-action){:target="_blank"}