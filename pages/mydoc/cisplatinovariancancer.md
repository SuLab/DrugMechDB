---
title: "cisplatin - Ovarian Cancer"
sidebar: mydoc_sidebar
permalink: cisplatinovariancancer.html
toc: false 
---

{% include image.html url="cisplatinovariancancer.png" file="cisplatinovariancancer.png" alt="cisplatinovariancancer" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D002945 | Cisplatin | Drug |
| GO:0090592 | DNA synthesis involved in DNA replication | BiologicalProcess |
| GO:0006351 | Transcription, DNA-templated | BiologicalProcess |
| MESH:D004247 | DNA | ChemicalSubstance |
| GO:0008283 | Cell population proliferation | BiologicalProcess |
| MESH:D010051 | Ovarian Cancer | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Cisplatin | NEGATIVELY REGULATES | Dna Synthesis Involved In Dna Replication |
| Cisplatin | NEGATIVELY REGULATES | Transcription, Dna-Templated |
| Cisplatin | DISRUPTS | Dna |
| Dna Synthesis Involved In Dna Replication | PART OF | Cell Population Proliferation |
| Transcription, Dna-Templated | PART OF | Cell Population Proliferation |
| Dna | OCCURS IN | Ovarian Cancer |
| Cell Population Proliferation | POSITIVELY CORRELATED WITH | Ovarian Cancer |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00515#mechanism-of-action](https://go.drugbank.com/drugs/DB00515#mechanism-of-action){:target="_blank"}