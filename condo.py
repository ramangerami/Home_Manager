from abstract_home import AbstractHome
from sqlalchemy import Column, String, Integer, Float, DateTime


class Condo(AbstractHome):
    """ Child class of AbstractHome that creates a Condo object """

    MONTHLY_FEE_LABEL = "Monthly Fee"
    PETS_ALLOWED_LABEL = "Pets Allowed"

    CONDO_TYPE = 'condo'

    # booleans are represented as Integer 0 and 1
    monthly_strata_fee = Column(Integer)
    pets_allowed = Column(Integer)

    def __init__(self, square_feet, year_built, rooms, bathrooms, city, seller, tax, monthly_fee, pets):
        """ Constructor for a Condo object """
        super().__init__(square_feet, year_built, rooms, bathrooms, city, seller, tax, Condo.CONDO_TYPE)

        AbstractHome._validate_int_input(Condo.MONTHLY_FEE_LABEL, monthly_fee)
        self.monthly_strata_fee = monthly_fee

        AbstractHome._validate_bool_input(Condo.PETS_ALLOWED_LABEL, pets)
        self.pets_allowed = pets

    # def get_monthly_strata_fee(self):
    #     """ Returns the monthly strata fee for a Condo """
    #     return self._monthly_strata_fee

    # def get_pets_allowed(self):
    #     """ Returns Boolean value for if pets are allowed in a Condo """
    #     return self._pets_allowed

    def get_description(self):
        """ Returns a description of a Condo object with details relevant to buyers and seller """
        description = "This is a " + str(self.square_footage) + " square foot condo " + "built in " + str(self.year_built)\
            + " " + "with " + str(self.number_of_rooms) + " rooms, "\
            + str(self.number_of_bathrooms) + " bathrooms"\
            + " and a monthly strata fee of " + str(self.monthly_strata_fee) + ". This home is being sold by "\
            + self.selling_agent
        return description

    def get_type(self):
        """ Returns the type of a Condo object """
        return Condo.CONDO_TYPE

    def to_dict(self):
        """ Get a Python Dictionary representation of the Condo """
        condo_dict = dict()
        condo_dict["square_feet"] = int(self.square_footage)
        condo_dict["year_built"] = int(self.year_built)
        condo_dict["number_of_rooms"] = int(self.number_of_rooms)
        condo_dict["number_of_bathrooms"] = int(self.number_of_bathrooms)
        condo_dict["city"] = str(self.city)
        condo_dict["selling_agent"] = str(self.selling_agent)
        condo_dict["yearly_property_tax"] = float(self.yearly_property_tax)
        condo_dict["monthly_strata_fee"] = int(self.monthly_strata_fee)
        # condo_dict["pets_allowed"] = bool(self.pets_allowed)
        condo_dict["pets_allowed"] = int(self.pets_allowed)
        condo_dict["type"] = self.home_type
        detached_home_dict["id"] = int(self.id)
        # if self.get_id() is not None:
            # condo_dict["id"] = self.get_id()

        return condo_dict
