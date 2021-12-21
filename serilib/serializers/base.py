from typing import Type, List, Mapping
from serilib.serializable import Serializable, SerializationError


class AbstractSerializer:
    @classmethod
    def deserialize(cls, file_path, deserializable_class: Type[Serializable]):
        raise NotImplementedError

    @classmethod
    def serialize(cls, file_path, serializable_object: Serializable):
        raise NotImplementedError




