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
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj and obj class name as key"""
        key = type(obj).__name__ + "." + str(obj.id)
        value = obj
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON path"""
        with open(FileStorage.__file_path, "w") as fd:
            json.dump(FileStorage.__objects, fd)

    def reload(self):
        """Deserialize JSON file to __objects if it exists"""
        try:
            with open(FileStorage.__file_path, "r") as fd:
                FileStorage.__objects = json.load(fd)
