---
title: "Budesonide - Crohn's disease"
sidebar: mydoc_sidebar
permalink: budesonidecrohnsdisease2.html
toc: false 
---

{% include image.html file="budesonidecrohnsdisease2.png" alt="budesonidecrohnsdisease2" %}![Path Visualization](/images/budesonidecrohnsdisease2.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D019819 | Budesonide | Drug |
| UniProt:P04150 | glucocorticoid receptor | Protein |
| UniProt:P04083 | Annexin A1 | Protein |
| UniProt:P22301 | Interleukin 10 | Protein |
| GO:0019370 | leukotriene synthesis | Protein |
| InterPro:IPR001211 | phospholipase A2 | GeneFamily |
| GO:0050482 | arachidonic acid release | BiologicalProcess |
| GO:0001516 | prostaglandin synthesis | BiologicalProcess |
| GO:0006954 | inflammation | BiologicalProcess |
| MESH:D003424 | Crohn's disease | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Budesonide | MOLECULARLY INTERACTS WITH | Glucocorticoid Receptor |
| Glucocorticoid Receptor | INCREASES ABUNDANCE OF | Annexin A1 |
| Annexin A1 | DECREASES ACTIVITY OF | Phospholipase A2 |
| Glucocorticoid Receptor | INCREASES ABUNDANCE OF | Interleukin 10 |
| Interleukin 10 | DECREASES ACTIVITY OF | Phospholipase A2 |
| Phospholipase A2 | PREVENTS | Arachidonic Acid Release |
| Arachidonic Acid Release | NEGATIVELY REGULATES | Leukotriene Synthesis |
| Leukotriene Synthesis | PREVENTS | Inflammation |
| Arachidonic Acid Release | NEGATIVELY REGULATES | Prostaglandin Synthesis |
| Prostaglandin Synthesis | PREVENTS | Inflammation |
| Inflammation | CORRELATED WITH | Crohn'S Disease |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB01222#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB01222#mechanism-of-action){:target="_blank"}