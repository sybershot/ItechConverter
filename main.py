import sys

from entities import PersonList
from serilib import JsonSerializer, YamlSerializer, CSVSerializer

JSON_EXT = ".json"
CSV_EXT = ".csv"
YAML_EXT = ".yml"


def replace_extension(path, source, target):
    return path.replace(source, target)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Expected exactly ONE parameter!')
        exit(1)
    input_path = sys.argv[1]

    csv_path = replace_extension(input_path, JSON_EXT, CSV_EXT)
    yaml_path = replace_extension(input_path, JSON_EXT, YAML_EXT)
    person_list = JsonSerializer.deserialize(input_path, PersonList)
    CSVSerializer.serialize(csv_path, person_list)
    person_list = CSVSerializer.deserialize(csv_path, PersonList)
    YamlSerializer.serialize(yaml_path, person_list)
