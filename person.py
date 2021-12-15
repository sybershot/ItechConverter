
from typing import Iterable, List

from serializable import Serializable, DeserializationError


class PersonList(Serializable):

    def serialize(self):
        return [person.serialize() for person in self.person_list]

    @classmethod
    def validate(cls, serialized_data):
        return isinstance(serialized_data, Iterable)

    def __init__(self) -> None:
        self.person_list: List[Person] = []

    @classmethod
    def deserialize(cls, serialized_data):
        if cls.validate(serialized_data):
            obj = cls()
            for i in serialized_data:
                obj.person_list.append(Person.deserialize(i))
            return obj


class Person(Serializable):
    # must be the same order as init arguments
    _expected_keys = ("name", "last name", "birthday", "height", "weight", "car", "car model", "languages")

    def serialize(self):
        return {"name": self.name, "last name": self.last_name, "birthday": self.birthday, "height": self.height,
                "weight": self.weight, "car": self.car, "car model": self.car_model, "languages": self.languages}

    @classmethod
    def deserialize(cls, serialized_data):
        if not cls.validate(serialized_data):
            raise DeserializationError(f'Failed to deserialize {cls.__name__} class due to validation error!')
        return cls(*[serialized_data[name] for name in cls._expected_keys])

    def __init__(self, name, last_name, birthday, height, weight, car, car_model, languages):
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.height = height
        self.weight = weight
        self.car = car
        self.car_model = car_model
        self.languages = languages

