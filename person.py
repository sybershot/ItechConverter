from typing import Iterable, List

from serilib import Serializable, DeserializationError


class PersonList(Serializable):

    def serialize(self):
        return [person.serialize() for person in self.person_list]

    @classmethod
    def validate(cls, serialized_data):
        return isinstance(serialized_data, Iterable)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.person_list: List[Person] = []

    @classmethod
    def deserialize(cls, serialized_data):
        if cls.validate(serialized_data):
            obj = cls()
            for i in serialized_data:
                obj.person_list.append(Person.deserialize(i))
            return obj


class Person(Serializable):

    _mapper = {"name": "name", "last name": "last_name",
               "birthday": "birthday", "height": "height",
               "weight": "weight", "car": "car",
               "car model": "car_model", "languages": "languages"}

    def __init__(self, name, last_name, birthday, height, weight, car, car_model, languages, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.height = height
        self.weight = weight
        self.car = car
        self.car_model = car_model
        self.languages = languages
