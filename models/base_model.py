#!/usr/bin/python3

import datetime
import uuid


class BaseModel():

    def __init__(self):
        self.created_at = datetime.datetime.now().isoformat()
        self.id = uuid.uuid4()

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_json(self):
        self.__dict__.update({'__class__': self.__class__.__name__})
        return self.__dict__

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
