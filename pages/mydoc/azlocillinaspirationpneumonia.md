---
title: "Azlocillin - Aspiration pneumonia"
sidebar: mydoc_sidebar
permalink: azlocillinaspirationpneumonia.html
toc: false 
---

{% include image.html url="images/azlocillinaspirationpneumonia.png" file="azlocillinaspirationpneumonia.png" alt="azlocillinaspirationpneumonia" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D001390 | Azlocillin | Drug |
| GO:0009252 | Peptidoglycan biosynthetic process | BiologicalProcess |
| InterPro:IPR005311 | Penicillin binding proteins | GeneFamily |
| GO:0009273 | Peptidoglycan-based cell wall biogenesis | BiologicalProcess |
| GO:0051301 | Cell division | BiologicalProcess |
| NCBITaxon:2 | Bacteria | OrganismTaxon |
| MESH:D011015 | Aspiration pneumonia | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Azlocillin | DECREASES ACTIVITY OF | Penicillin Binding Proteins |
| Penicillin Binding Proteins | POSITIVELY REGULATES | Peptidoglycan Biosynthetic Process |
| Peptidoglycan Biosynthetic Process | POSITIVELY REGULATES | Peptidoglycan-Based Cell Wall Biogenesis |
| Peptidoglycan-Based Cell Wall Biogenesis | POSITIVELY CORRELATED WITH | Cell Division |
| Cell Division | IN TAXON | Bacteria |
| Bacteria | CAUSES | Aspiration Pneumonia |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB01061#mechanism-of-action](https://go.drugbank.com/drugs/DB01061#mechanism-of-action){:target="_blank"}