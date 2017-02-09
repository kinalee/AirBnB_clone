#!/usr/bin/python3
import os.path
import json
from datetime import datetime


class FileStorage():
    __file_path = "models/engine/file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects.update({obj.id: obj})

    def save(self):
        serial = {}
        for key in FileStorage.__objects.keys():
            if type(FileStorage.__objects[key]) is not dict:
                serial.update({key: FileStorage.__objects[key].to_json()})
            else:
                serial.update({key: FileStorage.__objects[key]})
                my_dict = serial[key]
                my_dict.update({'created_at': str(my_dict['created_at'])})
                my_dict.update({'updated_at': str(my_dict['updated_at'])})
                serial[key] = my_dict
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(serial, json_file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                FileStorage.__objects = json.load(json_file)
            from models.base_model import BaseModel
            for key in FileStorage.__objects.keys():
                new_model = BaseModel(FileStorage.__objects[key])
                FileStorage.__objects.update({key: new_model})
