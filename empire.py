class Empire(object):
    """An Empire, top-level object for a player"""
    def __init__(self, name):
        self.name = name

        self.colonies = []
        self.fleets = []
