---
title: "Troglitazone - Diabetes mellitus type 2"
sidebar: mydoc_sidebar
permalink: troglitazonediabetesmellitustype2.html
toc: false 
---

{% include image.html url="images/troglitazonediabetesmellitustype2.png" file="troglitazonediabetesmellitustype2.png" alt="troglitazonediabetesmellitustype2" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| DB:DB00197 | Troglitazone | Drug |
| HP:0000855 | Insulin resistance | PhenotypicFeature |
| UBERON:0001630 | Muscle | GrossAnatomicalStructure |
| UBERON:0001013 | Adipose tissue | GrossAnatomicalStructure |
| REACT:R-HSA-70263 | Gluconeogenesis | Pathway |
| UBERON:0002107 | Liver | GrossAnatomicalStructure |
| MESH:D001786 | Blood glucose | ChemicalSubstance |
| MESH:D003924 | Diabetes mellitus type 2 | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Troglitazone | NEGATIVELY REGULATES | Insulin Resistance |
| Insulin Resistance | LOCATION OF | Muscle |
| Muscle | PREVENTS | Gluconeogenesis |
| Insulin Resistance | LOCATION OF | Adipose Tissue |
| Adipose Tissue | PREVENTS | Gluconeogenesis |
| Gluconeogenesis | LOCATION OF | Liver |
| Liver | DECREASES ABUNDANCE OF | Blood Glucose |
| Blood Glucose | MANIFESTATION OF | Diabetes Mellitus Type 2 |
|---------|-----------|---------|

Comment: Troglitazone was withdrawn in 2000 due to risk of hepatotoxicity

Reference: [https://go.drugbank.com/drugs/DB00197#mechanism-of-action](https://go.drugbank.com/drugs/DB00197#mechanism-of-action){:target="_blank"}