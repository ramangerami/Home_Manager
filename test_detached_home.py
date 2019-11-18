import unittest
import inspect
from abstract_home import AbstractHome
from detached_home import DetachedHome


class TestDetachedHome(unittest.TestCase):
    """ Unit Tests for the Detached Home class """

    def setUp(self):
        """ Creates a test fixture before each method is run """
        self.detached_home = DetachedHome(12000, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, 3, True)
        self.assertIsNotNone(self.detached_home, "Detached Home must be defined.")
        self.logPoint()
    
    def tearDown(self):
        """ Resets the variables after each method is run """
        self.logPoint()

    def logPoint(self):
        """ Prints the current running method as it is running """
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_detached_home_constructor_valid(self):
        """ 010A - Valid constructor parameters """
        self.assertEqual(self.detached_home.get_square_footage(), 12000, "Detached Home must have valid square footage")
        self.assertEqual(self.detached_home.get_year_built(), 2010, "Detached Home must have valid year built")
        self.assertEqual(self.detached_home.get_number_of_rooms(), 18, "Detached Home must have valid number of rooms")
        self.assertEqual(self.detached_home.get_number_of_bathrooms(), 3, "Detached Home must have valid number of bathrooms")
        self.assertEqual(self.detached_home.get_city(), "Richmond", "Detached Home must have valid city")
        self.assertEqual(self.detached_home.get_selling_agent(), "Camelia Stewart", "Detached Home must have valid agent")
        self.assertEqual(self.detached_home.get_yearly_property_tax(), 0.25, "Detached Home must have valid tax")
        self.assertEqual(self.detached_home.get_type(), "detached home", "Detached Home must be a detached home")
        self.assertEqual(self.detached_home.get_number_of_floors(), 3, "Detached Home must have valid Number of Floors")
        self.assertEqual(self.detached_home.get_has_rental_suite(), True, "Detached Home must have valid Has Suite flag")

    def test_detached_home_constructor_undefined(self):
        """ 010B - Invalid undefined None constructor parameters """
        undefined_input = None
        # Must reject undefined parameter
        self.assertRaisesRegex(ValueError, "Square Footage cannot be undefined", DetachedHome, undefined_input, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Year Build cannot be undefined", DetachedHome, 12000, undefined_input, 18, 3, "Richmond", "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Number of Rooms cannot be undefined", DetachedHome, 12000, 2010, undefined_input, 3, "Richmond", "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Number of Bathrooms cannot be undefined", DetachedHome, 12000, 2010, 18, undefined_input, "Richmond", "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "City Name cannot be undefined", DetachedHome, 12000, 2010, 18, 3, undefined_input, "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Selling Agent Name cannot be undefined", DetachedHome, 12000, 2010, 18, 3, "Richmond", undefined_input, 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Yearly Property Tax cannot be undefined", DetachedHome, 12000, 2010, 18, 3, "Richmond", "Camelia Stewart", undefined_input, 800, True)
        self.assertRaisesRegex(ValueError, "Number of Floors cannot be undefined", DetachedHome, 12000, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, undefined_input, True)
        self.assertRaisesRegex(ValueError, "Has Suite cannot be undefined", DetachedHome, 12000, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, 800, undefined_input)
    
    def test_detached_home_constructor_invalid(self):
        """ 010C - Invalid other constructor parameters """
        test_string = "Hello"
        test_int = 5
        # Must reject parameter of incorrect type
        self.assertRaisesRegex(ValueError, "Square Footage must be of type: Integer", DetachedHome, test_string, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Year Build must be of type: Integer", DetachedHome, 12000, test_string, 18, 3, "Richmond", "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Number of Rooms must be of type: Integer", DetachedHome, 12000, 2010, test_string, 3, "Richmond", "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Number of Bathrooms must be of type: Integer", DetachedHome, 12000, 2010, 18, test_string, "Richmond", "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "City Name must be of type: String", DetachedHome, 12000, 2010, 18, 3, test_int, "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Selling Agent Name must be of type: String", DetachedHome, 12000, 2010, 18, 3, "Richmond", test_int, 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Yearly Property Tax must be of type: Float", DetachedHome, 12000, 2010, 18, 3, "Richmond", "Camelia Stewart", test_string, 800, True)
        self.assertRaisesRegex(ValueError, "Number of Floors must be of type: Integer", DetachedHome, 12000, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, test_string, True)
        self.assertRaisesRegex(ValueError, "Has Suite must be of type: Boolean", DetachedHome, 12000, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, 800, test_string)

        empty_string = ""
        # Must reject parameter of empty string
        self.assertRaisesRegex(ValueError, "City Name cannot be empty string.", DetachedHome, 12000, 2010, 18, 3, empty_string, "Camelia Stewart", 0.25, 800, True)
        self.assertRaisesRegex(ValueError, "Selling Agent Name cannot be empty string.", DetachedHome, 12000, 2010, 18, 3, "Richmond", empty_string, 0.25, 800, True)

    def test_detached_home_get_id_unset(self):
        """ 020A - Get id of an unset home """
        self.assertIsNone(self.detached_home.get_id())
        
    def test_detached_home_get_id_set(self):
        """ 020B - Get id of an set home """
        test_id = 1
        self.detached_home.set_id(test_id)
        self.assertEqual(self.detached_home.get_id(), test_id)
        
    def test_detached_home_set_id_unset_valid(self):
        """ 030A - Set an id for a home that has not been set """
        test_id = 2
        self.assertIsNone(self.detached_home.get_id())
        self.detached_home.set_id(test_id)
        self.assertEqual(self.detached_home.get_id(), test_id)
        
    def test_detached_home_set_id_set_valid(self):
        """ 030B - Set an id for a home that already has an id set """
        test_id1 = 5
        test_id2 = 9
        self.detached_home.set_id(test_id1)
        self.assertEqual(self.detached_home.get_id(), test_id1)
        self.detached_home.set_id(test_id2)
        self.assertEqual(self.detached_home.get_id(), test_id2)

    def test_detached_home_set_id_set_valid(self):
        """ 030C - Setting an id with invalid parameters """
        undefined_input = None
        # Must reject invalid parameters
        self.assertRaisesRegex(ValueError, "Home ID cannot be undefined", self.detached_home.set_id, undefined_input)
        test_string = "Hello"
        self.assertRaisesRegex(ValueError, "Home ID must be of type: Integer", self.detached_home.set_id, test_string)

    def test_detached_home_get_square_footage(self):
        """ 040A - Getting square footage """
        self.assertEqual(self.detached_home.get_square_footage(), 12000, "Detached Home must have valid square footage")

    def test_detached_home_get_year_built(self):
        """ 050A - Getting year built """
        self.assertEqual(self.detached_home.get_year_built(), 2010, "Detached Home must have valid year built")

    def test_detached_home_get_number_of_rooms(self):
        """ 060A - Getting square footage """
        self.assertEqual(self.detached_home.get_number_of_rooms(), 18, "Detached Home must have valid number of rooms")

    def test_detached_home_get_number_of_bathrooms(self):
        """ 070A - Getting square footage """
        self.assertEqual(self.detached_home.get_number_of_bathrooms(), 3, "Detached Home must have valid number of bathrooms")

    def test_detached_home_get_city(self):
        """ 080A - Getting city """
        self.assertEqual(self.detached_home.get_city(), "Richmond", "Detached Home must have valid city")

    def test_detached_home_get_selling_agent(self):
        """ 090A - Getting selling agent """
        self.assertEqual(self.detached_home.get_selling_agent(), "Camelia Stewart", "Detached Home must have valid agent")

    def test_detached_home_get_yearly_property_tax(self):
        """ 100A - Getting yearly property tax """
        self.assertEqual(self.detached_home.get_yearly_property_tax(), 0.25, "Detached Home must have valid tax")

    def test_detached_home_get_type(self):
        """ 110A - Getting type """
        self.assertEqual(self.detached_home.get_type(), "detached home", "Detached Home must be a detached home")

    def test_detached_home_get_number_of_floors(self):
        """ 120A - Getting number of floors """
        self.assertEqual(self.detached_home.get_number_of_floors(), 3, "Detached Home must have valid Number of Floors")

    def test_detached_home_get_has_rental_suite(self):
        """ 130A - Getting whether it has a rental suite """
        self.assertEqual(self.detached_home.get_has_rental_suite(), True, "Detached Home must have valid Has Suite flag")

    def test_get_years_old_positive(self):
        """ 140A - Getting years old for a build year before current year """
        age = 2019 - 2010
        self.assertEqual(self.detached_home.get_years_old(), age)

    def test_get_years_old_non_positive(self):
        """ 140B - Getting years old for a build year on or after current year """
        detached_home1 = DetachedHome(12000, 2019, 18, 3, "Richmond", "Camelia Stewart", 0.25, 800, True)
        age1 = 2019 - 2019
        self.assertEqual(detached_home1.get_years_old(), age1)

        detached_home2 = DetachedHome(12000, 2099, 18, 3, "Richmond", "Camelia Stewart", 0.25, 800, True)
        age2 = 2019 - 2099
        self.assertEqual(detached_home2.get_years_old(), age2)

    def test_get_description(self):
        """ 150A - Getting the description """
        description = "This is a 12000 square foot home built in 2010 with 3 floors, 18 rooms, " + \
                        "3 bathrooms and a yearly property tax of 0.25. " + \
                        "This home is being sold by Camelia Stewart"
        self.assertEqual(self.detached_home.get_description(), description)

    def test_to_dict(self):
        """ 160A - Getting the Python Dictionary representation """
        detached_home_dict = {
            "type": "detached home",
            "square_feet": 12000,
            "year_built": 2010,
            "rooms": 18,
            "bathrooms": 3,
            "city": "Richmond",
            "seller": "Camelia Stewart",
            "tax": 0.25,
            "floors": 3,
            "has_suite": True,
            }
        self.assertEqual(self.detached_home.to_dict(), detached_home_dict)

if __name__ == "__main__":
    unittest.main()