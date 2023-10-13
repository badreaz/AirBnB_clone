#!/usr/bin/python3
"""Class City that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """The City class"""
    name: str = ""
    state_id: str = ""
