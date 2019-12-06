from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from home_stats import HomeStats
from abstract_home import AbstractHome
from detached_home import DetachedHome
from condo import Condo

# import json

class HomeManager:
    """ Manages Home Objects """

    HOME_OBJECT_LABEL = "Home object"
    HOME_ID_LABEL = "Home ID"
    HOME_TYPE_LABEL = "Type of Home"
    DB_FILE_NAME_LABEL = "Database File name"

    def __init__(self, db_filename):
    # def __init__(self):
        """ Constructor for a HomeManager Object """
        # self._home_listings = []
        # self._next_available_id = 0

        HomeManager._validate_string_input(HomeManager.DB_FILE_NAME_LABEL, db_filename)
        self._db_filename = db_filename

        # self._read_homes_from_file()

        # DB NAME should be a constructor param.
        # db_name = "PLACEHOLDER DATABASE NAME"
        # if db_name is None or db_name == "":
            # raise ValueError("DB Name cannot be undefined")

        engine = create_engine("sqlite:///" + self._db_filename)
        self._db_session = sessionmaker(bind=engine)
        # DB NAME should be a constructor param.

    def add_home(self, home):
        """ Adds a home to the listings, assigning it a unique id """
        HomeManager._validate_home_input(HomeManager.HOME_OBJECT_LABEL, home)
        # home.set_id(self._next_available_id)
    # home id is automatically added by sql
        # home.id = self._next_available_id
        # self._home_listings.append(home)

        # self._write_homes_to_file()
        session = self._db_session()

        session.add(home)
        session.commit()

        session.close()
        
        # self._next_available_id += 1
        # return self._next_available_id - 1

    def get_home_by_id(self, id_number):
        """ Returns a home in the listings based on id, returns none if it doesn't exist in the listings """
        HomeManager._validate_int_input(HomeManager.HOME_ID_LABEL, id_number)
        # for home in self._home_listings:
        #     # if home.get_id() == id_number:
        #     if home.id == id_number:
        #         return home
        # return next((home for home in self._home_listings if home.get_id() == id_number), None)
        session = self._db_session()

        home = session.query(Condo).filter(Condo.id == id_number).first()

        if home is None:
            home = session.query(DetachedHome).filter(DetachedHome.id == id_number).first()

        session.close() 

        # return None
        return home

    def get_all_homes(self):
        """ Returns list of all homes """
        # return self._home_listings
        homes_listings = []
        homes_listings.extend(self.get_all_homes_by_type("condo"))        
        homes_listings.extend(self.get_all_homes_by_type("detached home"))        
        return homes_listings


    def get_all_homes_by_type(self, home_type):
        """ Returns a list of homes by specific type """
        HomeManager._validate_string_input(HomeManager.HOME_TYPE_LABEL, home_type)
        if home_type not in ["condo", "detached home"]:
            raise ValueError("Home Type is invalid")
        results = []
        # for home in self._home_listings:
        #     if home.get_type() == home_type:
        #         results.append(home)
        # do i need to filter by type?
        if home_type == Condo.CONDO_TYPE:
            results = session.query(Condo).all()
        elif home_type == DetachedHome.DETACHED_HOME_TYPE:
            results = session.query(DetachedHome).all()
        # else:
        #     results = []

        session.close()
        return results

    def update_home(self, replacement_home):
        """ Takes a home object and replaces an existing home object with the same id """
        HomeManager._validate_home_input(HomeManager.HOME_OBJECT_LABEL, replacement_home)
        # if self.get_home_by_id(replacement_home.get_id()) is None:
        #TODO
        if self.get_home_by_id(replacement_home.id) is None:
            raise ValueError("Given Home's ID must match one in the listings to update.")
        session = self._db_session()

        home = session.query(Car).filter(Car.vin == vin).first()
        if home is None:
            home = session.query(Truck).filter(Truck.vin == vin).first()

        if home is None:
            session.close()
            raise ValueError("Could not find vehicle by VIN")

        vehicle.sell_vehicle(sold_price)
        session.commit()

        session.close()
        is_found = False
        for i in range(0, len(self._home_listings)):
            # if self._home_listings[i].get_id() == replacement_home.get_id():
            if self._home_listings[i].id == replacement_home.id:
                self._home_listings[i] = replacement_home
                # return self._home_listings[i]
                # self._write_homes_to_file()
                is_found = True
                break;
        # next((home for home in self._home_listings if home.get_id() == replacement_home.get_id()), ValueError("Home with same ID was not found"))
        # return None
        if not is_found:
            raise ValueError("Given Home's ID must match one in the listings to update.")


    def delete_home(self, home_id):
        """ Deletes a home from the manager, based on the id """
        HomeManager._validate_int_input(HomeManager.HOME_ID_LABEL, home_id)
        if self.get_home_by_id(home_id) is None:
            raise ValueError("Given Home's ID must match one in the listings to delete.")
        for home in self._home_listings:
            if home.get_id() == home_id:
                self._home_listings.remove(home)
                # self._write_homes_to_file()
                break

    def get_listing_stats(self):
        """ Generates a HomeStats from a listing of homes """
        total_homes = 0
        detached_homes = 0
        condos = 0
        years_list = []
        for home in self._home_listings:
            total_homes += 1
            years_list.append(home.get_years_old())
            if home.get_type() == DetachedHome.DETACHED_HOME_TYPE:
                detached_homes += 1
            elif home.get_type() == Condo.CONDO_TYPE:
                condos += 1
        years = 0
        if len(years_list) > 0:
            years = int(sum(years_list) / len(years_list))
        stats = HomeStats(total_homes, detached_homes, condos, years)
        return stats

# The _read_entities_from_file and _write_entities_to_file methods are no longer need
    # def _read_homes_from_file(self):
    #     """ Loads JSON Home record data from a file """
    #     with open(self._filepath, "r") as homes_file:
    #         list_of_homes = json.load(homes_file)
    #         for home in list_of_homes:
    #             if home["type"] == Condo.CONDO_TYPE:
    #                 condo = Condo(home["square_feet"], home["year_built"], home["number_of_rooms"], \
    #                         home["number_of_bathrooms"], home["city"], home["selling_agent"], home["yearly_property_tax"], \
    #                         home["monthly_strata_fee"], home["pets_allowed"])
    #                 self.add_home(condo)
    #             elif home["type"] == DetachedHome.DETACHED_HOME_TYPE:
    #                 detached_home = DetachedHome(home["square_feet"], home["year_built"], home["number_of_rooms"], \
    #                         home["number_of_bathrooms"], home["city"], home["selling_agent"], home["yearly_property_tax"], \
    #                         home["number_of_floors"], home["has_rental_suite"])
    #                 self.add_home(detached_home)
    #             else:
    #                 raise ValueError("Home type not recognized")
                
    # def _write_homes_to_file(self):
    #     """ Overwrites JSON Home record data to a file """
    #     with open(self._filepath, 'w') as homes_file:
    #         list_of_homes = list()
    #         for home in self._home_listings:
    #             list_of_homes.append(home.to_dict())
    #         json.dump(list_of_homes, homes_file) 

    #         # print(list_of_homes)
#/ The _read_entities_from_file and _write_entities_to_file methods are no longer need
                
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
        if not issubclass(type(home_val), AbstractHome):
            raise ValueError(display_name + " must be a class that extends AbstractHome.")