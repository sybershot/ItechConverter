import warnings
from typing import Mapping, List, Iterable

from serilib.serializable.abstract import Serializable


class DeserializationError(Exception):
    pass


class SerializationError(Exception):
    pass


class SerializableList(Serializable, List[Serializable]):
    _item_class = Serializable

    def serialize(self):
        return [item.serialize() for item in self]

    @classmethod
    def validate(cls, serialized_data):
        return isinstance(serialized_data, Iterable)

    @classmethod
    def deserialize(cls, serialized_data):
        if cls.validate(serialized_data):
            obj = cls()
            for i in serialized_data:
                obj.append(cls._item_class.deserialize(i))
            return obj
