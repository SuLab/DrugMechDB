---
title: "Cimetidine - Heartburn"
sidebar: mydoc_sidebar
permalink: cimetidineheartburn.html
toc: false 
---

{% include image.html url="images/cimetidineheartburn.png" file="cimetidineheartburn.png" alt="cimetidineheartburn" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D002927 | Cimetidine | Drug |
| UniProt:P25021 | Histamine H2 receptor | Protein |
| GO:0051381 | Histamine binding | BiologicalProcess |
| GO:0001696 | Gastric acid secretion | BiologicalProcess |
| MESH:D006356 | Heartburn | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Cimetidine | DECREASES ACTIVITY OF | Histamine H2 Receptor |
| Histamine H2 Receptor | PREVENTS | Histamine Binding |
| Histamine Binding | NEGATIVELY REGULATES | Gastric Acid Secretion |
| Gastric Acid Secretion | CONTRIBUTES TO | Heartburn |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00501#mechanism-of-action](https://go.drugbank.com/drugs/DB00501#mechanism-of-action){:target="_blank"}