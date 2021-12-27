import os.path
from typing import Type

import yaml

from serilib import Serializable
from serilib.serializers.abstract_serializer import AbstractSerializer


class YamlSerializer(AbstractSerializer):
    @staticmethod
    def deserialize(file_path, deserializable_class: Type[Serializable]):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Specified file {file_path!r} does not exist!')
        with open(file_path, "r", encoding='utf-8') as yaml_data:
            return deserializable_class.deserialize(yaml.safe_load(yaml_data))

    @staticmethod
    def serialize(file_path, serializable_object: Serializable):
        with open(file_path, "w", encoding='utf-8') as yaml_data:
            yaml.safe_dump(serializable_object.serialize(), yaml_data, indent=1)


