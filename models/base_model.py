#!/usr/bin/python3
"""Defines BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs: # changed from len(kwargs) != 0 to kwargs
            time_form = "%Y-%m-%dT%H:%M:%S.%f" # moved inside if block
            for key, val in kwargs.items():
                if key == "__class__": # Added check for key "__class__"
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, time_form)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.today()
        models.storage.save() # Added save method

    def to_dict(self):
        """returns dictionary containing keys/values of __dict__"""
        m_dict = self.__dict__.copy()
        m_dict["created_at"] = self.created_at.isoformat()
        m_dict["updated_at"] = self.updated_at.isoformat()
        m_dict["__class__"] = self.__class__.__name__
        return m_dict

    def __str__(self):
        """Return the str to print """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

