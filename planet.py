orbit_labels = [
    'prime',
    'II',
    'III',
    'IV',
    'V'
]


class Planet(object):
    def __init__(self, size, biome, minerals, special=None):
        self.system = None
        self.orbit = None

        self.size = size
        self.biome = biome
        self.minerals = minerals
        self.special = special

        self.colony = None

    def __str__(self):
        if self.colony:
            return self.colony.name
        if self.system and self.orbit:
            return "{system} {number}".format(str(self.system),
                                              number=orbit_labels[self.orbit])
        return 'Rogue Planet'
