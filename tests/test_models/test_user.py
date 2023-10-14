#!/usr/bin/python3
"""
TestUserDocs classes
"""

from datetime import datetime
import inspect
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = user.User


class TestUserDocs(unittest.TestCase):
    """check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """City class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """User class"""
    def test_is_subclass(self):
        """User is a subclass of BaseModel"""
        u = User()
        self.assertIsInstance(u, BaseModel)
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))

    def test_email_attr(self):
        """User has attr email, and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertEqual(u.email, "")

    def test_password_attr(self):
        """User has attr password, and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "password"))
        self.assertEqual(u.password, "")

    def test_first_name_attr(self):
        """User has attr first_name, and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "first_name"))
        self.assertEqual(u.first_name, "")

    def test_last_name_attr(self):
        """has attr last_name, and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = User()
        new_dict = u.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_dict = u.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        u = User()
        string = "[User] ({}) {}".format(u.id, u.__dict__)
        self.assertEqual(string, str(u))
