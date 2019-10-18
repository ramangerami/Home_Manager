class HomeManager:
    """ Manages Home Objects """

    def __init__(self):
        """ Constructor for a HomeManager Object """
        self._home_listings = []
        self._next_available_id = 0

    def add_home(self, home):
        """ Adds a home to the listings, assigning it a unique id """


    def get_home_by_id(self, id_number):
        """ Returns a home in the listings based on id, returns none if it doesn't exist in the listings """
        return next((home for home in self._home_listings if home.get_id() == id_number), None)

    def get_all_homes(self):
        """ Returns list of all homes """
        return self._home_listings

    def get_all_homes_by_type(self, home_type, home_list):
        """ Returns a list of homes by specific type """
        results = []
        for home in home_list:
            if home.get_type() == home_type:
                results.append(home)
        return results

    def update_home(self, replacement_home):
        """ Takes a home object and replaces an existing home object with the same id """
        next((home for home in self._home_listings if home.get_id() == replacement_home.get_id()), ValueError("Home with same ID was not found"))

    def delete_home(self, home_id):
        for home in self._home_listings:
            if home.get_id() == home_id:
                self._home_listings.remove(home)
