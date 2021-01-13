# Curation Guide

## Record Composition

Each record in DrugMechDB is a directed [graph](https://en.wikipedia.org/wiki/Graph_theory) consisting of the concepts
and relationships (aka nodes and edges) that connect a Drug in an indication to its treated Disease. The majority of
records are a [path](https://en.wikipedia.org/wiki/Path_(graph_theory)), consisting of a singular sequence of steps from
Drug to Disease.

Concepts of within DrugMechDB are mapped to universal identifiers as well as a [concept type](#concept-types).
Relationships are mapped to [relationship types](#relationships). These facets function to enhance the
machine-readability and reusability of the data contained within DrugMechDB.

An example of a record is illustrated below.

![Path](path.png)

### Branching Paths

Some drugs produce their treatment effects through multiple interactions occurring simultaneously. This may
include the inhibition multiple targets that combine to produce their effect, or acting on multiple unrelated pathways
that acting on them individually would not have an affect on the disease. This situation can be represented through
a branching path, a simple example of which is pictured below.

![Branch Path](branch.png)

If a branching path is used it should be because *multiple actions are converging to produce a given result*. This is in contrast
to multiple different expressions with equivalent meaning. For example, substituting 3 protein-to-compound interactions with
the one representation of pathway they belong to would not constitute a branched path, but rather equivalent expressions,
where only one should be selected.

### Format

YAML was chosen as a human friendly serialization standard for the content of DrugMechDB. YAML meets the primary
goal of machine readability and human-interoperability, important for the process of expert curation.
[For more information on the YAML standard, please follow this link](https://yaml.org/).

See [this sample](sample.yaml) for an example record, properly formatted in YAML.

### Components

Each record contains several components to produce a graph that is able to be consumed by programming languages
like Python, listed below. The following keys are required for a record (with more information on each provided below):
`directed`, `graph`, `links`, `nodes`, `multigraph`, and `reference`.

#### Graph

Information about the indication for this record. Includes the drug and disease names and their identifiers.

Example:

    graph:
        disease: Keratitis
        disease_mesh: MESH:D007634
        drug: cortisone acetate
        drug_mesh: MESH:D003348
        drugbank: DB01380

#### Links

The relationships (or edges) in the graph. Each link contains a the identifiers for the `source` and `target` concepts in the
relationship as well as a `key` field for the [relationship type](#relationships). Links are ordered from
first link in the path with
`source` being the Drug in the indication and the final link's `target` being the Disease in the indication.

Example:

    links:
    -   key: increases activity of
        source: MESH:D003348
        target: UniProt:P04150
    -   key: negatively regulates
        source: UniProt:P04150
        target: UniProt:P23219
    -   key: increases abundance of
        source: UniProt:P23219
        target: MESH:D011453
    -   key: located in
        source: MESH:D011453
        target: GO:0006954
    -   key: causes
        source: GO:0006954
        target: MESH:D007634


#### Nodes

Nodes contain information on each of the concepts in the graph. Each node contains the fields `id`, `name`, and `label`
corresponding to the external identifier, the name of the concept, and they type of concept respectively. Each node `id`
must EXACTLY MATCH the identifiers used in the `source` and `target` fields for [links](#links). All identifiers used in the
links section must be included in the nodes section.

`id` is the most important field and has a few additional requirements. Each node should have a **single** identifier.
Ids must be preceded by the [CURIE](http://dragoman.org/comuri.html) for the source of
the identifier (For example `MESH:` for MeSH identifiers, or `UniProt:` for those from Uniprot).
One important caveat is that <code>: </code> (colon space) is a reserved character-set in YAML, so
identifiers must not contain  spaces. For example `MESH:D007249` is correct, but `MESH: D007249` will
produce an error and should not be used.

See the [Concept types](#concept-types) section for preferred identifier sources.

Alternate identifiers from non-preferred sources may be included as a list in an optional `alt_ids` field:

    nodes:
    -   id: MESH:D003348
        label: Drug
        name: cortisone acetate
    -   id: UniProt:P04150
        label: Protein
        name: Glucocorticoid receptor
    -   id: UniProt:P23219
        label: Protein
        name: COX genes
    -   id: MESH:D011453
        label: ChemicalSubstance
        name: Prostaglandins
    -   id: GO:0006954
        label: BiologicalProcess
        name: Inflammation
        alt_ids:
        - MESH:D007249
        - KEGG:hsa04062
    -   id: MESH:D007634
        label: Disease
        name: Keratitis

#### Reference

Each record is to be annotated with a `reference` key linking to the data source where the record was curated from.

Example:

    reference: https://go.drugbank.com/drugs/DB01380#mechanism-of-action
    
#### Additional keys

To aid in machine readability two additional keys are required, `multigraph` and `directed` both being set to `true`.

Example:
    
    -   directed: true
        multigraph: true

    
## Sources

Records from DrugMechDB should be curated from secondary sources. The primary source for curation is the
Mechanism of Action section from [DrugBank](https://go.drugbank.com/drugs/DB01380#mechanism-of-action) for
the drug in the indication.

Other acceptable sources include (but are not limited to) Review articles, Gene Ontology, UniProt, Reactome, and
well-sourced Wikipedia articles.

Primary sources, including manuscripts containing experimental results should **not** be used
for sources in DrugMechDB. DrugMechDB should consist of highly curated and high-confidence data, therefore sources
curated to produce new records should already contain a level of curation.

Finally, there may be many relationships within the source text. Only those relevant to the disease in the indication
should be represented in the record's final path.


## Data Model

The data model used for concepts and relationships in the curated records is derived from the
 [Biolink data model](https://biolink.github.io/biolink-model/). Only a subset of Biolink is used, with concepts and
 relationship vocabulary relevant biochemical interactions and disease processes. Please see below for preferred
 concept and relationship types.

### Concept Types

Concepts are limited to the following vocabulary. The preferred identifiers are listed below. In the event that an identifier
from one of these sources cannot be found for a concept, identifiers listed on the Biolink page for the concept type
(linked below) may be used, in order of preference as they appear on the page.

|Concept Type                                                    | Identifier Source    |
|-----------------------------------------------------------------------------------------------------|--------------------------|
|[BiologicalProcess](https://biolink.github.io/biolink-model/docs/BiologicalProcess.html)  |  [GO](http://geneontology.org/)  |
|[Cell](https://biolink.github.io/biolink-model/docs/Cell.html)  |  [CL](http://www.obofoundry.org/ontology/cl.html) |
|[CellularComponent](https://biolink.github.io/biolink-model/docs/CellularComponent.html)  |  [GO](http://geneontology.org/)  |
|[ChemicalSubstance](https://biolink.github.io/biolink-model/docs/ChemicalSubstance.html)  |  [MESH](https://meshb.nlm.nih.gov/), [CHEBI](https://www.ebi.ac.uk/chebi/) |
|[Disease](https://biolink.github.io/biolink-model/docs/Disease.html)  |  [MESH](https://meshb.nlm.nih.gov/)  |
|[Drug](https://biolink.github.io/biolink-model/docs/Drug.html)  |  [MESH](https://meshb.nlm.nih.gov/), [DrugBank](https://go.drugbank.com/) |
|[GeneFamily](https://biolink.github.io/biolink-model/docs/GeneFamily.html)  |  [InterPro](https://www.ebi.ac.uk/interpro/) |
|[GrossAnatomicalStructure](https://biolink.github.io/biolink-model/docs/GrossAnatomicalStructure.html)  |  [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon)  |
|[MolecularActivity](https://biolink.github.io/biolink-model/docs/MolecularActivity.html)  |  [GO](http://geneontology.org/)  |
|[OrganismTaxon](https://biolink.github.io/biolink-model/docs/OrganismTaxon.html)  |  [NCBITaxon](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi)  |
|[Pathway](https://biolink.github.io/biolink-model/docs/Pathway.html)  |  [REACT](https://reactome.org/)  |
|[PhenotypicFeature](https://biolink.github.io/biolink-model/docs/PhenotypicFeature.html)  |  [HP](https://hpo.jax.org/app/)  |
|[Protein](https://biolink.github.io/biolink-model/docs/Protein.html)  |  [UniProt](https://www.uniprot.org/)  |


### Relationships

DrugMechDB currently uses a **limited subset** of the available predicates in the Biolink Data Model.

Unlike the concept types, this is not a hard limit on relationships. While ideally most relationships should be mapped
to one of the predicates previously used, if a relationship found in the process of curation does not fit neatly into
any of these types listed below, a predicate may be selected
from the [full set of biolink predicates](https://biolink.github.io/biolink-model/docs/predicates.html).

The predicates currently found within DrugMechDB are as follows:

[affects risk for](https://biolink.github.io/biolink-model/docs/affects_risk_for.html)  
[capable of](https://biolink.github.io/biolink-model/docs/capable_of.html)  
[caused by](https://biolink.github.io/biolink-model/docs/caused_by.html)  
[causes](https://biolink.github.io/biolink-model/docs/causes.html)  
[contributes to](https://biolink.github.io/biolink-model/docs/contributes_to.html)  
[correlated with](https://biolink.github.io/biolink-model/docs/correlated_with.html)  
[decreases abundance of](https://biolink.github.io/biolink-model/docs/decreases_abundance_of.html)  
[decreases activity of](https://biolink.github.io/biolink-model/docs/decreases_activity_of.html)  
[disrupts](https://biolink.github.io/biolink-model/docs/disrupts.html)  
[expressed in](https://biolink.github.io/biolink-model/docs/expressed_in.html)  
[expresses](https://biolink.github.io/biolink-model/docs/expresses.html)  
[has output](https://biolink.github.io/biolink-model/docs/has_output.html)  
[has participant](https://biolink.github.io/biolink-model/docs/has_participant.html)  
[has phenotype](https://biolink.github.io/biolink-model/docs/has_phenotype.html)  
[in taxon](https://biolink.github.io/biolink-model/docs/in_taxon.html)  
[increases abundance of](https://biolink.github.io/biolink-model/docs/increases_abundance_of.html)  
[increases activity of](https://biolink.github.io/biolink-model/docs/increases_activity_of.html)  
[located in](https://biolink.github.io/biolink-model/docs/located_in.html)  
[location of](https://biolink.github.io/biolink-model/docs/location_of.html)  
[manifestation of](https://biolink.github.io/biolink-model/docs/manifestation_of.html)  
[molecularly interacts with](https://biolink.github.io/biolink-model/docs/molecularly_interacts_with.html)  
[negatively correlated with](https://biolink.github.io/biolink-model/docs/negatively_correlated_with.html)  
[negatively regulates](https://biolink.github.io/biolink-model/docs/negatively_regulates.html)  
[occurs in](https://biolink.github.io/biolink-model/docs/occurs_in.html)  
[part of](https://biolink.github.io/biolink-model/docs/part_of.html)  
[participates in](https://biolink.github.io/biolink-model/docs/participates_in.html)  
[positively correlated with](https://biolink.github.io/biolink-model/docs/positively_correlated_with.html)  
[positively regulates](https://biolink.github.io/biolink-model/docs/positively_regulates.html)  
[precedes](https://biolink.github.io/biolink-model/docs/precedes.html)  
[prevents](https://biolink.github.io/biolink-model/docs/prevents.html)  
[produced by](https://biolink.github.io/biolink-model/docs/produced_by.html)  
[produces](https://biolink.github.io/biolink-model/docs/produces.html)  
[regulates](https://biolink.github.io/biolink-model/docs/regulates.html)  
[treats](https://biolink.github.io/biolink-model/docs/treats.html)  


## FAQ

TBD


