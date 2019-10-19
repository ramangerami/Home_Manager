from abstract_home import AbstractHome


class Condo(AbstractHome):
    """ Child class of AbstractHome that creates a Condo object """

    MONTHLY_FEE_LABEL = "Monthly Fee"
    PETS_ALLOWED_LABEL = "Pets Allowed"

    CONDO_TYPE = 'condo'

    def __init__(self, square_feet, year_built, rooms, bathrooms, city, seller, tax, monthly_fee, pets):
        """ Constructor for a Condo object """
        super().__init__(square_feet, year_built, rooms, bathrooms, city, seller, tax)

        AbstractHome._validate_int_input(Condo.MONTHLY_FEE_LABEL, monthly_fee)
        self._monthly_strata_fee = monthly_fee

        AbstractHome._validate_bool_input(Condo.PETS_ALLOWED_LABEL, pets)
        self._pets_allowed = pets

    def get_monthly_strata_fee(self):
        """ Returns the monthly strata fee for a Condo """
        return self._monthly_strata_fee

    def get_pets_allowed(self):
        """ Returns Boolean value for if pets are allowed in a Condo """
        return self._pets_allowed

    def get_description(self):
        """ Returns a description of a Condo object with details relevant to buyers and seller """
        description = "This is a " + str(self._square_footage) + " square foot condo " + "built in " + str(self._year_built)\
            + " " + "with " + str(self._number_of_rooms) + " rooms, "\
            + str(self._number_of_bathrooms) + " bathrooms"\
            + " and a monthly strata fee of " + str(self._monthly_strata_fee) + ". This home is being sold by "\
            + self._selling_agent
        return description

    def get_type(self):
        """ Returns the type of a Condo object """
        return self.CONDO_TYPE
