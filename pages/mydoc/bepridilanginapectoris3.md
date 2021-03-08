---
title: "bepridil - Angina pectoris"
sidebar: mydoc_sidebar
permalink: bepridilanginapectoris3.html
toc: false 
---

{% include image.html url="images/bepridilanginapectoris3.png" file="bepridilanginapectoris3.png" alt="bepridilanginapectoris3" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D015764 | Bepridil | Drug |
| UniProt:O00555 | Voltage-dependent P/Q-type calcium channel subunit alpha-1A | Protein |
| GO:0070509 | calcium ion import | BiologicalProcess |
| GO:0042311 | vasodilation | BiologicalProcess |
| GO:0002027 | regulation of heart rate | BiologicalProcess |
| GO:1903779 | regulation of cardiac conduction | BiologicalProcess |
| MESH:D017202 | Myocardial Ischemia | PhenotypicFeature |
| MESH:D000787 | Angina pectoris | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Bepridil | NEGATIVELY REGULATES | Voltage-Dependent P/Q-Type Calcium Channel Subunit Alpha-1A |
| Voltage-Dependent P/Q-Type Calcium Channel Subunit Alpha-1A | POSITIVELY CORRELATED WITH | Calcium Ion Import |
| Calcium Ion Import | NEGATIVELY CORRELATED WITH | Vasodilation |
| Calcium Ion Import | POSITIVELY REGULATES | Regulation Of Heart Rate |
| Calcium Ion Import | POSITIVELY REGULATES | Regulation Of Cardiac Conduction |
| Vasodilation | NEGATIVELY CORRELATED WITH | Myocardial Ischemia |
| Regulation Of Heart Rate | NEGATIVELY CORRELATED WITH | Myocardial Ischemia |
| Regulation Of Cardiac Conduction | NEGATIVELY CORRELATED WITH | Myocardial Ischemia |
| Myocardial Ischemia | POSITIVELY CORRELATED WITH | Angina Pectoris |
|---------|-----------|---------|

Comment: note that this drug is only associated with calcium channel blockers in ChEMBL (https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1008/), not with potassium channel blockers (or other targets) as DrugBank has it. This drug is no longer sold in the United States. It's been implicated in causing ventricular arrhythmia.

Reference: [https://go.drugbank.com/drugs/DB01244#mechanism-of-action](https://go.drugbank.com/drugs/DB01244#mechanism-of-action){:target="_blank"}