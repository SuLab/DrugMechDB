---
title: "Cefprozil - Bronchitis"
sidebar: mydoc_sidebar
permalink: cefprozilbronchitis2.html
toc: false 
---

{% include image.html url="images/cefprozilbronchitis2.png" file="cefprozilbronchitis2.png" alt="cefprozilbronchitis2" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C052018 | Cefprozil | Drug |
| UniProt:Q04707 | penicillin-binding proteins | Protein |
| InterPro:IPR033907 | Autolysins | GeneFamily |
| GO:0018104 | Peptidoglycan-protein cross-linking | BiologicalProcess |
| GO:0042546 | Cell wall biogenesis | BiologicalProcess |
| GO:0008219 | Cell death | BiologicalProcess |
| NCBITaxon:1313 | Streptococcus pneumoniae | OrganismTaxon |
| MESH:D001991 | Bronchitis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Cefprozil | DECREASES ACTIVITY OF | Penicillin-Binding Proteins |
| Peptidoglycan-Protein Cross-Linking | DISRUPTS | Cell Wall Biogenesis |
| Cell Wall Biogenesis | CONTRIBUTES TO | Cell Death |
| Cefprozil | INCREASES ACTIVITY OF | Autolysins |
| Autolysins | CAUSES | Cell Death |
| Penicillin-Binding Proteins | NEGATIVELY REGULATES | Peptidoglycan-Protein Cross-Linking |
| Cell Death | IN TAXON | Streptococcus Pneumoniae |
| Streptococcus Pneumoniae | CAUSES | Bronchitis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01150#mechanism-of-action](https://go.drugbank.com/drugs/DB01150#mechanism-of-action){:target="_blank"}