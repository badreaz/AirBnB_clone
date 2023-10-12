#!/usr/bin/python3
"""File storage class"""

import json
import models


class FileStorage:
    """Class to serialize instances to JSON file and 
    deserializes JSON file to instances"""
    __file_path  = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj and obj class name as key"""
        key = type(obj).__name__ + "." + str(obj.id)
        value = obj
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON path"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as fd:
            json.dump(obj_dict, fd)

    def reload(self):
        """Deserialize JSON file to __objects if it exists"""
        try:
            with open(FileStorage.__file_path, "r") as fd:
                obj_dict = json.load(fd)
            for key, value in obj_dict.items():
                class_name = value["__class__"](**value)
                FileStorage.__objects[key] = class_name
        except FileNotFoundError:
            pass
