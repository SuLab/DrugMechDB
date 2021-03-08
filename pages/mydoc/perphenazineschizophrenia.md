---
title: "perphenazine - Schizophrenia"
sidebar: mydoc_sidebar
permalink: perphenazineschizophrenia.html
toc: false 
---

{% include image.html url="images/perphenazineschizophrenia.png" file="perphenazineschizophrenia.png" alt="perphenazineschizophrenia" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D010546 | perphenazine | Drug |
| UniProt:P14416 | D(2) dopamine receptor | Protein |
| UniProt:P21728 | D(1A) dopamine receptor | Protein |
| GO:0014046 | dopamine secretion | BiologicalProcess |
| CHEBI:18243 | dopamine | ChemicalSubstance |
| UBERON:0001910 | medial forebrain bundle | GrossAnatomicalStructure |
| MESH:D012559 | Schizophrenia | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Perphenazine | DECREASES ACTIVITY OF | D(2) Dopamine Receptor |
| Perphenazine | DECREASES ACTIVITY OF | D(1A) Dopamine Receptor |
| D(2) Dopamine Receptor | POSITIVELY REGULATES | Dopamine Secretion |
| D(1A) Dopamine Receptor | POSITIVELY REGULATES | Dopamine Secretion |
| Dopamine Secretion | INCREASES ABUNDANCE OF | Dopamine |
| Dopamine | LOCATED IN | Medial Forebrain Bundle |
| Medial Forebrain Bundle | POSITIVELY CORRELATED WITH | Schizophrenia |
|---------|-----------|---------|

Comment: this drug may bind to calmodulin therefore having an anti-neoplasmic effect (https://pubmed.ncbi.nlm.nih.gov/28062709/). For schizophrenia, the dopamine neurons are located in the mesolimbic dopaminergic system (BTO:0005591), which is a component pathway of the medial forebrain bundle (UBERON:0001910. See [https://en.wikipedia.org/wiki/Medial_forebrain_bundle#Anatomy)](https://en.wikipedia.org/wiki/Medial_forebrain_bundle#Anatomy))

Reference: [https://go.drugbank.com/drugs/DB00850#mechanism-of-action](https://go.drugbank.com/drugs/DB00850#mechanism-of-action){:target="_blank"}