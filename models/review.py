#!/usr/bin/python3

BaseModel = __import__('base_model').BaseModel


class Review(BaseModel):

    def __init__(self):
        place_id = ""
        user_id = ""
        text = ""
