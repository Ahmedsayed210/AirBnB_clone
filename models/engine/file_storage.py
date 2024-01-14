#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialize_obj = {}

        for key, obj in FileStorage.__objects.items():
            serialize_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialize_obj, file)

    def reload(self):
        """
        This method deserializes the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)

                    for key, value in data.items():
                        class_name, obj_id = key.split('.')

                        clas = eval(class_name)

                        instance = clas(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
