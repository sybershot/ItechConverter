from abc import ABC


class DeserializationError(Exception):
    pass


class SerializationError(Exception):
    pass


class Serializable(ABC):
    """Marks object as serializable.
    All serializable objects must have _mapper attribute to map fields from dictionary to class attributes and vice versa
    In other cases you need to override serialize and deserialize methods
    """

    def serialize(self):
        pass

    @classmethod
    def deserialize(cls, serialized_data):
        pass

    @classmethod
    def validate(cls, serialized_data):
        pass
