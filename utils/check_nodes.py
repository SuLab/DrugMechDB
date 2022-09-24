import pandas as pd
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
    log_file = []

    # Open original indication_paths.yml file
    with open("./../indication_paths.yaml", "r") as indication_paths:
        paths = yaml.load(indication_paths, Loader=yaml.BaseLoader)
        # Loop for each item in list 
        for directed in paths:
            directed.update({"directed" : True})
            directed.update({"multigraph" : True})
            
            # Filters through nodes to only get MeSH IDs
            nodes = directed["nodes"]
            nodes = list(filter(lambda node: node["id"].startswith("MESH:"), nodes))

            # For loop against MeSH node IDs
            for node in nodes:
                time.sleep(0.1)

                # Skipping duplicates
                if node["id"] in nodes_:
                    continue

                # GET Request on NIH API to gather more information on MeSH ID
                with session.get("https://id.nlm.nih.gov/mesh/lookup/details?descriptor={}".format(node["id"][5:])) as res:
                    res = res.json()
                    preferred = list(filter(lambda term: term["preferred"], res["terms"]))
                    mesh.append({"node" : res["descriptor"].removeprefix("http://id.nlm.nih.gov/mesh/"), "name" : preferred[0]["label"] if preferred else None})

            for node in directed["nodes"]:
                # Append data to list for log file
                log_ = []
                log_.append(directed["graph"]["_id"])
                log_.append(node["id"])
                log_.append(node["name"])

                # Find the node which is equal to the node we found the updated name for
                names = list(filter(lambda m: m["node"] == node["id"][5:], mesh))
                if names:
                    log_.append(names[0]["name"])
                    node.update({ "name" : names[0]["name"] })
                else:
                    log_.append(None)

                if log_[1].startswith("MESH:"):
                    log_file.append(log_)

            indication_paths_updated.append(directed)

    # Create log file from log_file list
    log_file_ = pd.DataFrame(log_file)
    log_file_.to_csv("log_file.csv", sep="\t", index=False, header=["graph._id", "node.id", "node.name (original)", "node.name (new)"])

    # Create new indication_paths.yml file with updated names
    with open("./../indication_paths.yaml", "w") as u:
        yaml.dump(indication_paths_updated, stream=u, indent=4, default_flow_style=False)

    end = time.time()
    print(f"Finished in {(end - start)/60} minutes.")

if __name__ == "__main__":
    main()