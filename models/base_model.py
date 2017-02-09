#!/usr/bin/python3
import datetime
import uuid
from models.__init__ import storage


class BaseModel():

    def __init__(self, *args, **kwargs):
        if args and type(args[0]) is dict:
            self.created_at = datetime.datetime.strptime(args[0]['created_at'], '%Y-%m-%d %H:%H:S.%f')
            if args[0][updated_at]:
                self.updated_at = datetime.datetime.strptime(args[0]['updated_at'], '%Y-%m-%d %H:%H:S.%f')
            self.__dict__ = args[0]
        else:
            self.created_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
            storage.new(self)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_json(self):
        newdict = self.__dict__.copy()
        newdict.update({'__class__': self.__class__.__name__})
        newdict.update({'updated_at': str(self.updated_at)})
        newdict.update({'created_at': str(self.created_at)})
        return newdict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
