class Colony(object):
    """A colony on a planet"""
    def __init__(self, planet, empire):
        self.planet = planet
        self.empire = empire
        self.colonists = []

    @property
    def food_output(self):
        """Total food output of the colony

        Returns
        -------
        int
        """
        return 0

    @property
    def production_output(self):
        """Total food output of the colony

        Returns
        -------
        int
        """
        return 0

    @property
    def science_output(self):
        """Total science output of the colony

        Returns
        -------
        int
        """
        return 0

    def add_colonist(self, job=None):
        """Add a colonist to the colony

        Parameters
        ----------
        job : FARM, BUILD, RESEARCH
          defaults to whichever job has the least colonists
        """
