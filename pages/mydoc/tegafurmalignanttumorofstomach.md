---
title: "Tegafur - Malignant tumor of stomach"
sidebar: mydoc_sidebar
permalink: tegafurmalignanttumorofstomach.html
toc: false 
---

{% include image.html url="images/tegafurmalignanttumorofstomach.png" file="tegafurmalignanttumorofstomach.png" alt="tegafurmalignanttumorofstomach" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D005641 | Tegafur | Drug |
| InterPro:IPR001128 | cytochrome P-450 | GeneFamily |
| MESH:D005472 | 5-fluorouracil | ChemicalSubstance |
| MESH:D005468 | 5-fluoro-2-deoxyuridine monophosphate | ChemicalSubstance |
| MESH:C025635 | 5-fluorouridine triphosphate | ChemicalSubstance |
| UniProt:P04818 | Thymidylate synthase | Protein |
| GO:0071897 | DNA synthesis | BiologicalProcess |
| GO:0032774 | RNA synthesis | BiologicalProcess |
| GO:0006412 | Protein synthesis | BiologicalProcess |
| CL:0001063 | tumor cell | Cell |
| MESH:D013274 | Malignant tumor of stomach | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Tegafur | INCREASES ACTIVITY OF | Cytochrome P-450 |
| Cytochrome P-450 | INCREASES ABUNDANCE OF | 5-Fluorouracil |
| 5-Fluorouracil | HAS METABOLITE | 5-Fluoro-2-Deoxyuridine Monophosphate |
| 5-Fluorouracil | HAS METABOLITE | 5-Fluorouridine Triphosphate |
| 5-Fluorouridine Triphosphate | NEGATIVELY REGULATES | Rna Synthesis |
| 5-Fluorouridine Triphosphate | NEGATIVELY REGULATES | Protein Synthesis |
| 5-Fluoro-2-Deoxyuridine Monophosphate | DECREASES ACTIVITY OF | Thymidylate Synthase |
| Thymidylate Synthase | NEGATIVELY REGULATES | Dna Synthesis |
| Dna Synthesis | LOCATED IN | Tumor Cell |
| Rna Synthesis | LOCATED IN | Tumor Cell |
| Protein Synthesis | LOCATED IN | Tumor Cell |
| Tumor Cell | CONTRIBUTES TO | Malignant Tumor Of Stomach |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB09256#mechanism-of-action](https://go.drugbank.com/drugs/DB09256#mechanism-of-action){:target="_blank"}