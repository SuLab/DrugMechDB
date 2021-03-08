---
title: "Cefprozil - Infection due to Staphylococcus aureus"
sidebar: mydoc_sidebar
permalink: cefprozilinfectionduetostaphylococcusaureus.html
toc: false 
---

{% include image.html file="cefprozilinfectionduetostaphylococcusaureus.png" alt="cefprozilinfectionduetostaphylococcusaureus" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C052018 | Cefprozil | Drug |
| UniProt:Q53613 | penicillin-binding proteins | Protein |
| InterPro:IPR033907 | Autolysins | GeneFamily |
| GO:0018104 | Peptidoglycan-protein cross-linking | BiologicalProcess |
| GO:0042546 | Cell wall biogenesis | BiologicalProcess |
| GO:0008219 | Cell death | BiologicalProcess |
| NCBITaxon:1280 | Staphylococcus aureus | OrganismTaxon |
| MESH:D013203 | Infection due to Staphylococcus aureus | Disease |
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
| Cell Wall Biogenesis | IN TAXON | Staphylococcus Aureus |
| Cell Death | IN TAXON | Staphylococcus Aureus |
| Staphylococcus Aureus | CAUSES | Infection Due To Staphylococcus Aureus |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01150#mechanism-of-action](https://go.drugbank.com/drugs/DB01150#mechanism-of-action){:target="_blank"}