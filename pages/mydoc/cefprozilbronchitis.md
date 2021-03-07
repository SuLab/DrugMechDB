---
title: "Cefprozil - Bronchitis"
sidebar: mydoc_sidebar
permalink: cefprozilbronchitis.html
toc: false 
---

{% include image.html file="cefprozilbronchitis.png" alt="cefprozilbronchitis" %}![Path Visualization](/images/cefprozilbronchitis.png)

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
| Cefprozil | INCREASES ACTIVITY OF | Penicillin-Binding Proteins |
| Penicillin-Binding Proteins | NEGATIVELY REGULATES | Cell Wall Biogenesis |
| Cefprozil | INCREASES ACTIVITY OF | Autolysins |
| Autolysins | CONTRIBUTES TO | Cell Death |
| Cefprozil | NEGATIVELY REGULATES | Peptidoglycan-Protein Cross-Linking |
| Peptidoglycan-Protein Cross-Linking | CONTRIBUTES TO | Cell Death |
| Cell Wall Biogenesis | IN TAXON | Streptococcus Pneumoniae |
| Cell Death | IN TAXON | Streptococcus Pneumoniae |
| Streptococcus Pneumoniae | CAUSES | Bronchitis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB01150#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB01150#mechanism-of-action){:target="_blank"}