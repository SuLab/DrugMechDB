---
title: "Tramadol - Pain"
sidebar: mydoc_sidebar
permalink: tramadolpain2.html
toc: false 
---

{% include image.html url="images/tramadolpain2.png" file="tramadolpain2.png" alt="tramadolpain2" %}

## Concepts

|------------|------|---------|
| Identifier | Name | Type    |
|------------|------|---------|
| MESH:D014147 | Tramadol | Drug |
| UniProt:P35372 | Mu-type opioid receptor | Protein |
| UniProt:B7Z2C7 | Adenylate cyclase | Protein |
| UniProt:Q14654 | ATP-sensitive inward rectifier potassium channel 11 | Protein |
| GO:0070509 | Transmembrane calcium influx | BiologicalProcess |
| GO:1990793 | Substance P secretion, neurotransmission | BiologicalProcess |
| GO:0061535 | Glutamate secretion, neurotransmission | BiologicalProcess |
| GO:0099610 | Action potential initiation | BiologicalProcess |
| CL:0000198 | Nociceptor | Cell |
| UniProt:P23975 | Sodium-dependent noradrenaline transporter | Protein |
| GO:0051620 | Noradrenaline uptake | BiologicalProcess |
| MESH:D009638 | Noradrenaline | ChemicalSubstance |
| GO:0061533 | Norepinephrine secretion, neurotransmission | BiologicalProcess |
| UniProt:P31645 | Sodium-dependent serotonin transporter | Protein |
| GO:0051610 | Serotonin uptake | BiologicalProcess |
| MESH:D012701 | Serotonin | ChemicalSubstance |
| GO:0060096 | Serotonin secretion, neurotransmission | BiologicalProcess |
| GO:0019233 | Sensory perception of pain | BiologicalProcess |
| MESH:D010146 | Pain | Disease |
|------------|------|---------|

## Relationships

|---------|-----------|---------|
| Subject | Predicate | Object  |
|---------|-----------|---------|
| Tramadol | INCREASES ACTIVITY OF | Mu-Type Opioid Receptor |
| Tramadol | DECREASES ACTIVITY OF | Sodium-Dependent Noradrenaline Transporter |
| Tramadol | DECREASES ACTIVITY OF | Sodium-Dependent Serotonin Transporter |
| Sodium-Dependent Serotonin Transporter | PARTICIPATES IN | Serotonin Uptake |
| Sodium-Dependent Noradrenaline Transporter | PARTICIPATES IN | Noradrenaline Uptake |
| Noradrenaline Uptake | DECREASES ABUNDANCE OF | Noradrenaline |
| Serotonin Uptake | DECREASES ABUNDANCE OF | Serotonin |
| Serotonin | POSITIVELY CORRELATED WITH | Serotonin Secretion, Neurotransmission |
| Noradrenaline | POSITIVELY CORRELATED WITH | Norepinephrine Secretion, Neurotransmission |
| Serotonin Secretion, Neurotransmission | NEGATIVELY REGULATES | Sensory Perception Of Pain |
| Norepinephrine Secretion, Neurotransmission | NEGATIVELY REGULATES | Sensory Perception Of Pain |
| Sensory Perception Of Pain | CAUSES | Pain |
| Mu-Type Opioid Receptor | DECREASES ACTIVITY OF | Adenylate Cyclase |
| Adenylate Cyclase | DECREASES ACTIVITY OF | Atp-Sensitive Inward Rectifier Potassium Channel 11 |
| Mu-Type Opioid Receptor | NEGATIVELY REGULATES | Transmembrane Calcium Influx |
| Atp-Sensitive Inward Rectifier Potassium Channel 11 | NEGATIVELY REGULATES | Action Potential Initiation |
| Transmembrane Calcium Influx | POSITIVELY REGULATES | Substance P Secretion, Neurotransmission |
| Transmembrane Calcium Influx | POSITIVELY REGULATES | Glutamate Secretion, Neurotransmission |
| Substance P Secretion, Neurotransmission | POSITIVELY CORRELATED WITH | Pain |
| Glutamate Secretion, Neurotransmission | POSITIVELY CORRELATED WITH | Pain |
| Action Potential Initiation | POSITIVELY REGULATES | Nociceptor |
| Nociceptor | POSITIVELY CORRELATED WITH | Pain |
|---------|-----------|---------|

Reference: [https://go.drugbank.com/drugs/DB00193#mechanism-of-action](https://go.drugbank.com/drugs/DB00193#mechanism-of-action){:target="_blank"}