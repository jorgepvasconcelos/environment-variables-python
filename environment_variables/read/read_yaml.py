from pprint import pprint, pp

import yaml


def read_yaml(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        values = dict(yaml.full_load(file))
        return values
