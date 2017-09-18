class Ship(object):
    def __init__(self, name, max_hull, max_shield, speed, range, damage):
        self.name = name
        self.max_hull = max_hull
        self.hull = max_hull
        self.max_shield = max_shield
        self.shield = max_shield
        self.speed = speed
        self.range = range
        self.damage = damage

        self._position = (0, 0)
        self._destination = None
        self._target = None
        self._active = True

    def _move_to(self, x, y):
        self._position = (x, y)

    def set_course(self, x, y):
        self._destination = (x, y)

    def process_turn(self):
        pass
        # calculate direction vector
        # multiply by speed
        # add to position

        # check range to target
        # if < range, call damage on target

    def _damage_shield(self, damage):
        """Applies damage to the ships' shield, returning any damage left"""
        self.shield -= damage

        if self.shield < 0:
            overkill = self.shield * -1
            self.shield = 0
            return overkill

        return 0

    def _damage_hull(self, damage):
        self.hull -= damage

        if self.hull <= 0:
            self.hull = 0
            self._die()

    def _die(self):
        self._active = False

    def take_damage(self, damage):
        hull_damage = self._damage_shield(damage)

        if hull_damage:
            self._damage_hull(hull_damage)

    def status_report(self):
        return ("{name}: shield:{shield}/{max_shield}, hull:{hull}/{max_hull}"
                .format(name=self.name,
                        shield=self.shield,
                        max_shield=self.max_shield,
                        hull=self.hull,
                        max_hull=self.max_hull))
