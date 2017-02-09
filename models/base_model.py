#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel():

    def __init__(self, *args, **kwargs):
        time = '%Y-%m-%d %H:%M:%S.%f'
        dict_found = 0
        for item in args:
            if type(item) is dict:
                dict_found = 1
                self.__dict__ = item
                self.created_at = datetime.strptime(item['created_at'], time)
                self.updated_at = datetime.strptime(item['updated_at'], time)
        if not dict_found:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            from models.__init__ import storage
            storage.new(self)


    def save(self):
        self.updated_at = datetime.now()
        from models.__init__ import storage
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
