class AbstractHome:
    """ Representation of a home object, with relevant details to buyers/sellers """
    def __init__(self, home_id, square_feet, year_built, rooms, bathrooms, city, seller, tax ):
        """ Constructor for an Abstract Home Object """

        self._home_id = home_id
        self._square_footage = square_feet
        self._year_built = year_built
        self._number_of_rooms = rooms
        self._number_of_bathrooms = bathrooms
        self._city = city
        self._selling_agent = seller
        self._yearly_property_tax = tax

    def get_id(self):
        """ Returns id of a home object """
        return self._home_id

    def set_id(self, home_id):
        """ Sets the id of a home object """
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
        years_old = self.get_year_built() - 2019
        return -years_old

    def get_description(self):
        """ Returns description of a home object with relevant details to a buyer/seller """
        raise NotImplemented("Method must be implemented")

    def get_type(self):
        """ Returns the type of a home object """
        raise NotImplemented("Method must be implemented")

    @staticmethod
    def _validate_string(x):
        """ Used to validate a string variable """
        if x is None or type(x) != str:
            raise ValueError("Must be a non-empty string")

    @staticmethod
    def _validate_float(x):
        """ Used to validate a float variable """
        if x is None or type(x) != float:
            raise ValueError("Must be a non-empty float")

    @staticmethod
    def _validate_int(x):
        """ Used to validate an int variable """
        if x is None or type(x) != int:
            raise ValueError("Must be a non-empty int")

    @staticmethod
    def _validate_boolean(x):
        """ Used to validate a boolean variable """
        if x is None or type(x) != bool:
            raise ValueError("Must be a valid Boolean value")

    @staticmethod
    def _validate_vehicle(x):
        """ Used to validate Vehicle objects """
        if x is None or type(x) != AbstractHome:
            raise ValueError("Must be a Vehicle object")