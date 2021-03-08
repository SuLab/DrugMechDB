---
title: "epinephrine - Open-angle glaucoma"
sidebar: mydoc_sidebar
permalink: epinephrineopenangleglaucoma.html
toc: false 
---

{% include image.html url="epinephrineopenangleglaucoma.png" file="epinephrineopenangleglaucoma.png" alt="epinephrineopenangleglaucoma" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D004837 | epinephrine | Drug |
| UniProt:P35348 | Alpha-1A adrenergic receptor | Protein |
| UniProt:P35368 | Alpha-1B adrenergic receptor | Protein |
| UniProt:P25100 | Alpha-1D adrenergic receptor | Protein |
| REACT:R-HSA-416476﻿ | G alpha (q) signalling events | Pathway |
| REACT:R-HSA-416482﻿ | G alpha (12/13) signalling events | Pathway |
| GO:0042310 | vasoconstriction | BiologicalProcess |
| UBERON:0001796 | aqueous humor of eyeball | GrossAnatomicalStructure |
| HP:0007906 | Ocular Hypertension | PhenotypicFeature |
| MESH:D005902 | Open-angle glaucoma | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Epinephrine | INCREASES ACTIVITY OF | Alpha-1A Adrenergic Receptor |
| Epinephrine | INCREASES ACTIVITY OF | Alpha-1B Adrenergic Receptor |
| Epinephrine | INCREASES ACTIVITY OF | Alpha-1D Adrenergic Receptor |
| Alpha-1D Adrenergic Receptor | PARTICIPATES IN | G Alpha (Q) Signalling Events |
| Alpha-1A Adrenergic Receptor | PARTICIPATES IN | G Alpha (Q) Signalling Events |
| Alpha-1B Adrenergic Receptor | PARTICIPATES IN | G Alpha (Q) Signalling Events |
| Alpha-1D Adrenergic Receptor | PARTICIPATES IN | G Alpha (12/13) Signalling Events |
| Alpha-1A Adrenergic Receptor | PARTICIPATES IN | G Alpha (12/13) Signalling Events |
| Alpha-1B Adrenergic Receptor | PARTICIPATES IN | G Alpha (12/13) Signalling Events |
| G Alpha (Q) Signalling Events | POSITIVELY REGULATES | Vasoconstriction |
| G Alpha (12/13) Signalling Events | POSITIVELY REGULATES | Vasoconstriction |
| Vasoconstriction | NEGATIVELY CORRELATED WITH | Aqueous Humor Of Eyeball |
| Aqueous Humor Of Eyeball | POSITIVELY CORRELATED WITH | Ocular Hypertension |
| Ocular Hypertension | POSITIVELY CORRELATED WITH | Open-Angle Glaucoma |
|---------|-----------|---------|

Comment: DrugBank (https://go.drugbank.com/drugs/DB00668) has this drug modulating beta receptors but not for glaucoma. For this indication, the ligand should be an antagonist (and epinephrine is an agonist instead)

Reference: [https://go.drugbank.com/drugs/DB00668#mechanism-of-action](https://go.drugbank.com/drugs/DB00668#mechanism-of-action){:target="_blank"}