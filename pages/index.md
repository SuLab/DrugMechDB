---
title: "Indication Mechanism of Action Database"
sidebar: mydoc_sidebar
permalink: index.html
toc: false 
---

A database of paths that represent the mechanism of action from a drug to a disease in an indication.

> [**Database of mechanism of action paths for selected drug-disease indications**](https://zenodo.org/record/3708278)
<br><Small>Mayers, Michael; Steinecke, Dylan; Su, Andrew I.<small><br>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3708278.svg)](https://doi.org/10.5281/zenodo.3708278)


## Purpose

Most drug mechanisms are described simply as a protein target, or sometimes a pathway, that then treats the disease.
However, there are usually more steps across a biological knowledge graph required to traverse from the target through
its mechanism to the reduction of a disease.  This database attempts to catalog a subset of known drug-disease indications
as a path through a network of biomedical entities.

Below is a visualized example of one entry in DrugMechDB - A path from Cortisone acetate to Keratitis.

![Path Example](path.png)


## Curation

Indications were selected at random from the set contained within DrugCentral. Half were taken from the full set,
representing a set of common drug disease pairs, and the other half were selected from a pool of less-common diseases
to vary the targets and diseases treated.

Paths were derived from free-text descriptions found on DrugBank, Wikipeida and within literature. Concepts within the
text were then normalized to a concept type (Drug, Protein, Pathway, etc) and relationships between the concepts were
determined from the source. Finally concepts were mapped to an identifier depending on the concept type according to
the following table:

|Concept Type | Identifier Source|
|-------------|------------------|
|Anatomy      | UBERON           |
|BiologicalProcess | GO, (MESH)  |
|Cell Type    | CL               |
|Cellular Component | GO         |
|Compound     | MESH, CHEBI      |
|Compound Class | MESH, CHEBI    |
|Disease      | MESH             |
|Drug         | MESH, DrugBank   |
|Molecular Function | GO         |
|Pathway      | REACT            |
|Phenotype    | HP               |
|Protein      | UniProt          |
|Protein Family | InterPro       |
|Taxon        | NCBITaxon        |


## Contributing

If you would like to contribute your own curated mechanistic paths, please do so by making pull requests
with edits to the file `indication_paths.yaml`.

See the [Curation Guide](CurationGuide.md) for more information about contributions.

### Path formatting

Each path begins with a `-   directed: true` statment. Identifiers for concepts and concept type
should conform to the table above.

Paths contain the following structure:

    - directed: true
        graph:
            disease: *name of the disease in the indication*
            disease_mesh: *MESH Identifier for the disease (if known)*
            drug: *name of the drug in the indication*
            drug_mesh: *MESH Identifier for the drug (if known)*
            drugbank: *DrugBank Identifier for the drug (if known)*
        links:     (the edges of the path)
        -   key: *Semantics of the relationship (ALL CAPS)*
            source: *Identifier for source node in edge*
            target: *Identifier for target node in edge*
        nodes:     (the nodes in the path)
        -   id: *Identifier for the node*
            label: *Concept type for the node*
            name: *Name of the node*
        multigraph: true    (required statment for importing paths into networkx).


