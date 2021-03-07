---
title: "Estradiol - Postmenopausal osteoporosis"
sidebar: mydoc_sidebar
permalink: estradiolpostmenopausalosteoporosis.html
toc: false 
---

{% include image.html file="estradiolpostmenopausalosteoporosis.png" alt="estradiolpostmenopausalosteoporosis" %}![Path Visualization](/images/estradiolpostmenopausalosteoporosis.png)

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D004958 | Estradiol | Drug |
| UniProt:P03372 | Estrogen receptor alpha | Protein |
| UniProt:Q92731 | Estrogen receptor beta | Protein |
| GO:0043627 | Response to estrogen | BiologicalProcess |
| CL:0000092 | Osteoclast | Cell |
| GO:0046849 | Bone remodeling | BiologicalProcess |
| GO:0045453 | Bone resorption | BiologicalProcess |
| MESH:D015663 | Postmenopausal osteoporosis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Estradiol | INCREASES ACTIVITY OF | Estrogen Receptor Alpha |
| Estradiol | INCREASES ACTIVITY OF | Estrogen Receptor Beta |
| Estrogen Receptor Alpha | PARTICIPATES IN | Response To Estrogen |
| Estrogen Receptor Beta | PARTICIPATES IN | Response To Estrogen |
| Response To Estrogen | NEGATIVELY REGULATES | Osteoclast |
| Response To Estrogen | NEGATIVELY REGULATES | Bone Remodeling |
| Osteoclast | CONTRIBUTES TO | Bone Resorption |
| Bone Remodeling | CONTRIBUTES TO | Postmenopausal Osteoporosis |
| Bone Resorption | CAUSES | Postmenopausal Osteoporosis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB00783#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB00783#mechanism-of-action){:target="_blank"}