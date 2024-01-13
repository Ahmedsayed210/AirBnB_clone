#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self,*args,**kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))

                if key != "__class__":
                    setattr(self, key,value)

                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())

                if 'created_at' not in kwargs:
                    self.created_at = datetime.utcnow()

                if 'updated_at' not in kwargs:
                    self.created_at = datetime.utcnow()

        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)


    def save(self):
        """Method to save id to the storage"""
        self.updated_at = datetime.utcnow()
        models.storage.save()


    def to_dict(self):
        object_dic = self.__dict__.copy()
        object_dic["__class__"] = self.__class__.__name__
        object_dic["created_at"] = self.created_at.isoformat()
        object_dic["updated_at"] = self.updated_at.isoformat()

        return object_dic




    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)