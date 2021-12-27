import json
import os.path
from typing import Type

from serilib import Serializable
from serilib.serializers.abstract_serializer import AbstractSerializer


class JsonSerializer(AbstractSerializer):
    @staticmethod
    def deserialize(file_path, deserializable_class: Type[Serializable]):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Specified file {file_path!r} does not exist!')
        with open(file_path, "r", encoding='utf-8') as json_data:
            return deserializable_class.deserialize(json.load(json_data))

    @staticmethod
    def serialize(file_path, serializable_object: Serializable):
        with open(file_path, "w", encoding='utf-8') as json_data:
            json.dump(serializable_object.serialize(), json_data, indent=1)
