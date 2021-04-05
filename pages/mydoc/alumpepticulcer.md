---
title: "alum - Peptic ulcer"
sidebar: mydoc_sidebar
permalink: alumpepticulcer.html
toc: false 
---

{% include image.html url="images/alumpepticulcer.png" file="alumpepticulcer.png" alt="alumpepticulcer" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D000534 | alum | Drug |
| MESH:D000891 | Anti-Infective Agents, Local | ChemicalSubstance |
| MESH:D001252 | Astringents | ChemicalSubstance |
| MESH:D005744 | Gastric Acid | ChemicalSubstance |
| GO:0006954 | inflammatory response | BiologicalProcess |
| MESH:D010437 | Peptic ulcer | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Alum | SUBCLASS OF | Anti-Infective Agents, Local |
| Alum | SUBCLASS OF | Astringents |
| Anti-Infective Agents, Local | NEGATIVELY CORRELATED WITH | Inflammatory Response |
| Astringents | NEGATIVELY CORRELATED WITH | Gastric Acid |
| Inflammatory Response | POSITIVELY CORRELATED WITH | Peptic Ulcer |
| Gastric Acid | POSITIVELY CORRELATED WITH | Peptic Ulcer |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB09087#mechanism-of-action](https://go.drugbank.com/drugs/DB09087#mechanism-of-action){:target="_blank"}