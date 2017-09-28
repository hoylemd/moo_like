from collections import namedtuple
from math import sqrt

Vector = namedtuple('Vector', ['x', 'y'])


class Vector(object):
    def __init__(self, x, y):
        self._vector = (x, y)

    @property
    def x(self):
        return self._vector[0]

    @property
    def y(self):
        return self._vector[1]

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

    def __str__(self):
        return repr(self)


def get_direction_vector(a, b):
    """calculates a unit vector represetning the direction from a to b

    Parameters
    ----------
    a: 2-tuple of floats (position coordinates)
    b: 2-tuple of floats (position coordinates)

    Returns
    -------
    2-tuple of floats
    """

    direction = Vector(b.x - a.x, b.y - a.y)
    magnitude = sqrt(direction.x ** 2, direction.y ** 2)
    return Vector(direction.x / magnitude, direction.y / magnitude)
