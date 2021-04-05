---
title: "Aztreonam - Rhinoscleroma"
sidebar: mydoc_sidebar
permalink: aztreonamrhinoscleroma.html
toc: false 
---

{% include image.html url="images/aztreonamrhinoscleroma.png" file="aztreonamrhinoscleroma.png" alt="aztreonamrhinoscleroma" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D001398 | Aztreonam | Drug |
| UniProt:A0A3Q9U7L4 | Penicillin binding protein 3 | Protein |
| GO:0018104 | Peptidoglycan-protein cross-linking | BiologicalProcess |
| GO:0042546 | Cell wall biogenesis | BiologicalProcess |
| InterPro:IPR033907 | Autolysins | GeneFamily |
| GO:0019835 | Cytolysis | BiologicalProcess |
| GO:0008219 | Cell death | BiologicalProcess |
| NCBITaxon:39831 | Klebsiella rhinoscleromatis | OrganismTaxon |
| MESH:D012226 | Rhinoscleroma | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Aztreonam | DECREASES ACTIVITY OF | Penicillin Binding Protein 3 |
| Penicillin Binding Protein 3 | NEGATIVELY REGULATES | Peptidoglycan-Protein Cross-Linking |
| Peptidoglycan-Protein Cross-Linking | DISRUPTS | Cell Wall Biogenesis |
| Cell Wall Biogenesis | CONTRIBUTES TO | Cell Death |
| Aztreonam | INCREASES ABUNDANCE OF | Autolysins |
| Autolysins | CAUSES | Cytolysis |
| Cytolysis | IN TAXON | Klebsiella Rhinoscleromatis |
| Cell Death | IN TAXON | Klebsiella Rhinoscleromatis |
| Klebsiella Rhinoscleromatis | CAUSES | Rhinoscleroma |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00355#mechanism-of-action](https://go.drugbank.com/drugs/DB00355#mechanism-of-action){:target="_blank"}