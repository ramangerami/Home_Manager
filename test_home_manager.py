import unittest
import inspect
from abstract_home import AbstractHome
from detached_home import DetachedHome
from condo import Condo
from home_manager import HomeManager

class TestCondo(unittest.TestCase):
    """ Unit Tests for the Home Manager """

    def setUp(self):
        """ Creates a test fixture before each method is run """
        self.condo1 = Condo(6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.condo2 = Condo(7000, 2012, 5, 6, "White Rock", "Betty Anderson", 8.0, 120, True)
        self.condo3 = Condo(15000, 2019, 8, 12, "Surrey", "Kyle Moignahan", 1.5, 1357, False)

        self.detached_home1 = DetachedHome(12000, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, 3, True)
        self.detached_home2 = DetachedHome(800, 1990, 18, 1, "West Vancouver", "Spaghetti Alfredo", 5.0, 6, False)
        self.detached_home3 = DetachedHome(9500, 2019, 2, 0, "Coquitlam", "John Smiff", 1.3, 10, True)

        self.home_manager = HomeManager()
        self.assertIsNotNone(self.home_manager, "Home Manager must be defined.")

        self.logPoint()
    
    def tearDown(self):
        """ Resets the variables after each method is run """
        self.logPoint()

    def logPoint(self):
        """ Prints the current running method as it is running """
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_home_manager_constructor(self):
        """ 010A - Valid construction """
        self.assertIsNotNone(self.home_manager, "Home Manager must be defined.")
        self.assertIsInstance(self.home_manager, HomeManager, "Home Manager must be an instance of HomeManager.")

    def test_add_home_valid(self):
        """ 020A - Adding valid home objects """
        self.assertEqual(self.home_manager.get_all_homes(), [])
        self.home_manager.add_home(self.condo1)
        self.assertEqual(self.home_manager.get_all_homes(), [self.condo1])
        self.assertEqual(self.home_manager.get_home_by_id(0), self.condo1)
        self.home_manager.add_home(self.detached_home1)
        self.assertEqual(self.home_manager.get_home_by_id(1), self.detached_home1)
        self.assertEqual(self.home_manager.get_all_homes(), [self.condo1, self.detached_home1])
        self.home_manager.add_home(self.condo2)
        self.assertEqual(self.home_manager.get_all_homes(), [self.condo1, self.detached_home1, self.condo2])
        self.assertEqual(self.home_manager.get_home_by_id(2), self.condo2)

    def test_add_home_invalid(self):
        """ 020B - Adding invalid home objects """
        undefined_input = None
        # Must reject undefined parameter
        self.assertRaisesRegex(ValueError, "Home object cannot be undefined", self.home_manager.add_home, undefined_input)
        self.assertIsNone(self.home_manager.get_home_by_id(0))

        test_string = "Hello"
        # Must reject invalid parameter type
        self.assertRaisesRegex(ValueError, "Home object must be a class that extends AbstractHome.", self.home_manager.add_home, test_string)
        self.assertIsNone(self.home_manager.get_home_by_id(0))

    def test_get_home_by_id_valid_is_in(self):
        """ 030A - Getting home that is in listing with a valid id """
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)
        
        self.assertEqual(self.home_manager.get_home_by_id(0), self.condo1)
        self.assertEqual(self.home_manager.get_home_by_id(2), self.condo2)
        self.assertEqual(self.home_manager.get_home_by_id(1), self.detached_home1)

    def test_get_home_by_id_valid_not_in(self):
        """ 030B - Getting home that is not in listing with a valid id """
        self.assertIsNone(self.home_manager.get_home_by_id(0))
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)
        self.assertIsNone(self.home_manager.get_home_by_id(3))
        self.assertIsNone(self.home_manager.get_home_by_id(-2))
        self.assertIsNone(self.home_manager.get_home_by_id(300))

    def test_get_home_by_id_invalid(self):
        """ 030C - Getting home with invalid id """
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)

        undefined_input = None
        # Must reject undefined parameter
        self.assertRaisesRegex(ValueError, "Home ID cannot be undefined", self.home_manager.get_home_by_id, undefined_input)

        test_string = "Hello"
        # Must reject invalid parameter
        self.assertRaisesRegex(ValueError, "Home ID must be of type: Integer", self.home_manager.get_home_by_id, test_string)

    def test_get_all_homes_full(self):
        """ 040A - Getting all homes of a populated home manager """
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.condo2)
        self.home_manager.add_home(self.detached_home1)

        all_homes = self.home_manager.get_all_homes()
        self.assertEqual(all_homes, [self.condo1, self.condo2, self.detached_home1])
        self.assertEqual(len(all_homes), 3)


    def test_get_all_homes_empty(self):
        """ 040B - Getting all homes of an empty home manager """
        all_homes = self.home_manager.get_all_homes()
        self.assertEqual(all_homes, [])
        self.assertEqual(len(all_homes), 0)
        
    def test_get_all_homes_by_type_full(self):
        """ 050B - Getting all homes of valid type of a populated home manager """
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.condo2)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.detached_home3)
        self.home_manager.add_home(self.detached_home2)

        condos = self.home_manager.get_all_homes_by_type("condo")
        self.assertEqual(condos, [self.condo1, self.condo2])
        self.assertEqual(len(condos), 2)
        detacheds = self.home_manager.get_all_homes_by_type("detached home")
        self.assertEqual(detacheds, [self.detached_home1, self.detached_home3, self.detached_home2])
        self.assertEqual(len(detacheds), 3)

    def test_get_all_homes_by_type_empty(self):
        """ 050B - Getting all homes of valid type of an empty home manager """
        condos = self.home_manager.get_all_homes_by_type("condo")
        detacheds = self.home_manager.get_all_homes_by_type("detached home")

        self.assertEqual(condos, [])
        self.assertEqual(len(condos), 0)

        self.assertEqual(detacheds, [])
        self.assertEqual(len(detacheds), 0)
        
    def test_get_all_homes_by_type_invalid(self):
        """ 050B - Getting all homes with invalid parameter """
        undefined_input = None
        # Must reject undefined parameter
        self.assertRaisesRegex(ValueError, "Type of Home cannot be undefined", self.home_manager.get_all_homes_by_type, undefined_input)

        test_int = 25
        # Must reject invalid parameter
        self.assertRaisesRegex(ValueError, "Type of Home must be of type: String", self.home_manager.get_all_homes_by_type, test_int)

        empty_string = ""
        # Must reject empty string
        self.assertRaisesRegex(ValueError, "Type of Home cannot be empty string", self.home_manager.get_all_homes_by_type, empty_string)
        
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home3)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)
        self.home_manager.add_home(self.detached_home2)

        # Must reject undefined parameter
        self.assertRaisesRegex(ValueError, "Type of Home cannot be undefined", self.home_manager.get_all_homes_by_type, undefined_input)

        # Must reject invalid parameter
        self.assertRaisesRegex(ValueError, "Type of Home must be of type: String", self.home_manager.get_all_homes_by_type, test_int)

        # Must reject empty string
        self.assertRaisesRegex(ValueError, "Type of Home cannot be empty string", self.home_manager.get_all_homes_by_type, empty_string)
    



        
        
if __name__ == "__main__":
    unittest.main()