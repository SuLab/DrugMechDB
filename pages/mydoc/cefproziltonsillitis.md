---
title: "Cefprozil - Tonsillitis"
sidebar: mydoc_sidebar
permalink: cefproziltonsillitis.html
toc: false 
---

{% include image.html file="cefproziltonsillitis.png" alt="cefproziltonsillitis" %}![Path Visualization](/images/cefproziltonsillitis.png)

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
| Cefprozil | INCREASES ACTIVITY OF | Penicillin-Binding Proteins |
| Penicillin-Binding Proteins | NEGATIVELY REGULATES | Cell Wall Biogenesis |
| Cefprozil | INCREASES ACTIVITY OF | Autolysins |
| Autolysins | CONTRIBUTES TO | Cell Death |
| Cefprozil | NEGATIVELY REGULATES | Peptidoglycan-Protein Cross-Linking |
| Peptidoglycan-Protein Cross-Linking | CONTRIBUTES TO | Cell Death |
| Cell Wall Biogenesis | IN TAXON | Streptococcus Pyogenes |
| Cell Death | IN TAXON | Streptococcus Pyogenes |
| Streptococcus Pyogenes | CAUSES | Tonsillitis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB:DB01150#mechanism-of-action](https://go.drugbank.com/drugs/DB:DB01150#mechanism-of-action){:target="_blank"}