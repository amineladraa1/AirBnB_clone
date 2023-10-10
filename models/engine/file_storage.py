#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path : name of the file to save objects to.
        __objects : dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects  # added double underscore

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        o_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(o_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as fi:
            # Added encoding
            json.dump(obj_dict, fi)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as f:
                # Added encoding
                objdict = json.load(f)
                for obj in objdict.values():
                    # Removed unnecessary code
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
