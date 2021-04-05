---
title: "alum - Dyspepsia"
sidebar: mydoc_sidebar
permalink: alumdyspepsia.html
toc: false 
---

{% include image.html url="images/alumdyspepsia.png" file="alumdyspepsia.png" alt="alumdyspepsia" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D000534 | alum | Drug |
| MESH:D000891 | Anti-Infective Agents, Local | ChemicalSubstance |
| MESH:D001252 | Astringents | ChemicalSubstance |
| MESH:D005744 | Gastric Acid | ChemicalSubstance |
| HP:0005263 | Gastritis | PhenotypicFeature |
| GO:0006954 | inflammatory response | BiologicalProcess |
| HP:0002020 | Gastroesophageal reflux | PhenotypicFeature |
| MESH:D004415 | Dyspepsia | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Alum | SUBCLASS OF | Anti-Infective Agents, Local |
| Alum | SUBCLASS OF | Astringents |
| Anti-Infective Agents, Local | NEGATIVELY CORRELATED WITH | Inflammatory Response |
| Astringents | NEGATIVELY CORRELATED WITH | Gastric Acid |
| Inflammatory Response | POSITIVELY CORRELATED WITH | Gastritis |
| Gastric Acid | POSITIVELY CORRELATED WITH | Gastroesophageal Reflux |
| Gastroesophageal Reflux | POSITIVELY CORRELATED WITH | Dyspepsia |
| Gastritis | POSITIVELY CORRELATED WITH | Dyspepsia |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB09087#mechanism-of-action](https://go.drugbank.com/drugs/DB09087#mechanism-of-action){:target="_blank"}