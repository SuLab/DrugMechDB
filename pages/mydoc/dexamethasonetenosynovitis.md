---
title: "dexamethasone - Tenosynovitis"
sidebar: mydoc_sidebar
permalink: dexamethasonetenosynovitis.html
toc: false 
---

![Path Visualization](/images/dexamethasonetenosynovitis.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D003907 | dexamethasone | Drug |
| UniProt:P04150 | Glucocorticoid receptor | Protein |
| UniProt:P04083 | Annexin A1 | Protein |
| REACT:R-HSA-2162123 | Prostaglandin Synthesis | Pathway |
| GO:0006954 | Inflammation | BiologicalProcess |
| MESH:D013717 | Tenosynovitis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Dexamethasone | INCREASES ACTIVITY OF | Glucocorticoid Receptor |
| Glucocorticoid Receptor | INCREASES ABUNDANCE OF | Annexin A1 |
| Annexin A1 | NEGATIVELY REGULATES | Prostaglandin Synthesis |
| Prostaglandin Synthesis | POSITIVELY REGULATES | Inflammation |
| Inflammation | CAUSES | Tenosynovitis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01234#mechanism-of-action](https://go.drugbank.com/drugs/DB01234#mechanism-of-action){:target="_blank"}