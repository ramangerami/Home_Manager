from home_stats import HomeStats

class HomeManager:
    """ Manages Home Objects """

    HOME_OBJECT_LABEL = "Home object"
    HOME_ID_LABEL = "Home ID"
    HOME_TYPE_LABEL = "Type of Home"

    def __init__(self):
        """ Constructor for a HomeManager Object """
        self._home_listings = []
        self._next_available_id = 0

    def add_home(self, home):
        """ Adds a home to the listings, assigning it a unique id """
        HomeManager._validate_home_input(HomeManager.HOME_OBJECT_LABEL, home)
        home.set_id(self._next_available_id)
        self._home_listings.append(home)
        self._next_available_id += 1


    def get_home_by_id(self, id_number):
        """ Returns a home in the listings based on id, returns none if it doesn't exist in the listings """
        HomeManager._validate_int_input(HomeManager.HOME_ID_LABEL, id_number)
        for home in self._home_listings:
            if home.get_id() == id_number:
                return home
        # return next((home for home in self._home_listings if home.get_id() == id_number), None)
        return None

    def get_all_homes(self):
        """ Returns list of all homes """
        return self._home_listings

    def get_all_homes_by_type(self, home_type):
        """ Returns a list of homes by specific type """
        HomeManager._validate_string_input(HomeManager.HOME_TYPE_LABEL, home_type)
        results = []
        for home in self._home_listings:
            if home.get_type() == home_type:
                results.append(home)
        return results

    def update_home(self, replacement_home):
        """ Takes a home object and replaces an existing home object with the same id """
        HomeManager._validate_home_input(HomeManager.HOME_OBJECT_LABEL, replacement_home)
        if self.get_home_by_id(replacement_home.get_id()) is None:
            raise ValueError("Given Home's ID must match one in the listings to update.")
        for i in range(0, len(self._home_listings)):
            if self._home_listings[i].get_id() == replacement_home.get_id():
                self._home_listings[i] = replacement_home
                return self._home_listings[i]
        # next((home for home in self._home_listings if home.get_id() == replacement_home.get_id()), ValueError("Home with same ID was not found"))
        return None

    def delete_home(self, home_id):
        """ Deletes a home from the manager, based on the id """
        HomeManager._validate_int_input(HomeManager.HOME_ID_LABEL, home_id)
        if self.get_home_by_id(home_id) is None:
            raise ValueError("Given Home's ID must match one in the listings to delete.")
        for home in self._home_listings:
            if home.get_id() == home_id:
                self._home_listings.remove(home)
                break

                
                
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
    def _validate_int_input(cls, display_name, int_val):
        """ Used to validate a integer variable """
        cls._validate_general_input(display_name, int_val)
        if type(int_val) is not int:
            raise ValueError(display_name + " must be of type: Integer.")

    @classmethod
    def _validate_home_input(cls, display_name, home_val):
        """ Used to validate a variable is an instance of a class that extends AbstractHome """
        cls._validate_general_input(display_name, home_val)
        if not isinstance(type(home_val), AbstractHome):
            raise ValueError(display_name + " must be a class that extends AbstractHome.")