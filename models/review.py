#!/usr/bin/python3
"""The Review model that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Review"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
