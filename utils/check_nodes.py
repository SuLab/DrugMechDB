import requests
import yaml
import time

def main():
    start = time.time()

    # Define requests.Session
    session = requests.Session()
    session.headers.update({"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"})

    # Define lists used to gather data
    mesh = []
    nodes_ = []
    indication_paths_updated = []

    # Open original indication_paths.yml file
    with open("./../indication_paths.yaml", "r") as indication_paths:
        paths = yaml.load(indication_paths, Loader=yaml.CBaseLoader)
        # Loop for each item in list 
        for directed in paths:
            # Filters through nodes to only get MeSH IDs
            nodes = directed["nodes"]
            nodes = list(filter(lambda node: node["id"].startswith("MESH:"), nodes))

            # For loop against MeSH node IDs
            for node in nodes:
                time.sleep(0.05)

                # Skipping duplicates
                if node["id"] in nodes_:
                    continue

                # GET Request on NIH API to gather more information on MeSH ID
                with session.get("https://id.nlm.nih.gov/mesh/lookup/details?descriptor={}".format(node["id"][5:])) as res:
                    res = res.json()
                    preferred = list(filter(lambda term: term["preferred"], res["terms"]))
                    mesh.append({"node" : res["descriptor"].removeprefix("http://id.nlm.nih.gov/mesh/"), "label" : preferred[0]["label"] if preferred else None})

                nodes_.append(node["id"])

            for node in directed["nodes"]:
                # Find the node which is equal to the node we found the label for
                labels = list(filter(lambda m: m["node"] == node["id"][5:], mesh))
                if labels:
                    node.update({ "label" : labels[0]["label"] })

            indication_paths_updated.append(directed)

    # Create new indication_paths.yml file with updated labels
    with open("./../indication_paths.yaml", "w") as u:
        data = yaml.dump(indication_paths_updated, u)

    end = time.time()
    print(f"Finished in {(end - start)/60} minutes.")

if __name__ == "__main__":
    main()