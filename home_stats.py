class HomeStats:
    """ Statistics on a listings of homes """

    def __init__(self, total_homes, detached_homes, condos, years):
        """ Initialize the stats data values """

        if total_homes is None or type(total_homes) != int or not total_homes >= 0:
            raise ValueError("Invalid total homes value")
        self._total_num_homes = total_homes

        if detached_homes is None or type(detached_homes) != int or not detached_homes >= 0:
            raise ValueError("Invalid number of detached homes value")
        self._num_detached_homes = detached_homes

        if condos is None or type(condos) != int or not condos >= 0:
            raise ValueError("Invalid number of condos value")
        self._num_condos = condos

        if years is None or type(years) != int:
            raise ValueError("Invalid years old value")
        self._avg_years_old = years

    def get_total_num_homes(self):
        """ Returns the total number of homes in the listing """
        return self._total_num_homes

    def get_num_detached_homes(self):
        """ Returns the number of detached homes in the listing """
        return self._num_detached_homes

    def get_num_condos(self):
        """ Returns the number of condos in the listing """
        return self._num_condos

    def get_avg_years_old(self):
        """ Returns the average age of all the homes in the listing """
        return self._avg_years_old
    
    def to_dict(self):
        """ Get a Python Dictionary representation of the Home Stats """
        stats_dict = dict()
        stats_dict["total_homes"] = self._total_homes
        stats_dict["detached_homes"] = self._detached_homes
        stats_dict["condos"] = self._condos
        stats_dict["years"] = self._years

        return stats_dict