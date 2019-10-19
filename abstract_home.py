class AbstractHome:
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
        AbstractHome._validate_int_input(AbstractHome.YEAR_BUILD_LABEL, year_built)
        AbstractHome._validate_int_input(AbstractHome.NUM_ROOMS_LABEL, rooms)
        AbstractHome._validate_int_input(AbstractHome.YEAR_BUILD_LABEL, bathrooms)
        AbstractHome._validate_string_input(AbstractHome.CITY_LABEL, city)
        AbstractHome._validate_string_input(AbstractHome.SELLING_AGENT_LABEL, seller)
        AbstractHome._validate_float_input(AbstractHome.YEARLY_TAX_LABEL, tax)

        self._square_footage = square_feet
        self._year_built = year_built
        self._number_of_rooms = rooms
        self._number_of_bathrooms = bathrooms
        self._city = city
        self._selling_agent = seller
        self._yearly_property_tax = tax

        self._home_id = None

    def get_id(self):
        """ Returns id of a home object """
        return self._home_id

    def set_id(self, home_id):
        """ Sets the id of a home object """
        AbstractHome._validate_int_input(AbstractHome.HOME_ID_LABEL, home_id)
        self._home_id = home_id

    def get_square_footage(self):
        """ Returns square footage of a home object """
        return self._square_footage

    def get_year_built(self):
        """ Return year a home object was built """
        return self._year_built

    def get_number_of_rooms(self):
        """ Returns number of rooms of a home object """
        return self._number_of_rooms

    def get_number_of_bathrooms(self):
        """ Returns number of bathrooms of a home object """
        return self._number_of_bathrooms

    def get_city(self):
        """ Returns city of a home object """
        return self._city

    def get_selling_agent(self):
        """ Returns selling agent of a home object """
        return self._selling_agent

    def get_yearly_property_tax(self):
        """ Returns the yearly tax of a home object """
        return self._yearly_property_tax

    def get_years_old(self):
        """ Returns the age of a home object, assuming the current year is 2019 """
        years_old = self.get_year_built() - AbstractHome.CURRENT_YEAR
        return years_old

    def get_description(self):
        """ Returns description of a home object with relevant details to a buyer/seller """
        raise NotImplemented("Method must be implemented")

    def get_type(self):
        """ Returns the type of a home object """
        raise NotImplemented("Method must be implemented")

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
             
    @classmethod
    def _validate_home_input(cls, display_name, home_val):
        """ Used to validate a variable is an instance of a class that extends AbstractHome """
        cls._validate_general_input(display_name, home_val)
        if not isinstance(type(home_val), AbstractHome):
            raise ValueError(display_name + " must be a class that extends AbstractHome.")
             
    # kev - I commented your old validators and made new ones that give more detailed error messages
    
    # @staticmethod
    # def _validate_string(x):
    #     """ Used to validate a string variable """
    #     if x is None or type(x) != str:
    #         raise ValueError("Must be a non-empty string")

    # @staticmethod
    # def _validate_float(x):
    #     """ Used to validate a float variable """
    #     if x is None or type(x) != float:
    #         raise ValueError("Must be a non-empty float")

    # @staticmethod
    # def _validate_int(x):
    #     """ Used to validate an int variable """
    #     if x is None or type(x) != int:
    #         raise ValueError("Must be a non-empty int")

    # @staticmethod
    # def _validate_boolean(x):
    #     """ Used to validate a boolean variable """
    #     if x is None or type(x) != bool:
    #         raise ValueError("Must be a valid Boolean value")

    # @staticmethod
    # def _validate_home(x):
    #     """ Used to validate Vehicle objects """
    #     if x is None or type(x) != AbstractHome:
    #         raise ValueError("Must be a Vehicle object")