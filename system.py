class System(object):
    def __init__(self, name, position):
        self.name = name
        self.position = position

        self.planets = []

    def add_planet(self, planet, orbit=None)
        orbit = orbit or len(self.planets)

        if orbit < 0:
            raise ValueError('Cannot add a planet to a negative orbit')
        if orbit > 4:
            raise ValueError('Cannot add a planet to an orbit > 4')

        if self.planets[orbit]:
            raise ValueError('A planet already exists at orbital {} in {}'
                             .format(orbit, self))
