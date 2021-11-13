#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
            dictionary = {key: value.to_dict() for key,
                          value in FileStorage.__objects.items()}
            json.dump(dictionary, file)

    def reload(self):
        """deserialize"""
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as file:
                dictionary = json.load(file)
                for objects in dictionary.values():
                    class_name = objects["__class__"]
                    del objects["__class__"]
                    self.new(eval(class_name)(**objects))
        except Exception:
            return
