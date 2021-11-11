#!/usr/bin/python3
"""FileStorage class"""
from models.base_model import BaseModel
import json

class FileStorage:
    """ Json storage engine """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all the objects in dict format"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects the obj with key id"""
        objClassName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objClassName, obj.id)] = obj

    def save(self):
        """serialize __objects to json file"""
        with open(FileStorage.__file_path, "w") as file:
            objDict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(objDict, file)

    def reload(self):
        "deserialize the JSON file"
        try:
            with open(FileStorage.__file_path, "r") as file:
                for key, value in (json.load(file)).items():
                    value =  eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            return
