---
title: "bepridil - Angina pectoris"
sidebar: mydoc_sidebar
permalink: bepridilanginapectoris4.html
toc: false 
---

{% include image.html url="bepridilanginapectoris4.png" file="bepridilanginapectoris4.png" alt="bepridilanginapectoris4" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D015764 | Bepridil | Drug |
| UniProt:O95180 | Voltage-dependent T-type calcium channel subunit alpha-1H | Protein |
| GO:0070509 | calcium ion import | BiologicalProcess |
| GO:0086046 | membrane depolarization during SA node cell action potential | BiologicalProcess |
| GO:0002027 | regulation of heart rate | BiologicalProcess |
| MESH:D017202 | Myocardial Ischemia | PhenotypicFeature |
| MESH:D000787 | Angina pectoris | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Bepridil | NEGATIVELY REGULATES | Voltage-Dependent T-Type Calcium Channel Subunit Alpha-1H |
| Voltage-Dependent T-Type Calcium Channel Subunit Alpha-1H | POSITIVELY CORRELATED WITH | Calcium Ion Import |
| Voltage-Dependent T-Type Calcium Channel Subunit Alpha-1H | POSITIVELY CORRELATED WITH | Membrane Depolarization During Sa Node Cell Action Potential |
| Calcium Ion Import | POSITIVELY REGULATES | Regulation Of Heart Rate |
| Membrane Depolarization During Sa Node Cell Action Potential | POSITIVELY REGULATES | Regulation Of Heart Rate |
| Regulation Of Heart Rate | NEGATIVELY CORRELATED WITH | Myocardial Ischemia |
| Myocardial Ischemia | POSITIVELY CORRELATED WITH | Angina Pectoris |
|---------|-----------|---------|

Comment: note that this drug is only associated with calcium channel blockers in ChEMBL (https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1008/), not with potassium channel blockers (or other targets) as DrugBank has it. This drug is no longer sold in the United States. It's been implicated in causing ventricular arrhythmia.

Reference: [https://go.drugbank.com/drugs/DB01244#mechanism-of-action](https://go.drugbank.com/drugs/DB01244#mechanism-of-action){:target="_blank"}