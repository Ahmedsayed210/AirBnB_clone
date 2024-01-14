#!/usr/bin/python3
"""Module for user class """

from models.base_model import BaseModel


class User(BaseModel):
    """ Class User takes user information """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""