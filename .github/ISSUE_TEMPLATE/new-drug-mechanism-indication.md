---
name: New drug mechanism indication
about: The simplest way to suggest a new entry for DrugMechDB
title: "[ADDITION]"
labels: ''
assignees: ''

---

Great, you'd like to suggest a new entry in DrugMechDB.  Thank you!

First, two quick notes: 
* If you are familiar with GitHub pull requests, please submit a pull request on [indication_paths.yaml](https://github.com/SuLab/DrugMechDB/blob/master/indication_paths.yaml)
* If you don't know _all_ the information requested below, just fill in as much as you do know

A new Drug Mechanism is composed of nodes and edges.  The nodes are the biomedical entities (genes, diseases, complexes, pathways, etc.), and the edges are the relationships between those nodes.  The starting node will always be a drug, and ending node will always be a disease.  **For example, the mechanism for acetaminophen's mechanism of action in treating pain would look like this**:

Node 1:
- name: acetaminophen
- id: MESH:D000082
- type: Drug
        
Edge 1-2
- relation: INHIBITS

Node 2:
- name: Cox-1
- id: UniProt:P23219
- type: Protein

Edge 2-3
- relation: PRODUCES

Node 3:
- name: Prostaglandins
- id: MESH:D011453
- type: Compound Class
        
Edge 3-4
- relation: CAUSES

Node 4:
- name: Pain
- id: MESH:D010146
- type: Disease

Following that example, please fill out the template below.

----- PLEASE DELETE EVERYTHING ABOVE THIS LINE PRIOR TO SUBMITTING -----

Node 1
- name: 
- id: 
- type: drug

Edge 1-2
- relation: 

Node 2
- name: 
- id: 
- type: 

[add more nodes and edges, as needed]
