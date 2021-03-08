---
title: "Cefprozil - Streptococcus pyogenes infection"
sidebar: mydoc_sidebar
permalink: cefprozilstreptococcuspyogenesinfection.html
toc: false 
---

{% include image.html url="images/cefprozilstreptococcuspyogenesinfection.png" file="cefprozilstreptococcuspyogenesinfection.png" alt="cefprozilstreptococcuspyogenesinfection" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C052018 | Cefprozil | Drug |
| InterPro:IPR001460 | penicillin-binding proteins | GeneFamily |
| InterPro:IPR033907 | Autolysins | GeneFamily |
| GO:0018104 | Peptidoglycan-protein cross-linking | BiologicalProcess |
| GO:0042546 | Cell wall biogenesis | BiologicalProcess |
| GO:0008219 | Cell death | BiologicalProcess |
| NCBITaxon:1314 | Streptococcus pyogenes | OrganismTaxon |
| MESH:D013290 | Streptococcus pyogenes infection | Disease |
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
| Cell Wall Biogenesis | IN TAXON | Streptococcus Pyogenes |
| Cell Death | IN TAXON | Streptococcus Pyogenes |
| Streptococcus Pyogenes | CAUSES | Streptococcus Pyogenes Infection |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01150#mechanism-of-action](https://go.drugbank.com/drugs/DB01150#mechanism-of-action){:target="_blank"}