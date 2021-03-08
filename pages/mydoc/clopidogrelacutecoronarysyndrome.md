---
title: "clopidogrel - Acute coronary syndrome"
sidebar: mydoc_sidebar
permalink: clopidogrelacutecoronarysyndrome.html
toc: false 
---

{% include image.html file="clopidogrelacutecoronarysyndrome.png" alt="clopidogrelacutecoronarysyndrome" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| DB:DB00758 | clopidogrel | Drug |
| UniProt:P23141 | carboxylesterase-1 | Protein |
| UniProt:Q9H244 | P2Y12 receptor | Protein |
| CL:0000233 | platelet | Cell |
| GO:0043531 | ADP binding | BiologicalProcess |
| PR:000028445 | glycoprotein GPIIb/IIIa complex | MacromolecularComplex |
| GO:0070527 | platelet aggregation | BiologicalProcess |
| MESH:D054058 | Acute coronary syndrome | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Clopidogrel | ENABLED BY | Carboxylesterase-1 |
| Carboxylesterase-1 | INCREASES ACTIVITY OF | P2Y12 Receptor |
| P2Y12 Receptor | LOCATED IN | Platelet |
| Platelet | PREVENTS | Adp Binding |
| Adp Binding | DECREASES ACTIVITY OF | Glycoprotein Gpiib/Iiia Complex |
| Glycoprotein Gpiib/Iiia Complex | PREVENTS | Platelet Aggregation |
| Platelet Aggregation | CORRELATED WITH | Acute Coronary Syndrome |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00758#mechanism-of-action](https://go.drugbank.com/drugs/DB00758#mechanism-of-action){:target="_blank"}