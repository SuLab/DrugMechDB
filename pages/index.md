---
title: "Indication Mechanism of Action Database"
sidebar: mydoc_sidebar
permalink: index.html
toc: false 
---

**DrugMechDB** is a curated database that captures mechanistic paths from a drug to a disease within a given indication. DrugMechDB provides:
- Mechanistic paths from drug to disease via biological entities.
- Expert curation of relationships supported by literature.
- Graph-based representation of mechanisms suitable for computational analysis.
- DrugMechDB leverages the [**Biolink Model**](https://biolink.github.io/biolink-model/) to ensure semantic interoperability and consistency across biomedical entities and relationships.
  
## 🔗 Resources

- **Latest Release:**  
  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8139357.svg)](https://doi.org/10.5281/zenodo.8139357)

- **Publication:**  
  *Gonzalez-Cavazos, A. C., Tanska, A., Mayers, M., Carvalho-Silva, D., Sridharan, B., Rewers, P. A., Sankarlal, U., Jagannathan, L., & Su, A. I. (2023). DrugMechDB: a curated database of drug mechanisms*
  [Read the paper on Scientific Data](https://www.nature.com/articles/s41597-023-02534-z)

- **Web Interface:**  
  Explore DrugMechDB online: [https://sulab.github.io/DrugMechDB/](https://sulab.github.io/DrugMechDB/)

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

Paths were derived from free-text descriptions found on DrugBank, Wikipedia and within literature. Concepts within the
text were then normalized to a concept type (Drug, Protein, Pathway, etc) and relationships between the concepts were
determined from the source. Finally concepts were mapped to an identifier depending on the concept type according to
the following table:

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
|[MacromolecularComplex](https://biolink.github.io/biolink-model/docs/MacromolecularComplexMixin.html)  |  [PR](https://www.ebi.ac.uk/ols/ontologies/pr)  |
|[MolecularActivity](https://biolink.github.io/biolink-model/docs/MolecularActivity.html)  |  [GO](http://geneontology.org/)  |
|[OrganismTaxon](https://biolink.github.io/biolink-model/docs/OrganismTaxon.html)  |  [NCBITaxon](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi)  |
|[Pathway](https://biolink.github.io/biolink-model/docs/Pathway.html)  |  [REACT](https://reactome.org/)  |
|[PhenotypicFeature](https://biolink.github.io/biolink-model/docs/PhenotypicFeature.html)  |  [HP](https://hpo.jax.org/app/)  |
|[Protein](https://biolink.github.io/biolink-model/docs/Protein.html)  |  [UniProt](https://www.uniprot.org/)  |


## Contributing

If you would like to contribute your own curated mechanistic paths, please do so by making pull requests
with edits to the file `submission.yaml`.

See the [Curation Guide](CurationGuide.md) for more information about contributions and [Submission Guide](SubmissionGuide.md) for
detailed submission instructions.

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


## Website build guide

We originally had this configured so that the ["Update Website" action](https://github.com/SuLab/DrugMechDB/actions/workflows/update-website.yaml) would build the Jekyll files and push to the `gh-pages` branch, which would then be rendered by Github Pages.  However, the web content is now too large and the build process times out.  Therefore, we have to build locally.  The protocol is as follows:
    
* **Execute the ["Merge Pages" action](https://github.com/SuLab/DrugMechDB/actions/workflows/merge-pages.yaml)** which will merge the `main` branch to `gh-pages`
* **Create the `gh-pages` branch locally**
    
    ```
    git clone --branch gh-pages --depth 1 git@github.com:SuLab/DrugMechDB.git DrugMechDB.gh-pages
    cd DrugMechDB.gh-pages
    ``` 
    
    or if the repo already exists locally, 
    ```
    cd DrugMechDB.gh-pages
    git pull
    ```
* **Create the Jekyll files from `indication_paths.yaml`**
    
    ```
    python parse.py
    ```
* **Use jekyll to render HTML output**: 
    
    This command can take up to ~30 mins to complete, and output HTML files will be in `_site`
    ```
    bundle exec jekyll build
    ```
* **Create the `gh-pages-html` branch locally**: 
    
    ```
    cd ..
    git clone --branch gh-pages-html git@github.com:SuLab/DrugMechDB.git DrugMechDB.gh-pages-html
    cd DrugMechDB.gh-pages-html
    ``` 
    or if the repo already exists locally, 
    
    ```
    cd DrugMechDB.gh-pages-html
    git pull
    ```
* **Copy the new rendered files**: 
    
    ```
    rm -rf *
    cp -r ../DrugMechDB.gh-pages/_site/* .
    ```
* **Commit and push**: 
    
    ```
    git add .
    git commit -m 'Update website'
    git push
    ```


### To cite the use of DrugMechDB in your work
```
Gonzalez-Cavazos, A. C., Tanska, A., Mayers, M., Carvalho-Silva, D., Sridharan, B., Rewers, P. A., Sankarlal, U., Jagannathan, L. & Su, A. I. (2023). DrugMechDB: A Curated Database of Drug Mechanisms. Scientific Data, 10(1), 632.
```
