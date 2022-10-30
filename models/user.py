#!/usr/bin/python3
""" User Module that Inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class Used to represent an User
        Attributes
        ----------
        email : str
            email of the user
        password: str
            password of the user
        first_name: str
            first legal name of the user
        last_name: str
            last legal name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
