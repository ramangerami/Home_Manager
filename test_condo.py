import unittest
import inspect
from abstract_home import AbstractHome
from condo import Condo


class TestCondo(unittest.TestCase):
    """ Unit Tests for the Condo class """

    def setUp(self):
        """ Creates a test fixture before each method is run """
        self.condo = Condo(6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.assertIsNotNone(self.condo, "Condo must be defined.")
        self.logPoint()
    
    def tearDown(self):
        """ Resets the variables after each method is run """
        self.logPoint()

    def logPoint(self):
        """ Prints the current running method as it is running """
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_condo_constructor_valid(self):
        """ 010A - Valid constructor parameters """
        self.assertEqual(self.condo.get_square_footage(), 6000, "Condo must have valid square footage")
        self.assertEqual(self.condo.get_year_built(), 1999, "Condo must have valid year built")
        self.assertEqual(self.condo.get_number_of_rooms(), 4, "Condo must have valid number of rooms")
        self.assertEqual(self.condo.get_number_of_bathrooms(), 2, "Condo must have valid number of bathrooms")
        self.assertEqual(self.condo.get_city(), "Vancouver", "Condo must have valid city")
        self.assertEqual(self.condo.get_selling_agent(), "Adrian Gekko", "Condo must have valid agent")
        self.assertEqual(self.condo.get_yearly_property_tax(), 12.5, "Condo must have valid tax")
        self.assertEqual(self.condo.get_type(), "condo", "Condo must be a condo")
        self.assertEqual(self.condo.get_monthly_strata_fee(), 800, "Condo must have valid monthly fee")
        self.assertEqual(self.condo.get_pets_allowed(), False, "Condo must have valid pets allowed flag")

    def test_condo_constructor_undefined(self):
        """ 010B - Invalid undefined None constructor parameters """
        undefined_input = None
        # Must reject undefined parameter
        self.assertRaisesRegex(ValueError, "Square Footage cannot be undefined", Condo, undefined_input, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Year Build cannot be undefined", Condo, 6000, undefined_input, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Number of Rooms cannot be undefined", Condo, 6000, 1999, undefined_input, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Number of Bathrooms cannot be undefined", Condo, 6000, 1999, 4, undefined_input, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "City Name cannot be undefined", Condo, 6000, 1999, 4, 2, undefined_input, "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Selling Agent Name cannot be undefined", Condo, 6000, 1999, 4, 2, "Vancouver", undefined_input, 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Yearly Property Tax cannot be undefined", Condo, 6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", undefined_input, 800, False)
        self.assertRaisesRegex(ValueError, "Monthly Fee cannot be undefined", Condo, 6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, undefined_input, False)
        self.assertRaisesRegex(ValueError, "Pets Allowed cannot be undefined", Condo, 6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, undefined_input)
    
    def test_condo_constructor_invalid(self):
        """ 010C - Invalid other constructor parameters """
        test_string = "Hello"
        test_int = 5
        # Must reject parameter of incorrect type
        self.assertRaisesRegex(ValueError, "Square Footage must be of type: Integer", Condo, test_string, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Year Build must be of type: Integer", Condo, 6000, test_string, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Number of Rooms must be of type: Integer", Condo, 6000, 1999, test_string, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Number of Bathrooms must be of type: Integer", Condo, 6000, 1999, 4, test_string, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "City Name must be of type: String", Condo, 6000, 1999, 4, 2, test_int, "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Selling Agent Name must be of type: String", Condo, 6000, 1999, 4, 2, "Vancouver", test_int, 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Yearly Property Tax must be of type: Float", Condo, 6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", test_string, 800, False)
        self.assertRaisesRegex(ValueError, "Monthly Fee must be of type: Integer", Condo, 6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, test_string, False)
        self.assertRaisesRegex(ValueError, "Pets Allowed must be of type: Boolean", Condo, 6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, test_string)

        empty_string = ""
        # Must reject parameter of empty string
        self.assertRaisesRegex(ValueError, "City Name cannot be empty string.", Condo, 6000, 1999, 4, 2, empty_string, "Adrian Gekko", 12.5, 800, False)
        self.assertRaisesRegex(ValueError, "Selling Agent Name cannot be empty string.", Condo, 6000, 1999, 4, 2, "Vancouver", empty_string, 12.5, 800, False)

    def test_condo_get_id_unset(self):
        """ 020A - Get id of an unset home """
        self.assertIsNone(self.condo.get_id())
        
    def test_condo_get_id_set(self):
        """ 020B - Get id of an set home """
        test_id = 1
        self.condo.set_id(test_id)
        self.assertEqual(self.condo.get_id(), test_id)
        
    def test_condo_set_id_unset_valid(self):
        """ 030A - Set an id for a home that has not been set """
        test_id = 2
        self.assertIsNone(self.condo.get_id())
        self.condo.set_id(test_id)
        self.assertEqual(self.condo.get_id(), test_id)
        
    def test_condo_set_id_set_valid(self):
        """ 030B - Set an id for a home that already has an id set """
        test_id1 = 5
        test_id2 = 9
        self.condo.set_id(test_id1)
        self.assertEqual(self.condo.get_id(), test_id1)
        self.condo.set_id(test_id2)
        self.assertEqual(self.condo.get_id(), test_id2)

    def test_condo_set_id_set_valid(self):
        """ 030C - Setting an id with invalid parameters """
        undefined_input = None
        # Must reject invalid parameters
        self.assertRaisesRegex(ValueError, "Home ID cannot be undefined", self.condo.set_id, undefined_input)
        test_string = "Hello"
        self.assertRaisesRegex(ValueError, "Home ID must be of type: Integer", self.condo.set_id, test_string)

    def test_condo_get_square_footage(self):
        """ 040A - Getting square footage """
        self.assertEqual(self.condo.get_square_footage(), 6000, "Condo must have valid square footage")

    def test_condo_get_year_built(self):
        """ 050A - Getting year built """
        self.assertEqual(self.condo.get_year_built(), 1999, "Condo must have valid year built")

    def test_condo_get_number_of_rooms(self):
        """ 060A - Getting square footage """
        self.assertEqual(self.condo.get_number_of_rooms(), 4, "Condo must have valid number of rooms")

    def test_condo_get_number_of_bathrooms(self):
        """ 070A - Getting square footage """
        self.assertEqual(self.condo.get_number_of_bathrooms(), 2, "Condo must have valid number of bathrooms")

    def test_condo_get_city(self):
        """ 080A - Getting city """
        self.assertEqual(self.condo.get_city(), "Vancouver", "Condo must have valid city")

    def test_condo_get_selling_agent(self):
        """ 090A - Getting selling agent """
        self.assertEqual(self.condo.get_selling_agent(), "Adrian Gekko", "Condo must have valid agent")

    def test_condo_get_yearly_property_tax(self):
        """ 100A - Getting yearly property tax """
        self.assertEqual(self.condo.get_yearly_property_tax(), 12.5, "Condo must have valid tax")

    def test_condo_get_type(self):
        """ 110A - Getting type """
        self.assertEqual(self.condo.get_type(), "condo", "Condo must be a condo")

    def test_condo_get_monthly_strata_fee(self):
        """ 120A - Getting strata fee """
        self.assertEqual(self.condo.get_monthly_strata_fee(), 800, "Condo must have valid monthly fee")

    def test_condo_get_pets_allowed(self):
        """ 130A - Getting whether pets are allowed """
        self.assertEqual(self.condo.get_pets_allowed(), False, "Condo must have valid pets allowed flag")

    def test_get_years_old_positive(self):
        """ 140A - Getting years old for a build year before current year """
        age = 2019 - 1999
        self.assertEqual(self.condo.get_years_old(), age)

    def test_get_years_old_non_positive(self):
        """ 140B - Getting years old for a build year on or after current year """
        condo1 = Condo(6000, 2019, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        age1 = 2019 - 2019
        self.assertEqual(condo1.get_years_old(), age1)

        condo2 = Condo(6000, 2099, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        age2 = 2019 - 2099
        self.assertEqual(condo2.get_years_old(), age2)

    def test_get_description(self):
        """ 150A - Getting the description """
        description = "This is a 6000 square foot condo built in 1999 with 4 rooms, " + \
                        "2 bathrooms and a monthly strata fee of 800. " + \
                        "This home is being sold by Adrian Gekko"
        self.assertEqual(self.condo.get_description(), description)

if __name__ == "__main__":
    unittest.main()