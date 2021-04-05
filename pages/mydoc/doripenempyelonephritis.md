---
title: "Doripenem - Pyelonephritis"
sidebar: mydoc_sidebar
permalink: doripenempyelonephritis.html
toc: false 
---

{% include image.html url="images/doripenempyelonephritis.png" file="doripenempyelonephritis.png" alt="doripenempyelonephritis" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:C099245 | Doripenem | Drug |
| InterPro:IPR001460 | Penicillin-binding protein, transpeptidase | GeneFamily |
| GO:0018104 | Cross-linking of the peptidoglycan | BiologicalProcess |
| GO:0009273 | Peptidoglycan-based cell wall biogenesis | BiologicalProcess |
| GO:0005618 | Cell wall | CellularComponent |
| NCBITaxon:562 | Escherichia coli | OrganismTaxon |
| MESH:D011704 | Pyelonephritis | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Doripenem | DECREASES ACTIVITY OF | Penicillin-Binding Protein, Transpeptidase |
| Penicillin-Binding Protein, Transpeptidase | POSITIVELY REGULATES | Cross-Linking Of The Peptidoglycan |
| Cross-Linking Of The Peptidoglycan | POSITIVELY REGULATES | Peptidoglycan-Based Cell Wall Biogenesis |
| Peptidoglycan-Based Cell Wall Biogenesis | HAS OUTPUT | Cell Wall |
| Cell Wall | OCCURS IN | Escherichia Coli |
| Escherichia Coli | CAUSES | Pyelonephritis |
|---------|-----------|---------|

Comment: The FDA revised the doripenem label in 2014 to include a warning against use in ventilator-associated pneumonia and to reiterate its safety and efficacy for its approved indications.

Reference: [https://go.drugbank.com/drugs/DB06211#mechanism-of-action](https://go.drugbank.com/drugs/DB06211#mechanism-of-action){:target="_blank"}