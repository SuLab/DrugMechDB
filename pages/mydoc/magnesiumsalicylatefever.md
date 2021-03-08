---
title: "Magnesium salicylate - Fever"
sidebar: mydoc_sidebar
permalink: magnesiumsalicylatefever.html
toc: false 
---

{% include image.html file="magnesiumsalicylatefever.png" alt="magnesiumsalicylatefever" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C496892 | Magnesium salicylate | Drug |
| UniProt:P23219 | Cox-1 | Protein |
| UniProt:P35354 | Cox-2 | Protein |
| MESH:D011453 | Prostaglandins | ChemicalSubstance |
| GO:0006954 | Inflammatory response | BiologicalProcess |
| MESH:D005334 | Fever | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Magnesium Salicylate | DECREASES ACTIVITY OF | Cox-1 |
| Magnesium Salicylate | DECREASES ACTIVITY OF | Cox-2 |
| Cox-1 | INCREASES ABUNDANCE OF | Prostaglandins |
| Cox-2 | INCREASES ABUNDANCE OF | Prostaglandins |
| Prostaglandins | POSITIVELY REGULATES | Inflammatory Response |
| Inflammatory Response | CAUSES | Fever |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01397#mechanism-of-action](https://go.drugbank.com/drugs/DB01397#mechanism-of-action){:target="_blank"}