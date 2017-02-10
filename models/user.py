#!/usr/bin/python3

<<<<<<< HEAD
BaseModel = __import__('base_model').BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
=======
from models.base_model import BaseModel


class User(BaseModel):

    def __init__(self, *args, **kwargs):
        if args and type(args[0]) is dict:
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
>>>>>>> 17051d047bbd18d2900b5fcc93f9bdf2f26d8ff8
