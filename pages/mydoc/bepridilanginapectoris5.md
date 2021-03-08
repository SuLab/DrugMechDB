---
title: "bepridil - Angina pectoris"
sidebar: mydoc_sidebar
permalink: bepridilanginapectoris5.html
toc: false 
---

{% include image.html url="images/bepridilanginapectoris5.png" file="bepridilanginapectoris5.png" alt="bepridilanginapectoris5" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D015764 | Bepridil | Drug |
| UniProt:Q9NY47 | Voltage-dependent calcium channel subunit alpha-2/delta-2 | Protein |
| GO:1903779 | regulation of cardiac conduction | BiologicalProcess |
| GO:0002027 | regulation of heart rate | BiologicalProcess |
| MESH:D017202 | Myocardial Ischemia | PhenotypicFeature |
| MESH:D000787 | Angina pectoris | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Bepridil | NEGATIVELY REGULATES | Voltage-Dependent Calcium Channel Subunit Alpha-2/Delta-2 |
| Voltage-Dependent Calcium Channel Subunit Alpha-2/Delta-2 | POSITIVELY REGULATES | Regulation Of Cardiac Conduction |
| Regulation Of Cardiac Conduction | POSITIVELY CORRELATED WITH | Regulation Of Heart Rate |
| Regulation Of Heart Rate | NEGATIVELY CORRELATED WITH | Myocardial Ischemia |
| Myocardial Ischemia | POSITIVELY CORRELATED WITH | Angina Pectoris |
|---------|-----------|---------|

Comment: note that this drug is only associated with calcium channel blockers in ChEMBL (https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1008/), not with potassium channel blockers (or other targets) as DrugBank has it. This drug is no longer sold in the United States. It's been implicated in causing ventricular arrhythmia.

Reference: [https://go.drugbank.com/drugs/DB01244#mechanism-of-action](https://go.drugbank.com/drugs/DB01244#mechanism-of-action){:target="_blank"}