---
title: "loracarbef - Pneumonia"
sidebar: mydoc_sidebar
permalink: loracarbefpneumonia.html
toc: false 
---

{% include image.html url="images/loracarbefpneumonia.png" file="loracarbefpneumonia.png" alt="loracarbefpneumonia" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C054920 | Loracarbef | Drug |
| InterPro:IPR005311 | penicillin binding proteins | GeneFamily |
| GO:0018104 | cross-linking of the peptidoglycan | BiologicalProcess |
| GO:0005618 | cell wall | CellularComponent |
| NCBITaxon:1280 | Staphylococcus aureus | OrganismTaxon |
| MESH:D011014 | Pneumonia | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Loracarbef | DECREASES ACTIVITY OF | Penicillin Binding Proteins |
| Penicillin Binding Proteins | PREVENTS | Cross-Linking Of The Peptidoglycan |
| Cross-Linking Of The Peptidoglycan | CONTRIBUTES TO | Cell Wall |
| Cell Wall | IN TAXON | Staphylococcus Aureus |
| Staphylococcus Aureus | CAUSES | Pneumonia |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00447#mechanism-of-action](https://go.drugbank.com/drugs/DB00447#mechanism-of-action){:target="_blank"}