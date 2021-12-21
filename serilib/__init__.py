from .serializable import Serializable, DeserializationError
from .serializers import *


# Shortcuts:

def to_json(file_path, serializable_object: Serializable):
    serializer = JsonSerializer()
    serializer.serialize(file_path, serializable_object)


def to_yaml(file_path, serializable_object: Serializable):
    serializer = YamlSerializer()
    serializer.serialize(file_path, serializable_object)


def to_csv(file_path, serializable_object: Serializable):
    serializer = CSVSerializer()
    serializer.serialize(file_path, serializable_object)
