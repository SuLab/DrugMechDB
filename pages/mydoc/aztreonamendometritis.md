---
title: "Aztreonam - Endometritis"
sidebar: mydoc_sidebar
permalink: aztreonamendometritis.html
toc: false 
---

{% include image.html url="images/aztreonamendometritis.png" file="aztreonamendometritis.png" alt="aztreonamendometritis" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D001398 | Aztreonam | Drug |
| UniProt:A0A0H2X0X9 | Penicillin binding protein 3 | Protein |
| GO:0018104 | Peptidoglycan-protein cross-linking | BiologicalProcess |
| GO:0042546 | Cell wall biogenesis | BiologicalProcess |
| InterPro:IPR033907 | Autolysins | GeneFamily |
| GO:0019835 | Cytolysis | BiologicalProcess |
| GO:0008219 | Cell death | BiologicalProcess |
| NCBITaxon:813 | Chlamydia trachomatis | OrganismTaxon |
| MESH:D004716 | Endometritis | Disease |
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
| Cytolysis | IN TAXON | Chlamydia Trachomatis |
| Cell Death | IN TAXON | Chlamydia Trachomatis |
| Chlamydia Trachomatis | CAUSES | Endometritis |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00355#mechanism-of-action](https://go.drugbank.com/drugs/DB00355#mechanism-of-action){:target="_blank"}