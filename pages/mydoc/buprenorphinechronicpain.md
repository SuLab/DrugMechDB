---
title: "Buprenorphine - Chronic pain"
sidebar: mydoc_sidebar
permalink: buprenorphinechronicpain.html
toc: false 
---

{% include image.html file="buprenorphinechronicpain.png" alt="buprenorphinechronicpain" %}![Path Visualization](/images/buprenorphinechronicpain.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D002047 | Buprenorphine | Drug |
| UniProt:P35372 | Mu-opioid receptor | Protein |
| InterPro:IPR013673 | G-protein–gated potassium channel | GeneFamily |
| MESH:D000242 | cAMP | ChemicalSubstance |
| GO:0007269 | neurotransmitter release | BiologicalProcess |
| GO:0060081 | membrane hyperpolarization | BiologicalProcess |
| MESH:D059350 | Chronic pain | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Buprenorphine | INCREASES ACTIVITY OF | Mu-Opioid Receptor |
| Mu-Opioid Receptor | POSITIVELY REGULATES | G-Protein–Gated Potassium Channel |
| G-Protein–Gated Potassium Channel | DECREASES ABUNDANCE OF | Camp |
| Camp | PREVENTS | Neurotransmitter Release |
| Neurotransmitter Release | DECREASES ACTIVITY OF | Membrane Hyperpolarization |
| Membrane Hyperpolarization | AMELIORATES | Chronic Pain |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB00921#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB00921#mechanism-of-action){:target="_blank"}