import json
import os
import traceback
import requests
from time import sleep
from datetime import datetime

MAX_RETRIES = 3
BATCH_SIZE = 5000

def normalize_nodes(session, url, curies_batch, cache, failed_ids):
    """
    Normalize a batch of node CURIEs using the Node Normalization API.

    Parameters:
    - session: requests.Session object for making HTTP requests.
    - url: URL of the Node Normalization API endpoint.
    - curies_batch: List of CURIEs to be normalized.
    - cache: Dictionary to store normalized CURIE mappings.
    - failed_ids: Set to collect CURIEs that failed normalization.
    """
    payload = {
        "curies": curies_batch,
        "conflate": False,
        "description": False,
        "drug_chemical_conflate": False
    }
    retries = 0
    while True:
        try:
            response = session.post(url, json=payload)
            if response.status_code == 200:
                response_text = response.text
                try:
                    response_data = json.loads(response_text)
                except json.JSONDecodeError as e:
                    raise e

                if not isinstance(response_data, dict):
                    raise Exception("Unexpected response data type")

                if not response_data:
                    failed_ids.update(curies_batch)
                    return

                for key, value in response_data.items():
                    if isinstance(value, dict) and isinstance(value.get("id"), dict):
                        cache[key] = value["id"].get("identifier", key)
                    else:
                        failed_ids.add(key)
                return
            elif retries < MAX_RETRIES:
                retries += 1
                sleep(2 ** retries)  # Exponential backoff
            else:
                failed_ids.update(curies_batch)
                break
        except Exception as e:
            traceback.print_exc()
            if retries < MAX_RETRIES:
                retries += 1
                sleep(2 ** retries)
            else:
                failed_ids.update(curies_batch)
                break

def update_graph_links(entry, id_map):
    """
    Update node IDs in the graph and links of an entry using the provided ID map.

    Parameters:
    - entry: A dictionary representing a single data entry with 'graph' and 'links'.
    - id_map: Dictionary mapping original IDs to normalized IDs.
    """
    graph = entry.get('graph', {})
    entry['graph'] = {k: id_map.get(v, v) if isinstance(v, str) else v for k, v in graph.items()}
    entry['links'] = [{
        **link,
        'source': id_map.get(link.get('source'), link.get('source')),
        'target': id_map.get(link.get('target'), link.get('target'))
    } for link in entry.get('links', [])]

def normalize_node_ids(input_file, output_file):
    """
    Normalize node IDs in the input JSON file and write the updated data to the output file.

    Parameters:
    - input_file: Path to the input JSON file containing data entries.
    - output_file: Path to the output JSON file to save normalized data.
    """
    with open(input_file, 'r') as f:
        entries = json.load(f)

    url = "https://nodenorm.transltr.io/1.5/get_normalized_nodes"
    cache_file_path = "./output/norm_cache.json"
    if os.path.exists(cache_file_path):
        with open(cache_file_path, 'r') as f:
            cache = json.load(f)
    else:
        cache = {}
    failed_ids = set()

    all_curies = set()
    for entry in entries:
        for node in entry.get('nodes', []):
            curie = node.get('id', '')
            # Replace prefixes to match expected format
            if curie.startswith('UniProt'):
                curie = curie.replace('UniProt', 'UniProtKB', 1)
            elif curie.startswith('reactome'):
                curie = curie.replace('reactome', 'REACT', 1)
            elif curie.startswith('taxonomy'):
                curie = curie.replace('taxonomy', 'NCBITaxon', 1)
            elif curie.startswith('DB'):
                curie = curie.replace('DB', 'DrugBank', 1)
            # Add CURIE if it contains exactly one colon
            if ':' in curie and len(curie.split(':')) == 2:
                all_curies.add(curie)

    unknown_curies = [curie for curie in all_curies if curie not in cache]
    batches = [unknown_curies[i:i + BATCH_SIZE] for i in range(0, len(unknown_curies), BATCH_SIZE)]

    session = requests.Session()
    for batch in batches:
        normalize_nodes(session, url, batch, cache, failed_ids)

    # Update node IDs in entries using the normalized IDs from cache
    for entry in entries:
        update_graph_links(entry, cache)

    # Write the updated entries to the output file
    with open(output_file, 'w') as f:
        json.dump(entries, f, indent=2)

    # Save the cache to a file
    with open(cache_file_path, 'w') as f:
        json.dump(cache, f, indent=2)

    # Save the list of failed IDs to a file
    failed_ids_path = "./output/failed_ids.json"
    unique_failed_prefixes_path = "./output/unique_failed_prefixes.json"
    with open(failed_ids_path, 'w') as f:
        json.dump(list(failed_ids), f, indent=2)
    # Extract unique prefixes from failed IDs
    unique_prefixes = set(id.split(':')[0] for id in failed_ids)
    with open(unique_failed_prefixes_path, 'w') as f:
        json.dump(list(unique_prefixes), f, indent=2)

    print(f"Total unique normalized IDs: {len(cache)}")
    print(f"Total unique failed IDs: {len(failed_ids)}")

def main():
    normalize_node_ids(
        "./input/indication_paths.json",
        f"./output/indication_paths-{datetime.now().strftime('%Y-%m-%d')}.json"
    )

if __name__ == "__main__":
    main()
