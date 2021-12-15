import json
import yaml
import csv
import os.path
from typing import Type, List, Mapping
from .serializable import Serializable, SerializationError


class BaseSerializer:
    @classmethod
    def from_file(cls, file_path, deserializable_class: Type[Serializable]):
        raise NotImplementedError

    @classmethod
    def to_file(cls, file_path, serializable_object: Serializable):
        raise NotImplementedError


class JsonSerializer(BaseSerializer):
    @classmethod
    def from_file(cls, file_path, deserializable_class: Type[Serializable]):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Specified file {file_path!r} does not exist!')
        with open(file_path, "r", encoding='utf-8') as json_data:
            return deserializable_class.deserialize(json.load(json_data))

    @classmethod
    def to_file(cls, file_path, serializable_object: Serializable):
        with open(file_path, "w", encoding='utf-8') as json_data:
            json.dump(serializable_object.serialize(), json_data, indent=1)


class YamlSerializer(BaseSerializer):
    @classmethod
    def from_file(cls, file_path, deserializable_class: Type[Serializable]):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Specified file {file_path!r} does not exist!')
        with open(file_path, "r", encoding='utf-8') as yaml_data:
            return deserializable_class.deserialize(yaml.safe_load(yaml_data))

    @classmethod
    def to_file(cls, file_path, serializable_object: Serializable):
        with open(file_path, "w", encoding='utf-8') as yaml_data:
            yaml.safe_dump(serializable_object.serialize(), yaml_data, indent=1)


class CSVSerializer(BaseSerializer):
    @classmethod
    def from_file(cls, file_path, deserializable_class: Type[Serializable]):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Specified file {file_path!r} does not exist!')
        with open(file_path, "r", encoding='utf-8') as csv_data:
            reader = csv.DictReader(csv_data)
            return deserializable_class.deserialize([cls._unpack_row(item) for item in reader])

    @classmethod
    def to_file(cls, file_path, serializable_object: Serializable):
        with open(file_path, "w", encoding='utf-8', newline='') as csv_data:
            serialized_data = serializable_object.serialize()
            header = cls._validate_and_return_keys(serialized_data)
            csv_writer = csv.DictWriter(csv_data, header)
            csv_writer.writeheader()
            for item in serialized_data:
                csv_writer.writerow(cls._pack_row(item))

    @staticmethod
    def _pack_row(item):
        new_item = {}
        for field, value in item.items():
            if isinstance(value, List):
                new_item[field] = ';'.join(list(map(str, value)))
            else:
                new_item[field] = value
        return new_item


    @staticmethod
    def _unpack_row(item):
        new_item = {}
        for field, value in item.items():
            if ';' in value:
                new_item[field] = value.split(';')
            else:
                new_item[field] = value
        return new_item


    @staticmethod
    def _validate_and_return_keys(serialized_data):
        if not isinstance(serialized_data, List):
            return None
        keys = set()
        for item in serialized_data:
            if not isinstance(item, Mapping):
                raise SerializationError(f'Got unexpected data for CSV writer!')
            [keys.add(key) for key in item.keys()]
        return keys
