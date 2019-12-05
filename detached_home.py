from abstract_home import AbstractHome


class DetachedHome(AbstractHome):
    """ Child class of AbstractHome that creates a DetachedHome object """

    FLOORS_LABEL = "Number of Floors"
    HAS_SUITE_LABEL = "Has Suite"

    DETACHED_HOME_TYPE = 'detached home'

    def __init__(self, square_feet, year_built, rooms, bathrooms, city, seller, tax, floors, has_suite):
        """ Constructor for Condo object """
        super().__init__(square_feet, year_built, rooms, bathrooms, city, seller, tax)

        AbstractHome._validate_int_input(DetachedHome.FLOORS_LABEL, floors)
        self.number_of_floors = floors

        AbstractHome._validate_bool_input(DetachedHome.HAS_SUITE_LABEL, has_suite)
        self.has_rental_suite = has_suite

    # def get_number_of_floors(self):
    #     """ Returns the number of floors for a DetachedHome object """
    #     return self._number_of_floors

    # def get_has_rental_suite(self):
    #     """ Returns boolean for if a home has a rental suite """
    #     return self._has_rental_suite

    def get_description(self):
        """ Returns a description of a DetachedHome object with details relevant to buyers and seller """
        description = "This is a " + str(self._square_footage) + " square foot home " + "built in " + str(self._year_built)\
            + " " + "with " + str(self._number_of_floors) + " floors, " + str(self._number_of_rooms) + " rooms, "\
            + str(self._number_of_bathrooms) + " bathrooms"\
            + " and a yearly property tax of " + str(self._yearly_property_tax) + ". This home is being sold by "\
            + self._selling_agent
        return description

    def get_type(self):
        """ Return type of a DetachedHome Object """
        return DetachedHome.DETACHED_HOME_TYPE

    def to_dict(self):
        """ Get a Python Dictionary representation of the Detached Home """
        detached_home_dict = dict()
        detached_home_dict["square_feet"] = int(self.square_footage)
        detached_home_dict["year_built"] = int(self.year_built)
        detached_home_dict["number_of_rooms"] = int(self.number_of_rooms)
        detached_home_dict["number_of_bathrooms"] = int(self.number_of_bathrooms)
        detached_home_dict["city"] = str(self.city)
        detached_home_dict["selling_agent"] = str(self.selling_agent)
        detached_home_dict["yearly_property_tax"] = float(self.yearly_property_tax)
        detached_home_dict["number_of_floors"] = int(self.number_of_floors)
        detached_home_dict["has_rental_suite"] = bool(self.has_rental_suite)
        detached_home_dict["type"] = self.get_type()
        detached_home_dict["id"] = int(self.id)
        # if self.get_id() is not None:
            # detached_home_dict["id"] = self.get_id()
            
        return detached_home_dict