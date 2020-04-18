import yaml

def read_yaml_into_dict(path: str) -> dict:
    with open(path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            return data
        except yaml.YAMLError as exc:
            print(exc)
