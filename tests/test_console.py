#!/usr/bin/python3
"""Defines unittests for the console"""

import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage
import console
from console import HBNBCommand


class TestHBNBCommand(unittest.HBNBCommand):
    """Unittest for HBNB Command"""
    def setUp(self):
        self.command = HBNBCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_prompt(self):
        self.assertEqual("(hbnb)", self.command.prompt())
