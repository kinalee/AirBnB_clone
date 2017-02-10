#!/usr/bin/python3

BaseModel = __import__('base_model').BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
