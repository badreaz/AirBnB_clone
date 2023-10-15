#!/usr/bin/python3
"""File storage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.city import City


class FileStorage:
    """Class to serialize instances to JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj and obj class name as key"""
        key = type(obj).__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON path"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as fd:
            json.dump(obj_dict, fd)

    def reload(self):
        """Deserialize JSON file to __objects if it exists"""
        classes = {
                "BaseModel": BaseModel, "User": User, "Place": Place,
                "Amenity": Amenity, "City": City, "Review": Review,
                "State": State}
        try:
            with open(self.__file_path, "r") as fd:
                obj_dict = json.load(fd)
            for key, value in obj_dict.items():
                class_name = classes[value["__class__"]](**value)
                self.__objects[key] = class_name
        except FileNotFoundError:
            pass
