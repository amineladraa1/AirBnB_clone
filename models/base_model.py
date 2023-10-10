#!/usr/bin/python3
"""Defines BaseModel class."""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    def __init__(self):
        """Initialize a new BaseModel.

        Args:
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.today()

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

