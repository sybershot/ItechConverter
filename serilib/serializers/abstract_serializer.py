from abc import ABC
from typing import Type, List, Mapping
from serilib.serializable import Serializable, SerializationError


class AbstractSerializer(ABC):
    @staticmethod
    def deserialize(file_path, deserializable_class: Type[Serializable]):
        """
        Deserializes object from file path.
        :param file_path: Path to the input file, must be a string.
        :param deserializable_class: Accepts any class inherited from Serializable.
        """
        pass

    @staticmethod
    def serialize(file_path, serializable_object: Serializable):
        """
        Serializes object to file
        :param file_path: Path to the output file, must be a string.
        :param serializable_object: Accepts any object inherited from Serializable.
        """
        pass
