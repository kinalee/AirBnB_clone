#!/usr/bin/python3
import os.path
import json
import datetime


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
                serial[key].update({'created_at': str(serial[key]['created_at'])})
                serial[key].update({'updated_at': str(serial[key]['updated_at'])})
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(serial, json_file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                FileStorage.__objects = json.load(json_file)
            for key in FileStorage.__objects.keys():
                FileStorage.__objects[key].update({'created_at': datetime.datetime.strptime(FileStorage.__objects[key]['created_at'], '%Y-%m-%d %H:%M:%S.%f')})
                FileStorage.__objects[key].update({'updated_at': datetime.datetime.strptime(FileStorage.__objects[key]['updated_at'], '%Y-%m-%d %H:%M:%S.%f')})
