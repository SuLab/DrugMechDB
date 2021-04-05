---
title: "Tenoxicam - Arthritis"
sidebar: mydoc_sidebar
permalink: tenoxicamarthritis.html
toc: false 
---

{% include image.html url="images/tenoxicamarthritis.png" file="tenoxicamarthritis.png" alt="tenoxicamarthritis" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C032801 | Tenoxicam | Drug |
| UniProt:P23219 | Cyclooxygenase-1 | Protein |
| REACT:R-HSA-265295 | Prostaglandin synthesis | Pathway |
| GO:0006954 | Inflammation | BiologicalProcess |
| UniProt:P35354 | Cyclooxygenase-2 | Protein |
| MESH:D001168 | Arthritis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Tenoxicam | DECREASES ACTIVITY OF | Cyclooxygenase-1 |
| Cyclooxygenase-1 | NEGATIVELY REGULATES | Prostaglandin Synthesis |
| Tenoxicam | DECREASES ACTIVITY OF | Cyclooxygenase-2 |
| Cyclooxygenase-2 | NEGATIVELY REGULATES | Prostaglandin Synthesis |
| Prostaglandin Synthesis | AMELIORATES | Inflammation |
| Inflammation | CORRELATED WITH | Arthritis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00469#mechanism-of-action](https://go.drugbank.com/drugs/DB00469#mechanism-of-action){:target="_blank"}