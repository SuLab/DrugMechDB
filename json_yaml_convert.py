import yaml
import argparse
import simplejson


def read_json(f_name):
    """
    Read the DrugMechDB paths from a .json file

    :param filename: str, the path to the json file to be read

    :return: dict, the paths as a dictionary object.
    """
    with open(filename, 'r') as f_in:
        G = simplejson.load(f_in)
    return G


def write_json(G, outname):
    """
    Write the DrugMechDB paths out to a .json file

    :param G: dict, the DrugMechDB paths as a dictionary object
    :param outname: the path to write the json output file
    """

    with open(outname, 'w') as fout:
        simplejson.dump(G, fout, indent=2, ignore_nan=True)


def read_yaml(f_name):
    """
    Read the DrugMechDB paths from a .yaml file

    :param filename: str, the path to the yaml file to be read

    :return: dict, the paths as a dictionary object.
    """
    with open(filename, 'r') as f_in:
        G = yaml.safe_load(f_in)
    return G


def write_yaml(G, outname):
    """
    Write the DrugMechDB paths out to a .yaml file

    :param G: dict, the DrugMechDB paths as a dictionary object
    :param outname: the path to write the yaml output file
    """

    with open(outname, 'w') as fout:
        yaml.dump(G, stream=fout, indent=4, default_flow_style=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Interconvert .json and .yaml representations of DrugMechDB')
    parser.add_argument('filename', help='The name of the file to convert', type=str)
    parser.add_argument('-o', '--outname', help='Name of the output file for conversion. Default: indication_paths',
                        default='indication_paths')

    args = parser.parse_args()

    filename = args.filename
    outname = args.outname

    # Get the infile type
    in_json = False
    in_yaml = False

    if filename.endswith('.json'):
        in_json = True
    elif filename.endswith('.yaml'):
        in_yaml = True
    else:
        print("Can't determine input filetype. Please ensure proper .json or .yaml extension")
        exit(1)

    # Get the proper extension for the output file
    if in_json and not outname.endswith('.yaml'):
        outname = outname + '.yaml'

    elif in_yaml and not outname.endswith('.json'):
        outname = outname = '.json'

    if in_json:
        G = read_json(filename)
        write_yaml(G, outname)
    elif in_yaml:
        G = read_yaml(filename)
        write_json(G, outname)

