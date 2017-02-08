#!/usr/bin/python3

import datetime
import uuid


class BaseModel():

    def __init__(self):
        self.created_at = datetime.datetime.today().isoformat()
        self.id = uuid.UUID
        self.__dict__.update({'__class__': self.__class__.__name__})

    def save(self):
        self.updated_at = datetime.datetime.today().isoformat()

    def to_json(self):
        return self.__dict__

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
