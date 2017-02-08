#!/usr/bin/python3

import datetime
import uuid
from models.__init__ import storage


class BaseModel():

    def __init__(self, *args, **kwargs):
        if args and type(args[0]) is dict:
            self.__dict__ = args[0]
        else:
            self.created_at = datetime.datetime.now().isoformat()
            self.id = str(uuid.uuid4())
            storage.new(self)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()
        storage.save()

    def to_json(self):
        self.__dict__.update({'__class__': self.__class__.__name__})
        return self.__dict__

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
