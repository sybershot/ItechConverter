import sys

from person import PersonList
from serializable import JsonSerializer, YamlSerializer, CSVSerializer

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Expected 1 parameter!')
        exit(1)
    input_path = sys.argv[1]
    person_list = JsonSerializer.from_file(input_path, PersonList)
    CSVSerializer.to_file(input_path.replace(".json", ".csv"), person_list)
    person_list = CSVSerializer.from_file(input_path.replace(".json", ".csv"), PersonList)
    YamlSerializer.to_file(input_path.replace(".json", ".yml"), person_list)

