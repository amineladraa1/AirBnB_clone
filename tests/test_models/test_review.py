#!/usr/bin/python3
"""
TestReviewDocs classes
"""

from datetime import datetime
import inspect
from models import review
from models.base_model import BaseModel
import pep8
import unittest
Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """check the documentation and style of Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up the doc tests"""
        cls.review_func = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """models/review.py conforms to PEP8."""
        s_pep8 = pep8.StyleGuide(quiet=True)
        result = s_pep8.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """tests/test_models/test_review.py conforms to PEP8."""
        s_pep8 = pep8.StyleGuide(quiet=True)
        result = s_pep8.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """the review.py module docstring"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """the presence of docstrings in Review methods"""
        for func in self.review_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestReview(unittest.TestCase):
    """the Review class"""
    def test_is_subclass(self):
        """Review is a subclass of BaseModel"""
        rev = Review()
        self.assertIsInstance(rev, BaseModel)
        self.assertTrue(hasattr(rev, "id"))
        self.assertTrue(hasattr(rev, "created_at"))
        self.assertTrue(hasattr(rev, "updated_at"))

    def test_place_id_attr(self):
        """Review has attr place_id, and it's an empty string"""
        rev = Review()
        self.assertTrue(hasattr(rev, "place_id"))
        self.assertEqual(rev.place_id, "")

    def test_user_id_attr(self):
        """Review has attr user_id, and it's an empty string"""
        rev = Review()
        self.assertTrue(hasattr(rev, "user_id"))
        self.assertEqual(rev.user_id, "")

    def test_text_attr(self):
        """Review has attr text, and it's an empty string"""
        rev = Review()
        self.assertTrue(hasattr(rev, "text"))
        self.assertEqual(rev.text, "")

    def test_to_dict_creates_dict(self):
        """to_dict method creates a dictionary with proper attrs"""
        rev = Review()
        new_dict = rev.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in rev.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        rev = Review()
        new_dict = rev.to_dict()
        self.assertEqual(new_dict["__class__"], "Review")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], rev.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"], rev.updated_at.strftime(time_format))

    def test_str(self):
        """the str method has the correct output"""
        rev = Review()
        string = "[Review] ({}) {}".format(rev.id, rev.__dict__)
        self.assertEqual(string, str(review))
