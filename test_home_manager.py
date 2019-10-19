import unittest
import inspect
from abstract_home import AbstractHome
from detached_home import DetachedHome
from home_manager import HomeManager

class TestCondo(unittest.TestCase):
    """ Unit Tests for the Home Manager """

    def setUp(self):
        """ Creates a test fixture before each method is run """
        self.condo1 = Condo(6000, 1999, 4, 2, "Vancouver", "Adrian Gekko", 12.5, 800, False)
        self.condo2 = Condo(7000, 2012, 4, 2, "White Rock", "Adrian Gekko", 12.5, 800, False)
        self.condo3 = Condo(15000, 2019, 4, 2, "Surrey", "Adrian Gekko", 12.5, 800, False)

        self.detached_home1 = DetachedHome(12000, 2010, 18, 3, "Richmond", "Camelia Stewart", 0.25, 3, True)
        self.detached_home2 = DetachedHome(800, 1990, 18, 3, "West Vancouver", "Camelia Stewart", 0.25, 3, True)
        self.detached_home3 = DetachedHome(9500, 2019, 18, 3, "Coquitlam", "Camelia Stewart", 0.25, 3, True)

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