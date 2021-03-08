---
title: "epinephrine - Open-angle glaucoma"
sidebar: mydoc_sidebar
permalink: epinephrineopenangleglaucoma2.html
toc: false 
---

{% include image.html url="epinephrineopenangleglaucoma2.png" file="epinephrineopenangleglaucoma2.png" alt="epinephrineopenangleglaucoma2" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D004837 | epinephrine | Drug |
| UniProt:P18089 | Alpha-2B adrenergic receptor | Protein |
| UniProt:P08913 | Alpha-2A adrenergic receptor | Protein |
| REACT:R-HSA-418594 | G alpha (i) signalling events | Pathway |
| REACT:R-HSA-418597 | G alpha (z) signalling events | Pathway |
| GO:0042310 | vasoconstriction | BiologicalProcess |
| UBERON:0001796 | Aqueous Humor | GrossAnatomicalStructure |
| HP:0007906 | Ocular Hypertension | PhenotypicFeature |
| MESH:D005902 | Open-angle glaucoma | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Epinephrine | INCREASES ACTIVITY OF | Alpha-2B Adrenergic Receptor |
| Epinephrine | INCREASES ACTIVITY OF | Alpha-2A Adrenergic Receptor |
| Alpha-2B Adrenergic Receptor | PARTICIPATES IN | G Alpha (I) Signalling Events |
| Alpha-2B Adrenergic Receptor | PARTICIPATES IN | G Alpha (Z) Signalling Events |
| Alpha-2A Adrenergic Receptor | PARTICIPATES IN | G Alpha (I) Signalling Events |
| Alpha-2A Adrenergic Receptor | PARTICIPATES IN | G Alpha (Z) Signalling Events |
| G Alpha (I) Signalling Events | POSITIVELY REGULATES | Vasoconstriction |
| G Alpha (Z) Signalling Events | POSITIVELY REGULATES | Vasoconstriction |
| Vasoconstriction | NEGATIVELY CORRELATED WITH | Aqueous Humor |
| Aqueous Humor | POSITIVELY CORRELATED WITH | Ocular Hypertension |
| Ocular Hypertension | POSITIVELY CORRELATED WITH | Open-Angle Glaucoma |
|---------|-----------|---------|

Comment: DrugBank (https://go.drugbank.com/drugs/DB00668) has this drug modulating beta receptors but not for glaucoma. For this indication, the ligand should be an antagonist (and epinephrine is an agonist instead)

Reference: [https://go.drugbank.com/drugs/DB00668#mechanism-of-action](https://go.drugbank.com/drugs/DB00668#mechanism-of-action){:target="_blank"}