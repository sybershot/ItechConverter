import warnings
from typing import Mapping


class DeserializationError(Exception):
    pass


class SerializationError(Exception):
    pass


class Serializable:
    _expected_keys = ()

    def serialize(self):
        raise NotImplementedError

    @classmethod
    def deserialize(cls, serialized_data):
        raise NotImplementedError

    @classmethod
    def validate(cls, serialized_data):
        if not isinstance(serialized_data, Mapping):
            warnings.warn(f'Expected dict like object as input, but got {type(serialized_data)}!')
            return False
        for expected_key in cls._expected_keys:
            if expected_key not in serialized_data:
                warnings.warn(f'Missing {expected_key!r} key in {cls.__name__}!')
                return False
        return True
