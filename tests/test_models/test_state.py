#!/usr/bin/python3
"""
the TestStateDocs classes
"""

from datetime import datetime
import inspect
from models import state
from models.base_model import BaseModel
import pep8
import unittest
State = state.State


class TestStateDocs(unittest.TestCase):
    """check the documentation and style of State class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """that models/state.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """tests/test_models/test_state.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """Test for the state.py module docstring"""
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_state_class_docstring(self):
        """the State class docstring"""
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_func_docstrings(self):
        """the presence of docstrings in State methods"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestState(unittest.TestCase):
    """State class"""
    def test_is_subclass(self):
        """State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name_attr(self):
        """State has attribute name, and it's as an empty string"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        st = State()
        new_dict = st.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in st.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        st = State()
        new_dict = st.to_dict()
        self.assertEqual(new_dict["__class__"], "State")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], st.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"], st.updated_at.strftime(time_format))

    def test_str(self):
        """the str method has the correct output"""
        st = State()
        string = "[State] ({}) {}".format(st.id, st.__dict__)
        self.assertEqual(string, str(st))
