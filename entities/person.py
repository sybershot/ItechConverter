from serilib.serializable import SerializableObject


class Person(SerializableObject):
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
