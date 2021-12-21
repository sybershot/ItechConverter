import sys

from person import PersonList
from serilib import JsonSerializer, YamlSerializer, CSVSerializer

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Expected exactly ONE parameter!')
        exit(1)
    input_path = sys.argv[1]
    csv_path = input_path.replace(".json", ".csv")
    yaml_path = input_path.replace(".json", ".yml")
    person_list = JsonSerializer.deserialize(input_path, PersonList)
    CSVSerializer.serialize(csv_path, person_list)
    person_list = CSVSerializer.deserialize(csv_path, PersonList)
    YamlSerializer.serialize(yaml_path, person_list)

