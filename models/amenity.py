#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):

    def __init__(self, *args, **kwargs):
        if args and type(args[0]) is dict:
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
        self.name = ""