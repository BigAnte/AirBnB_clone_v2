#!/usr/bin/python3
"""All the test for the place model are implemented here. """
from tests.test_models.test_base_model import test_basemodel
import unittest
from models.base_model import BaseModel
from models.place import Place
from os import getenv, remove


storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestPlace(unittest.TestCase):
    """Test Place """
     @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_place = Place(city_id="0O01", user_id="0O02", name="house",
                              description="awesome", number_rooms=3,
                              number_bathrooms=2, max_guest=1,
                              price_by_night=100, latitude=37.77,
                              longitude=127.12)

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_place
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def __init__(self, *args, **kwargs):
        """ test instantiation"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test city id is str """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test user id is str """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test name is str """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test description is str """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test room number is int"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test bathrooms number is int"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test max-guest is int """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test price by night is int """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test latitude is float """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test longitude is float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test amenity ids is type list """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_Place_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_place.__tablename__, "places")

    def test_Place_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''

        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes(self):
        '''
            Checks that the attribute exist.
        '''
        self.assertTrue("city_id" in self.new_place.__dir__())
        self.assertTrue("user_id" in self.new_place.__dir__())
        self.assertTrue("description" in self.new_place.__dir__())
        self.assertTrue("name" in self.new_place.__dir__())
        self.assertTrue("number_rooms" in self.new_place.__dir__())
        self.assertTrue("max_guest" in self.new_place.__dir__())
        self.assertTrue("price_by_night" in self.new_place.__dir__())
        self.assertTrue("latitude" in self.new_place.__dir__())
        self.assertTrue("longitude" in self.new_place.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_place_amenity_attrb(self):
        self.assertTrue("amenity_ids" in self.new_place.__dir__())

    @unittest.skipIf(storage != "db", "Testing database storage only")
    def test_place_amenity_dbattrb(self):
        self.assertTrue("amenities" in self.new_place.__dir__())
        self.assertTrue("reviews" in self.new_place.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_longitude(self):
        '''
            Test the type of longitude.
        '''
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_latitude(self):
        '''
            Test the type of latitude
        '''
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_amenity(self):
        '''
            Test the type of latitude
        '''
        amenity = getattr(self.new_place, "amenity_ids")
        self.assertIsInstance(amenity, list)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_price_by_night(self):
        '''
            Test the type of price_by_night
        '''
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_max_guest(self):
        '''
            Test the type of max_guest
        '''
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_number_bathrooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_number_rooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_description(self):
        '''
            Test the type of description
        '''
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_user_id(self):
        '''
            Test the type of user_id
        '''
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_city_id(self):
        '''
            Test the type of city_id
        '''
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)