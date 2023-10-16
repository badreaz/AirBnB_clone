#!/usr/bin/python3
"""Base Model class for other classes"""

from datetime import datetime
from uuid import uuid4
import models

fmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base class for all classes"""

    def __init__(self, *args, **kwargs):
        """Instastiate the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, fmt))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """Override the str representation of class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at attr with current time"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns dict containing key/values of instance"""
        cls_dict = self.__dict__.copy()
        cls_dict["__class__"] = type(self).__name__
        cls_dict["created_at"] = cls_dict["created_at"].isoformat()
        cls_dict["updated_at"] = cls_dict["updated_at"].isoformat()
        return cls_dict
