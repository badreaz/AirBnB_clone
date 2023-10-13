#!/usr/bin/python3
"""Class State that inherits from the BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """The State Class"""
    name: str = ""
