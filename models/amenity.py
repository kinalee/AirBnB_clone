#!/usr/bin/python3

BaseModel = __import__('base_model').BaseModel

class Amenity(BaseModel):

    def __init__(self):
        self.name = ""
