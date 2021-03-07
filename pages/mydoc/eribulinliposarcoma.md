---
title: "eribulin - Liposarcoma"
sidebar: mydoc_sidebar
permalink: eribulinliposarcoma.html
toc: false 
---

{% include image.html file="eribulinliposarcoma.png" alt="eribulinliposarcoma" %}![Path Visualization](/images/eribulinliposarcoma.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C490954 | eribulin | Drug |
| PR:000028799 | Tubulin | MacromolecularComplex |
| GO:0000278 | mitotic cell cycle | BiologicalProcess |
| GO:0051225 | spindle assembly | BiologicalProcess |
| GO:0006915 | apoptotic process | BiologicalProcess |
| MESH:D008080 | Liposarcoma | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Eribulin | NEGATIVELY REGULATES | Tubulin |
| Tubulin | POSITIVELY REGULATES | Mitotic Cell Cycle |
| Tubulin | POSITIVELY REGULATES | Spindle Assembly |
| Mitotic Cell Cycle | NEGATIVELY CORRELATED WITH | Apoptotic Process |
| Spindle Assembly | NEGATIVELY CORRELATED WITH | Apoptotic Process |
| Apoptotic Process | POSITIVELY CORRELATED WITH | Liposarcoma |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB08871#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB08871#mechanism-of-action){:target="_blank"}