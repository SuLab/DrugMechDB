#Import libraries
import requests

def write_output_file (file, graph_id, node_id, original_name, preferred_name):
    """
    write outputfile
    """
    file.writerow({'graph_id': graph_id, #graph id
                     'node_id': node_id, # node identifier
                     'original_node_name': original_name, #original node name
                     "preferred_node_name":preferred_name}) #prederred node name


def access_MESH_API(node_id): 
    """
    Return preferred name of MESH identifiers
    """
    
    session = requests.Session()
    node_id = node_id.strip("MESH:")
    
    api_access = f"https://id.nlm.nih.gov/mesh/lookup/details?descriptor={node_id}"
    #print(api_access)
    
    with session.get(api_access) as res:

        res = res.json()
        preferred_name =  [term["label"] for term in res["terms"]if term["preferred"] == True] 
        
        
        return (preferred_name[0])

def access_GO_API(node_id): 
    """
    Return preferred name of GO identifiers
    """
    session = requests.Session()
    api_access = f"http://api.geneontology.org/api/ontology/term/{node_id}"
    #print(api_access)
    
    with session.get(api_access) as res:
        res = res.json()
        preferred_name = res["label"]
        
        return preferred_name

def access_UniProt_API(node_id): 
    """
    Return preferred name of UniProt identifiers
    """
    session = requests.Session()
    node_id = node_id.strip("UniProt:")
    
    try: 
        api_access = f"https://www.ebi.ac.uk/proteins/api/proteins/P{node_id}"
        #print(api_access)

        with session.get(api_access) as res:
            res = res.json()

            try: 
                preferred_name = res["protein"]["recommendedName"]["fullName"]["value"]
            except: 
                preferred_name = res["protein"]["recommendedName"]["shortName"]["value"]

            return preferred_name
    except:
        api_access = f"https://www.ebi.ac.uk/proteins/api/proteins/{node_id}"
        #print(api_access)
        with session.get(api_access) as res:
            res = res.json()

            try: 
                preferred_name = res["protein"]["recommendedName"]["fullName"]["value"]
            except: 
                preferred_name = res["protein"]["recommendedName"]["shortName"]["value"]

            return preferred_name

def access_nodenormalizer_API(node_id): 
    """
   Return preferred name of HP,NCBITaxon, UBERON,REACT, PR identifiers
    """
    session = requests.Session()
    prefix = node_id.split(":")[0]
    _id = node_id.split(":")[1]
    api_access = f"https://nodenormalization-sri.renci.org/1.3/get_normalized_nodes?curie={prefix}%3A{_id}&conflate=true"
    #print(api_access)
    
    with requests.get(api_access) as res:
        res = res.json()
        preferred_name = res[node_id]["id"]["label"]
        
        return preferred_name

def access_mychem_API(node_id):
    """
    Return preferred name of CHEBI
    """
    session = requests.Session()
    api_access = f"http://mychem.info/v1/chem/{node_id}"
    #print(api_access)
    
    with requests.get(api_access) as res:
        res = res.json()
        try:
            preferred_name = (res["chebi"]["name"])
            return preferred_name
        
        except:
            preferred_name = (res["aeolus"]["drug_name"])
            return preferred_name
            

def access_interpro_API(node_id):
    """
    Return preferred name of InterPro
    """
    
    node_id = node_id.strip("InterPro:IPR")
    session = requests.Session()
    api_access = f"https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/ipr{node_id}"

    with requests.get(api_access) as res:
        res = res.json()
        preferred_name = res["results"][0]["metadata"]["name"]
        
        return preferred_name

def access_pfam_API(node_id):
    """
    Return preferred name of Pfam
    """
    
    node_id = node_id.strip("Pfam:")
    session = requests.Session()
    api_access = f"https://www.ebi.ac.uk/interpro/api/entry/pfam/pf{node_id}"

    with requests.get(api_access) as res:
        res = res.json()
        preferred_name = res["metadata"]["name"]["name"]
        
        return preferred_name