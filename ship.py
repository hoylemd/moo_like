from vector import Vector


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

        self._position = Vector(0, 0)
        self._destination = None
        self._target = None
        self._active = True

    def _move_to(self, x, y=None):
        """Move the ship to a new position

        Parameters
        ----------
        x : Vector, int, or float
            New `Vector` representing the position, or first component thereof
        y : int or float
            optional, default `None`. Second component of new vector
        """
        if y is None and isinstance(x, Vector):
            self._position = x
        else:
            self._position = Vector(x, y)

    def set_course(self, x, y=None):
        """Set a new destination for the ship

        Parameters
        ----------
        x : Vector, int, or float
            New `Vector` representing new destination, or first component
        y : int or float
            optional, default `None`. Second component of new vector
        """
        if y is None and (x.x and x.y):
            self._destination = x
        else:
            self._destination = Vector(x, y)

    def _damage_shield(self, damage):
        """Applies damage to the ships' shield, returning any damage left

        Parameters
        ----------
        damage : int

        Returns
        -------
        int
            amount of damage left after shield damage
        """
        self.shield -= damage

        if self.shield < 0:
            overkill = self.shield * -1
            self.shield = 0
            return overkill

        return 0

    def _damage_hull(self, damage):
        """Applies damage directly to the ship's hull, maybe killing the ship

        Parameters
        ----------
        damage : int
        """
        self.hull -= damage

        if self.hull <= 0:
            self.hull = 0
            self._die()

    def _die(self):
        """Hook for when ship is destroyed"""
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

    def set_target(self, target):
        self.target = target

    def _process_move(self):
        pass
        # calculate direction vector
        # multiply by speed
        # add to position

    def _process_attack(self):
        pass
        # check range to target
        # if < range, call damage on target

    def process_turn(self):
        self._process_move()
        self._process_attack()

    @property
    def position(self):
        return self._position
