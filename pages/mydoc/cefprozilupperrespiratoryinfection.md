---
title: "Cefprozil - Upper respiratory infection"
sidebar: mydoc_sidebar
permalink: cefprozilupperrespiratoryinfection.html
toc: false 
---

{% include image.html file="cefprozilupperrespiratoryinfection.png" alt="cefprozilupperrespiratoryinfection" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C052018 | Cefprozil | Drug |
| UniProt:P45299 | penicillin-binding proteins | Protein |
| InterPro:IPR033907 | Autolysins | GeneFamily |
| GO:0018104 | Peptidoglycan-protein cross-linking | BiologicalProcess |
| GO:0042546 | Cell wall biogenesis | BiologicalProcess |
| GO:0008219 | Cell death | BiologicalProcess |
| NCBITaxon:727 | Haemophilus influenzae | OrganismTaxon |
| MESH:D012141 | Upper respiratory infection | Disease |
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
| Cell Wall Biogenesis | IN TAXON | Haemophilus Influenzae |
| Cell Death | IN TAXON | Haemophilus Influenzae |
| Haemophilus Influenzae | CAUSES | Upper Respiratory Infection |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01150#mechanism-of-action](https://go.drugbank.com/drugs/DB01150#mechanism-of-action){:target="_blank"}