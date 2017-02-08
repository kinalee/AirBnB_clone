#!/usr/bin/python3
import os.path
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects.update({obj.id: str(obj)})

    def save(self):
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                FileStorage.__objects = json.load(json_file)
