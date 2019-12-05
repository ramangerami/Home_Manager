from sqlalchemy import Column, String, Integer, Float, DateTime
from base import Base

class AbstractHome(Base):
    """ Representation of a home object, with relevant details to buyers/sellers """
    
    HOME_ID_LABEL = "Home ID"
    SQUARE_FOOTAGE_LABEL = "Square Footage"
    YEAR_BUILD_LABEL = "Year Build"
    NUM_ROOMS_LABEL = "Number of Rooms"
    NUM_BATHROOMS_LABEL = "Number of Bathrooms"
    CITY_LABEL = "City Name"
    SELLING_AGENT_LABEL = "Selling Agent Name"
    YEARLY_TAX_LABEL = "Yearly Property Tax"

    CURRENT_YEAR = 2019

    def __init__(self,square_feet, year_built, rooms, bathrooms, city, seller, tax):
        """ Constructor for an Abstract Home Object """

        AbstractHome._validate_int_input(AbstractHome.SQUARE_FOOTAGE_LABEL, square_feet)
        self.square_footage = square_feet

        AbstractHome._validate_int_input(AbstractHome.YEAR_BUILD_LABEL, year_built)
        self.year_built = year_built

        AbstractHome._validate_int_input(AbstractHome.NUM_ROOMS_LABEL, rooms)
        self.number_of_rooms = rooms

        AbstractHome._validate_int_input(AbstractHome.NUM_BATHROOMS_LABEL, bathrooms)
        self.number_of_bathrooms = bathrooms

        AbstractHome._validate_string_input(AbstractHome.CITY_LABEL, city)
        self.city = city

        AbstractHome._validate_string_input(AbstractHome.SELLING_AGENT_LABEL, seller)
        self.selling_agent = seller

        AbstractHome._validate_float_input(AbstractHome.YEARLY_TAX_LABEL, tax)
        self.yearly_property_tax = tax

        self.home_id = None

# All entity attributes are public (as per SQLAlchemy)
# so getter and setter methods are no longer required
    # def get_id(self):
    #     """ Returns id of a home object """
    #     return self._home_id

    # def set_id(self, home_id):
    #     """ Sets the id of a home object """
    #     AbstractHome._validate_int_input(AbstractHome.HOME_ID_LABEL, home_id)
    #     self._home_id = home_id

    # def get_square_footage(self):
    #     """ Returns square footage of a home object """
    #     return self._square_footage

    # def get_year_built(self):
    #     """ Return year a home object was built """
    #     return self._year_built

    # def get_number_of_rooms(self):
    #     """ Returns number of rooms of a home object """
    #     return self._number_of_rooms

    # def get_number_of_bathrooms(self):
    #     """ Returns number of bathrooms of a home object """
    #     return self._number_of_bathrooms

    # def get_city(self):
    #     """ Returns city of a home object """
    #     return self._city

    # def get_selling_agent(self):
    #     """ Returns selling agent of a home object """
    #     return self._selling_agent

    # def get_yearly_property_tax(self):
    #     """ Returns the yearly tax of a home object """
    #     return self._yearly_property_tax
#/ All entity attributes are public (as per SQLAlchemy)
#/ so getter and setter methods are no longer required

    def get_years_old(self):
        """ Returns the age of a home object, assuming the current year is 2019 """
        years_old = AbstractHome.CURRENT_YEAR - self.get_year_built()
        return years_old

    def get_description(self):
        """ Returns description of a home object with relevant details to a buyer/seller """
        raise NotImplemented("Method must be implemented")

    def get_type(self):
        """ Returns the type of a home object """
        raise NotImplemented("Method must be implemented")

    def to_dict(self):
        """ Abstract method to return a Dictionary representation of the Home """
        raise NotImplementedError("Subclass must implement abstract method")

    @classmethod
    def _validate_general_input(cls, display_name, val):
        """ Used to validate a variable for not being None """
        if val is None:
            raise ValueError(display_name + " cannot be undefined.")

    @classmethod
    def _validate_string_input(cls, display_name, str_val):
        """ Used to validate a string variable """
        cls._validate_general_input(display_name, str_val)
        if type(str_val) is not str:
            raise ValueError(display_name + " must be of type: String.")
        if str_val == "":
            raise ValueError(display_name + " cannot be empty string.")

    @classmethod
    def _validate_float_input(cls, display_name, flt_val):
        """ Used to validate a float variable """
        cls._validate_general_input(display_name, flt_val)
        if type(flt_val) is not float:
            raise ValueError(display_name + " must be of type: Float.")

    @classmethod
    def _validate_int_input(cls, display_name, int_val):
        """ Used to validate a integer variable """
        cls._validate_general_input(display_name, int_val)
        if type(int_val) is not int:
            raise ValueError(display_name + " must be of type: Integer.")

    @classmethod
    def _validate_bool_input(cls, display_name, bool_val):
        """ Used to validate a boolean variable """
        cls._validate_general_input(display_name, bool_val)
        if type(bool_val) is not bool:
            raise ValueError(display_name + " must be of type: Boolean.")