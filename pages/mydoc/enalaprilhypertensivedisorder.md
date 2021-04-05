---
title: "Enalapril - Hypertensive disorder"
sidebar: mydoc_sidebar
permalink: enalaprilhypertensivedisorder.html
toc: false 
---

{% include image.html url="images/enalaprilhypertensivedisorder.png" file="enalaprilhypertensivedisorder.png" alt="enalaprilhypertensivedisorder" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D004656 | Enalapril | Drug |
| MESH:D015773 | Enalaprilat | Drug |
| UniProt:P12821 | Angiotensin-converting enzyme | Protein |
| MESH:D000804 | Angiotensin II | ChemicalSubstance |
| GO:0070294 | Renal sodium ion absorption | BiologicalProcess |
| GO:0003092 | Renal water retention | BiologicalProcess |
| GO:0045777 | Positive regulation of blood pressure | BiologicalProcess |
| MESH:D014661 | Vasoconstriction | Disease |
| MESH:D006973 | Hypertensive disorder | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Enalapril | PRODUCES | Enalaprilat |
| Enalaprilat | DECREASES ACTIVITY OF | Angiotensin-Converting Enzyme |
| Angiotensin-Converting Enzyme | INCREASES ABUNDANCE OF | Angiotensin Ii |
| Angiotensin Ii | CAUSES | Renal Sodium Ion Absorption |
| Renal Sodium Ion Absorption | POSITIVELY CORRELATED WITH | Renal Water Retention |
| Renal Water Retention | CONTRIBUTES TO | Positive Regulation Of Blood Pressure |
| Positive Regulation Of Blood Pressure | AFFECTS RISK FOR | Hypertensive Disorder |
| Angiotensin Ii | CAUSES | Vasoconstriction |
| Vasoconstriction | CONTRIBUTES TO | Hypertensive Disorder |
|---------|-----------|---------|

Comment: Being a prodrug, enalapril is rapidly biotransformed into its active metabolite, enalaprilat. Please note this drug had 2 DrugBank IDs in the Drug Centarl, DB00584 and DB09477. The DB09477 is ID for Enalapril, which has been previously curated.

Reference: [https://go.drugbank.com/drugs/DB00584#mechanism-of-action](https://go.drugbank.com/drugs/DB00584#mechanism-of-action){:target="_blank"}