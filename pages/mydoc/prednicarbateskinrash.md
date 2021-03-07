---
title: "prednicarbate - Skin Rash"
sidebar: mydoc_sidebar
permalink: prednicarbateskinrash.html
toc: false 
---

{% include image.html file="prednicarbateskinrash.png" alt="prednicarbateskinrash" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C035287 | Prednicarbate | Drug |
| UniProt:P04150 | Glucocorticoid receptor | Protein |
| UniProt:P04083 | Annexin A1 | Protein |
| REACT:R-HSA-2162123 | Prostaglandin Synthesis | Pathway |
| GO:0006954 | Inflammation | BiologicalProcess |
| MESH:D005076 | Skin Rash | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Prednicarbate | INCREASES ACTIVITY OF | Glucocorticoid Receptor |
| Glucocorticoid Receptor | INCREASES ABUNDANCE OF | Annexin A1 |
| Annexin A1 | NEGATIVELY REGULATES | Prostaglandin Synthesis |
| Prostaglandin Synthesis | POSITIVELY REGULATES | Inflammation |
| Inflammation | CAUSES | Skin Rash |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01130#mechanism-of-action](https://go.drugbank.com/drugs/DB01130#mechanism-of-action){:target="_blank"}