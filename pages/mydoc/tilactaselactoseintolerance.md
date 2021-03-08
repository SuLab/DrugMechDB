---
title: "Tilactase - Lactose intolerance"
sidebar: mydoc_sidebar
permalink: tilactaselactoseintolerance.html
toc: false 
---

{% include image.html file="tilactaselactoseintolerance.png" alt="tilactaselactoseintolerance" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| DB:DB13761 | Tilactase | Drug |
| CHEBI:17716 | Lactose | ChemicalSubstance |
| CHEBI:4167 | D-glucopyranose | ChemicalSubstance |
| CHEBI:28061 | α-D-galactose | ChemicalSubstance |
| GO:0050892 | intestinal absorption | BiologicalProcess |
| MESH:D007787 | Lactose intolerance | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Tilactase | INCREASES DEGRADATION OF | Lactose |
| Lactose | HAS METABOLITE | Α-D-Galactose |
| Lactose | HAS METABOLITE | D-Glucopyranose |
| Α-D-Galactose | POSITIVELY CORRELATED WITH | Intestinal Absorption |
| D-Glucopyranose | POSITIVELY CORRELATED WITH | Intestinal Absorption |
| Intestinal Absorption | DISRUPTED BY | Lactose Intolerance |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB13761#mechanism-of-action](https://go.drugbank.com/drugs/DB13761#mechanism-of-action){:target="_blank"}