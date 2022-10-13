#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest
import pep8
from models.base_model import BaseModel
from models.review import Review
from os import getenv, remove


storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestReview(unittest.TestCase):
    """Test Review """
    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.rev = Review()
        cls.rev.user_id = "Adriel and Melissa 123"
        cls.rev.place_id = "Amy and Victor's room at SF"
        cls.rev.text = "Team Awesome includes Adekunle"

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.rev
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_style_check(self):
        '''
            Tests pep8 style
        '''
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error needs fixing")
    
    def __init__(self, *args, **kwargs):
        """ test instantiation"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test place is str """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test user id is str """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test text is str """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_Review_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.rev.__tablename__, "reviews")

    def test_Review_inheritance(self):
        '''
            Tests that the Review class Inherits from BaseModel
        '''
        self.assertIsInstance(self.rev, BaseModel)

    def test_Review_attributes(self):
        '''
            Tests Review class has place_id, user_id and text attributes
        '''
        self.assertTrue("place_id" in self.rev.__dir__())
        self.assertTrue("user_id" in self.rev.__dir__())
        self.assertTrue("text" in self.rev.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        place_id = getattr(self.rev, "place_id")
        user_id = getattr(self.rev, "user_id")
        text = getattr(self.rev, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)