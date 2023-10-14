#!/usr/bin/python3
"""
TestAmenityDocs classes
"""

from datetime import datetime
import inspect
from models import amenity
from models.base_model import BaseModel
import pep8
import unittest
Amenity = amenity.Amenity



class TestAmenityDocs(unittest.TestCase):
    """Tests that checks the documentation and style of Amenity"""
    @classmethod
    def setUpClass(cls):
        """Set up the doc tests"""
        cls.amenity_func = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test to check models/amenity.py conforms to PEP8."""
        c_pep8 = pep8.StyleGuide(quiet=True)
        result = c_pep8.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Test the amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                "amenity.py needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test the presence of docstrings in Amenity methods"""
        for f in self.amenity_func:
            self.assertIsNot(f[1].__doc__, None,
                             "{:s} method needs a docstring".format(f[0]))
            self.assertTrue(len(f[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(f[0]))

class TestAmenity(unittest.TestCase):
        """Test Amenity class"""
        def test_is_subclass(self):
            """Test Amenity is a subclass of BaseModel"""
            amen = Amenity()
            self.assertIsInstance(amen, BaseModel)
            self.assertTrue(hasattr(amen, "id"))
            self.assertTrue(hasattr(amen, "created_at"))
            self.assertTrue(hasattr(amen, "updated_at"))

        def test_name_attr(self):
            """Test Amenity has attribute name, and it's empty string"""
            amen = Amenity()
            self.assertTrue(hasattr(amen, "name"))
            self.assertEqual(amen.name, "")

        def test_to_dict_creates_dict(self):
            """test to_dict method if creates a dictionary with proper attrs"""
            amen = Amenity()
            new_dict = amen.to_dict()
            self.assertEqual(type(new_dict), dict)
            for attr in amen.__dict__:
                self.assertTrue(attr in new_dict)
                self.assertTrue("__class__" in new_dict)

        def test_to_dict_values(self):
            """test values in dict returned from to_dict"""
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            amen = Amenity()
            new_dict = amen.to_dict()
            self.assertEqual(new_dict["__class__"], "Amenity")
            self.assertEqual(type(new_dict["created_at"]), str)
            self.assertEqual(type(new_dict["updated_at"]), str)
            self.assertEqual(new_dict["created_at"], amen.created_at.strftime(time_format))
            self.assertEqual(new_dict["updated_at"], amen.updated_at.strftime(time_format))

        def test_str(self):
            """test str method has the correct output"""
            amen = Amenity()
            string = "[Amenity] ({}) {}".format(amen.id, amen.__dict__)
            self.assertEqual(string, str(amen))
