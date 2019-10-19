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
        self.assertEqual(self.condo.get_type(), "condo", "Condo be a condo")
        self.assertEqual(self.condo.get_monthly_strata_fee(), 800, "Condo must have valid monthly fee")
        self.assertEqual(self.condo.get_pets_allowed(), False, "Condo must have valid pets allowed flag")

    def test_condo_constructor_invalid(self):
        """ 010B - Invalid constructor parameters """
        pass

if __name__ == "__main__":
    unittest.main()