---
title: "Naloxone - Pain"
sidebar: mydoc_sidebar
permalink: naloxonepain.html
toc: false 
---

{% include image.html url="images/naloxonepain.png" file="naloxonepain.png" alt="naloxonepain" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D009270 | Naloxone | Drug |
| UniProt:P35372 | Mu-type opioid receptor | Protein |
| UniProt:P41143 | Delta-type opioid receptor | Protein |
| UniProt:P41145 | Kappa-type opioid receptor | Protein |
| InterPro:IPR000276 | G-Protein coupled receptor | GeneFamily |
| InterPro:IPR000274 | Adenylate cyclase | GeneFamily |
| MESH:D000242 | cAMP levels | ChemicalSubstance |
| GO:0048265 | Response to pain | BiologicalProcess |
| MESH:D010146 | Pain | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Naloxone | DECREASES ACTIVITY OF | Delta-Type Opioid Receptor |
| Delta-Type Opioid Receptor | NEGATIVELY REGULATES | G-Protein Coupled Receptor |
| Naloxone | DECREASES ACTIVITY OF | Mu-Type Opioid Receptor |
| Mu-Type Opioid Receptor | NEGATIVELY REGULATES | G-Protein Coupled Receptor |
| Naloxone | DECREASES ACTIVITY OF | Kappa-Type Opioid Receptor |
| Kappa-Type Opioid Receptor | NEGATIVELY REGULATES | G-Protein Coupled Receptor |
| G-Protein Coupled Receptor | DECREASES ACTIVITY OF | Adenylate Cyclase |
| Adenylate Cyclase | DECREASES ABUNDANCE OF | Camp Levels |
| Camp Levels | POSITIVELY REGULATES | Response To Pain |
| Response To Pain | CAUSED BY | Pain |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01183#mechanism-of-action](https://go.drugbank.com/drugs/DB01183#mechanism-of-action){:target="_blank"}