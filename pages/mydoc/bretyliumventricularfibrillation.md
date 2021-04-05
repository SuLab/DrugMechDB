---
title: "Bretylium - Ventricular fibrillation"
sidebar: mydoc_sidebar
permalink: bretyliumventricularfibrillation.html
toc: false 
---

{% include image.html url="images/bretyliumventricularfibrillation.png" file="bretyliumventricularfibrillation.png" alt="bretyliumventricularfibrillation" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C045166 | Bretylium | Drug |
| GO:0048243 | Release of norepinephrine | BiologicalProcess |
| InterPro:IPR005821 | Voltage-gated potassium channel | GeneFamily |
| GO:0001508 | Action potential | BiologicalProcess |
| HP:0004308 | Ventricular arrhythmias | PhenotypicFeature |
| MESH:D014693 | Ventricular fibrillation | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Bretylium | NEGATIVELY REGULATES | Release Of Norepinephrine |
| Release Of Norepinephrine | DECREASES ACTIVITY OF | Voltage-Gated Potassium Channel |
| Voltage-Gated Potassium Channel | DECREASES RESPONSE TO | Action Potential |
| Action Potential | PREVENTS | Ventricular Arrhythmias |
| Ventricular Arrhythmias | CAUSES | Ventricular Fibrillation |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01158#mechanism-of-action](https://go.drugbank.com/drugs/DB01158#mechanism-of-action){:target="_blank"}