---
title: "Cefprozil - Tonsillitis"
sidebar: mydoc_sidebar
permalink: cefproziltonsillitis2.html
toc: false 
---

{% include image.html url="images/cefproziltonsillitis2.png" file="cefproziltonsillitis2.png" alt="cefproziltonsillitis2" %}

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
| MESH:D014069 | Tonsillitis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Cefprozil | DECREASES ACTIVITY OF | Penicillin-Binding Proteins |
| Penicillin-Binding Proteins | NEGATIVELY REGULATES | Peptidoglycan-Protein Cross-Linking |
| Peptidoglycan-Protein Cross-Linking | DISRUPTS | Cell Wall Biogenesis |
| Cell Wall Biogenesis | CONTRIBUTES TO | Cell Death |
| Cefprozil | INCREASES ACTIVITY OF | Autolysins |
| Autolysins | CONTRIBUTES TO | Cell Death |
| Cell Death | IN TAXON | Streptococcus Pyogenes |
| Streptococcus Pyogenes | CAUSES | Tonsillitis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01150#mechanism-of-action](https://go.drugbank.com/drugs/DB01150#mechanism-of-action){:target="_blank"}