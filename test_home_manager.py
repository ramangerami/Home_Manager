import unittest
# from unittest.mock import patch, mock_open
import inspect
from abstract_home import AbstractHome
from detached_home import DetachedHome
from condo import Condo
from home_manager import HomeManager

from sqlalchemy import create_engine
from base import Base
import os

class TestCondo(unittest.TestCase):
    """ Unit Tests for the Home Manager """

    # @patch('builtins.open', mock_open(read_data='{}'))
    def setUp(self):
        """ Creates a test database before each method is run """
        self.db_filename = "test_homes"
        self.db_filename += ".sqlite"
        engine = create_engine("sqlite:///"+self.db_filename)

        # Creates all the tables
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self.condo1 = Condo(1, 6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, 0)
        self.condo2 = Condo(3, 7000, 2012, 5, 6, "White Rock", "Betty Anderson", 8.0, 120, 1)
        self.condo3 = Condo(5, 15000, 2019, 8, 12, "Surrey", "Kyle Moignahan", 1.5, 1357, 0)

        self.detached_home1 = DetachedHome(2, 12000, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, 3, 1)
        self.detached_home2 = DetachedHome(4, 800, 1990, 18, 1, "West Vancouver", "Spaghetti Alfredo", 5.0, 6, 0)
        self.detached_home3 = DetachedHome(6, 9500, 2019, 2, 0, "Coquitlam", "John Smiff", 1.3, 10, 1)

        # self.filename = "home_records.txt"
        self.home_manager = HomeManager(self.db_filename)
        self.assertIsNotNone(self.home_manager, "Home Manager must be defined.")

        self.logPoint()
    
    def tearDown(self):
        """ Resets the variables and deletes test database after each method is run """
        print("deleting file:", self.db_filename)
        os.remove(self.db_filename)
        self.logPoint()


    def logPoint(self):
        """ Prints the current running method as it is running """
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_home_manager_constructor(self):
        """ 010A - Valid construction """
        self.assertIsNotNone(self.home_manager, "Home Manager must be defined.")
        self.assertIsInstance(self.home_manager, HomeManager, "Home Manager must be an instance of HomeManager.")

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_home_manager_constructor_invalid(self):
        """ 010B - Invalid filename construction """
        undefined_input = None
        self.assertRaisesRegex(ValueError, "Database File name cannot be undefined.", HomeManager, undefined_input)

        empty_input = ""
        self.assertRaisesRegex(ValueError, "Database File name cannot be empty string", HomeManager, empty_input)

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_add_home_valid(self):
        """ 020A - Adding valid home objects """
        self.assertEqual(self.home_manager.get_all_homes(), [])
        self.home_manager.add_home(self.condo1)
        self.assertEqual(len(self.home_manager.get_all_homes()), len([self.condo1]))
        self.assertEqual(self.home_manager.get_home_by_id(1).home_id, 1)
        self.home_manager.add_home(self.detached_home1)
        self.assertEqual(self.home_manager.get_home_by_id(2).home_id, 2)
        self.assertEqual(len(self.home_manager.get_all_homes()), len([self.condo1, self.detached_home1]))
        self.home_manager.add_home(self.condo2)
        self.assertEqual(len(self.home_manager.get_all_homes()), len([self.condo1, self.detached_home1, self.condo2]))
        self.assertEqual(self.home_manager.get_home_by_id(3).home_id, 3)

    # @patch('builtins.open', mock_open(read_data='{}'))
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

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_get_home_by_id_valid_is_in(self):
        """ 030A - Getting home that is in listing with a valid id """
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)
        
        self.assertEqual(self.home_manager.get_home_by_id(1).home_id, 1)
        self.assertEqual(self.home_manager.get_home_by_id(3).home_id, 3)
        self.assertEqual(self.home_manager.get_home_by_id(2).home_id, 2)

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_get_home_by_id_valid_not_in(self):
        """ 030B - Getting home that is not in listing with a valid id """
        self.assertIsNone(self.home_manager.get_home_by_id(0))
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)
        self.assertIsNone(self.home_manager.get_home_by_id(0))
        self.assertIsNone(self.home_manager.get_home_by_id(-2))
        self.assertIsNone(self.home_manager.get_home_by_id(300))

    # @patch('builtins.open', mock_open(read_data='{}'))
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

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_get_all_homes_full(self):
        """ 040A - Getting all homes of a populated home manager """
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.condo2)
        self.home_manager.add_home(self.detached_home1)

        all_homes = self.home_manager.get_all_homes()
        self.assertEqual(all_homes[2].home_id, 2)
        self.assertEqual(len(all_homes), 3)


    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_get_all_homes_empty(self):
        """ 040B - Getting all homes of an empty home manager """
        all_homes = self.home_manager.get_all_homes()
        self.assertEqual(all_homes, [])
        self.assertEqual(len(all_homes), 0)
        
    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_get_all_homes_by_type_full(self):
        """ 050A - Getting all homes of valid type of a populated home manager """
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.condo2)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.detached_home3)
        self.home_manager.add_home(self.detached_home2)

        condos = self.home_manager.get_all_homes_by_type("condo")
        self.assertEqual(condos[1].home_id, 3)
        self.assertEqual(len(condos), 2)
        detacheds = self.home_manager.get_all_homes_by_type("detached home")
        self.assertEqual(detacheds[2].home_id, 4)
        self.assertEqual(len(detacheds), 3)

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_get_all_homes_by_type_empty(self):
        """ 050B - Getting all homes of valid type of an empty home manager """
        condos = self.home_manager.get_all_homes_by_type("condo")
        detacheds = self.home_manager.get_all_homes_by_type("detached home")

        self.assertEqual(condos, [])
        self.assertEqual(len(condos), 0)

        self.assertEqual(detacheds, [])
        self.assertEqual(len(detacheds), 0)
        
    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_get_all_homes_by_type_invalid(self):
        """ 05BC - Getting all homes with invalid parameter """
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
    
        
    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_update_home_valid(self):
        """ 060A - Updating a home in the list """
        id = self.condo1.home_id
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home3)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo3)
        self.home_manager.add_home(self.detached_home2)

        # print("060A this is id", id)
        self.assertEqual(self.home_manager.get_home_by_id(id).home_id, 1)
        self.assertEqual(self.home_manager.get_home_by_id(id).city, "Vancouver")
        # self.condo2.set_id(id)
        self.condo2.home_id = id
        # print("060A this is id", self.condo2.home_id)

        self.home_manager.update_home(self.condo2)
        self.assertEqual(self.home_manager.get_home_by_id(id).city, "White Rock")

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_update_home_invalid(self):
        """ 060B - Updating an invalid home in the list """
        self.detached_home3.home_id = 1
        self.assertEqual(self.detached_home3.home_id, 1)

        # Must reject home that is not in the manager
        self.assertRaisesRegex(ValueError, "Given Home's ID must match one in the listings to update.", self.home_manager.update_home, self.detached_home3)
        
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)

        self.condo3.home_id = 5
        self.assertEqual(self.condo3.home_id, 5)
        # Must reject home that is not in the manager
        self.assertRaisesRegex(ValueError, "Given Home's ID must match one in the listings to update.", self.home_manager.update_home, self.condo3)

        undefined_input = None
        # Must reject undefined parameter
        self.assertRaisesRegex(ValueError, "Home object cannot be undefined", self.home_manager.update_home, undefined_input)
        self.assertRaisesRegex(ValueError, "Given Home's ID must match one in the listings to update.", self.home_manager.update_home, self.detached_home2)

        test_string = "Hello"
        # Must reject invalid parameter
        self.assertRaisesRegex(ValueError, "Home object must be a class that extends AbstractHome.", self.home_manager.update_home, test_string)
        
    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_delete_home_valid(self):
        """ 070A - Deleting a home in the list """
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)
        self.home_manager.add_home(self.detached_home2)

        all_homes = self.home_manager.get_all_homes()
        self.assertEqual(len(all_homes), 4)
        self.home_manager.delete_home(3)
        all_homes = self.home_manager.get_all_homes()
        self.assertEqual(len(all_homes), 3)
        self.home_manager.delete_home(1)
        all_homes = self.home_manager.get_all_homes()
        self.assertEqual(len(all_homes), 2)

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_delete_home_invalid(self):
        """ 070B - Deleting an invalid home in the list """

        # Must reject home that is not in the manager
        self.assertRaisesRegex(ValueError, "Given Home's ID must match one in the listings to delete.", self.home_manager.delete_home, 0)
        
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)

        # Must reject home that is not in the manager
        self.assertRaisesRegex(ValueError, "Given Home's ID must match one in the listings to delete.", self.home_manager.delete_home, 4)

        undefined_input = None
        # Must reject undefined parameter
        self.assertRaisesRegex(ValueError, "Home ID cannot be undefined", self.home_manager.delete_home, undefined_input)
        self.assertRaisesRegex(ValueError, "Given Home's ID must match one in the listings to delete.", self.home_manager.delete_home, self.detached_home2.home_id)

        test_string = "Hello"
        # Must reject invalid parameter
        self.assertRaisesRegex(ValueError, "Home ID must be of type: Integer", self.home_manager.delete_home, test_string)
        
    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_get_listing_stats_full(self):
        """ 080A - Getting the stats of a populated manager """
        self.home_manager.add_home(self.condo1)
        self.home_manager.add_home(self.detached_home3)
        self.home_manager.add_home(self.detached_home1)
        self.home_manager.add_home(self.condo2)
        self.home_manager.add_home(self.detached_home2)

        stats = self.home_manager.get_listing_stats()

        self.assertEqual(stats.get_total_num_homes(), 5)
        self.assertEqual(stats.get_num_detached_homes(), len(self.home_manager.get_all_homes_by_type("detached home")))
        self.assertEqual(stats.get_num_condos(), len(self.home_manager.get_all_homes_by_type("condo")))
        self.assertEqual(stats.get_avg_years_old(), 13)

    # @patch('builtins.open', mock_open(read_data='{}'))
    def test_get_listing_stats_empty(self):
        """ 080B - Getting the stats of an empty manager """
        stats = self.home_manager.get_listing_stats()

        self.assertEqual(stats.get_total_num_homes(), 0)
        self.assertEqual(stats.get_num_detached_homes(), 0)
        self.assertEqual(stats.get_num_condos(), 0)
        self.assertEqual(stats.get_avg_years_old(), 0)

        
        
if __name__ == "__main__":
    unittest.main()