from serilib.serializable.list import SerializableList
from .person import Person

class PersonList(SerializableList):
    _item_class = Person
