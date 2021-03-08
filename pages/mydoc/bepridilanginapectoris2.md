---
title: "bepridil - Angina pectoris"
sidebar: mydoc_sidebar
permalink: bepridilanginapectoris2.html
toc: false 
---

{% include image.html url="images/bepridilanginapectoris2.png" file="bepridilanginapectoris2.png" alt="bepridilanginapectoris2" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D015764 | Bepridil | Drug |
| UniProt:P05023 | Sodium/potassium-transporting ATPase subunit alpha-1 | Protein |
| GO:0036376 | sodium ion export across plasma membrane | BiologicalProcess |
| GO:0070509 | calcium ion import | BiologicalProcess |
| MESH:D017202 | Myocardial Ischemia | PhenotypicFeature |
| MESH:D000787 | Angina pectoris | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Bepridil | DECREASES ACTIVITY OF | Sodium/Potassium-Transporting Atpase Subunit Alpha-1 |
| Sodium/Potassium-Transporting Atpase Subunit Alpha-1 | POSITIVELY REGULATES | Sodium Ion Export Across Plasma Membrane |
| Sodium Ion Export Across Plasma Membrane | POSITIVELY CORRELATED WITH | Calcium Ion Import |
| Calcium Ion Import | NEGATIVELY CORRELATED WITH | Myocardial Ischemia |
| Myocardial Ischemia | POSITIVELY CORRELATED WITH | Angina Pectoris |
|---------|-----------|---------|

Comment: note that this drug is only associated with calcium channel blockers in ChEMBL (https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1008/), not with potassium channel blockers (or other targets) as DrugBank has it. This drug is no longer sold in the United States. It's been implicated in causing ventricular arrhythmia.

Reference: [https://go.drugbank.com/drugs/DB01244#mechanism-of-action](https://go.drugbank.com/drugs/DB01244#mechanism-of-action){:target="_blank"}