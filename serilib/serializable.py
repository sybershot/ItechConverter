import warnings
from typing import Mapping


class DeserializationError(Exception):
    pass


class SerializationError(Exception):
    pass


class Serializable:
    """Marks object as serializable.
    All serializable objects must have _mapper attribute to map fields from dictionary to class attributes and vice versa
    In other cases you need to override serialize and deserialize methods
    """
    _mapper = {}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    def serialize(self):
        return {original_name: getattr(self, internal_name) for (original_name, internal_name) in self._mapper.items()}

    @classmethod
    def deserialize(cls, serialized_data):
        if not cls.validate(serialized_data):
            raise DeserializationError(f'Failed to deserialize {cls.__name__} class due to validation error!')
        return cls(
            **{internal_name: serialized_data.get(original_name, None) for (original_name, internal_name) in
               cls._mapper.items()})

    @classmethod
    def validate(cls, serialized_data):
        if not isinstance(serialized_data, Mapping):
            warnings.warn(f'Expected dict like object as input, but got {type(serialized_data)}!')
            return False
        for expected_key in cls._mapper:
            if expected_key not in serialized_data:
                warnings.warn(f'Missing {expected_key!r} key in {cls.__name__}!')
                return False
        return True
