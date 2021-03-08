---
title: "Eplerenone - Hypertensive disorder"
sidebar: mydoc_sidebar
permalink: eplerenonehypertensivedisorder.html
toc: false 
---

{% include image.html url="images/eplerenonehypertensivedisorder.png" file="eplerenonehypertensivedisorder.png" alt="eplerenonehypertensivedisorder" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| DB:DB00700 | Eplerenone | Drug |
| UniProt:P08235 | mineralocorticoid receptor | Protein |
| UniProt:P00797 | plasma renin | Protein |
| MESH:D000450 | serum aldosterone | ChemicalSubstance |
| HP:0011104 | blood volume | PhenotypicFeature |
| HP:0005117 | diastolic blood pressure | PhenotypicFeature |
| HP:0004421 | systolic blood pressure | PhenotypicFeature |
| MESH:D006973 | Hypertensive disorder | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Eplerenone | DECREASES ACTIVITY OF | Mineralocorticoid Receptor |
| Mineralocorticoid Receptor | INCREASES ABUNDANCE OF | Plasma Renin |
| Mineralocorticoid Receptor | INCREASES ABUNDANCE OF | Serum Aldosterone |
| Plasma Renin | DECREASES ABUNDANCE OF | Blood Volume |
| Serum Aldosterone | DECREASES ABUNDANCE OF | Blood Volume |
| Blood Volume | NEGATIVELY REGULATES | Systolic Blood Pressure |
| Blood Volume | NEGATIVELY REGULATES | Diastolic Blood Pressure |
| Systolic Blood Pressure | PREVENTS | Hypertensive Disorder |
| Diastolic Blood Pressure | PREVENTS | Hypertensive Disorder |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00700#mechanism-of-action](https://go.drugbank.com/drugs/DB00700#mechanism-of-action){:target="_blank"}