---
title: "Gabapentin - Restless legs"
sidebar: mydoc_sidebar
permalink: gabapentinrestlesslegs.html
toc: false 
---

{% include image.html url="images/gabapentinrestlesslegs.png" file="gabapentinrestlesslegs.png" alt="gabapentinrestlesslegs" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| DB:DB00996 | Gabapentin | Drug |
| UniProt:Q9NY47 | Voltage-dependent calcium channel subunit alpha-2/delta-2 | Protein |
| InterPro:IPR018882 | NMDA receptors | GeneFamily |
| InterPro:IPR037440 | Neurexins | GeneFamily |
| InterPro:IPR000884 | Thrombospondins | GeneFamily |
| UniProt:Q00975 | Voltage-gated calcium channels | Protein |
| GO:0098793 | Presynapse | CellularComponent |
| GO:0015278 | Calcium-release channel activity | MolecularActivity |
| GO:0005262 | Calcium channel activity | MolecularActivity |
| GO:0007269 | Neurotransmitter release | BiologicalProcess |
| HP:0012514 | Lower limb pain | PhenotypicFeature |
| MESH:D012148 | Restless legs | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Gabapentin | DECREASES ACTIVITY OF | Voltage-Dependent Calcium Channel Subunit Alpha-2/Delta-2 |
| Voltage-Dependent Calcium Channel Subunit Alpha-2/Delta-2 | DECREASES MOLECULAR INTERACTION | Nmda Receptors |
| Nmda Receptors | DECREASES EXPRESSION OF | Voltage-Gated Calcium Channels |
| Voltage-Dependent Calcium Channel Subunit Alpha-2/Delta-2 | DECREASES MOLECULAR INTERACTION | Neurexins |
| Neurexins | DECREASES EXPRESSION OF | Voltage-Gated Calcium Channels |
| Voltage-Dependent Calcium Channel Subunit Alpha-2/Delta-2 | DECREASES MOLECULAR INTERACTION | Thrombospondins |
| Thrombospondins | DECREASES EXPRESSION OF | Voltage-Gated Calcium Channels |
| Voltage-Gated Calcium Channels | LOCATED IN | Presynapse |
| Presynapse | PREVENTS | Calcium-Release Channel Activity |
| Calcium-Release Channel Activity | POSITIVELY REGULATES | Neurotransmitter Release |
| Presynapse | NEGATIVELY REGULATES | Calcium Channel Activity |
| Calcium Channel Activity | POSITIVELY REGULATES | Neurotransmitter Release |
| Neurotransmitter Release | AMELIORATES | Lower Limb Pain |
| Lower Limb Pain | CORRELATED WITH | Restless Legs |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00996#mechanism-of-action](https://go.drugbank.com/drugs/DB00996#mechanism-of-action){:target="_blank"}