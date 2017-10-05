"""
The MIT License (MIT)

Copyright (c) 2015 Mat Leonard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import math

UNIT_DEGREES = 'decrees'
UNIT_RADIANS = 'radians'
TAU = 2 * math.pi


class Vector(object):
    UNIT_DEGREES = UNIT_DEGREES
    UNIT_RADIANS = UNIT_RADIANS
    """An Iterable, (roughly) Immutable class for representing vectors.

    A vector is simply an array of numbers (usually 2 or 3 for spacial vectors)
    but this includes a bunch of useful vector math operations too.
    """
    def __init__(self, *args):
        """Create a vector

        Examples
        --------
        >>>v = Vector(1, 2)
        Vector(1, 2)
        """
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    def norm(self):
        """Returns the norm (length, magnitude) of the vector

        Returns
        -------
        float
        """
        return math.sqrt(sum(comp**2 for comp in self))

    def argument(self, unit=UNIT_RADIANS):
        """Returns the argument of the vector

        Argument: The angle between the vector and the vector [0, 1], clockwise

        Parameters
        ----------
        unit : Vector.UNIT_DEGREES or Vector.UNIT_RADIANS
            determines the unit in which the argument will be expressed.
            defaults to Vector.UNIT_RADIANS

        Returns
        -------
        float
        """
        argument = math.acos(Vector(0, 1) * self / self.norm())
        if self.values[0] < 0:
            argument = TAU - argument

        if unit == UNIT_DEGREES:
            return math.degrees(argument)

        return argument

    def normalize(self):
        """Returns a normalized unit vector

        Returns
        -------
        Vector
        """
        norm = self.norm()
        normed = tuple(comp / norm for comp in self)
        return Vector(*normed)

    def rotate_by_angle(self, theta, unit=UNIT_RADIANS):
        """Rotate this vector clockwise by the provided angle

        Parameters
        ----------
        theta : int or float
            The angle to rotate the vector about the origin
        unit : Vector.UNIT_DEGREES or Vector.UNIT_RADIANS
            determines the unit in which `theta` will be expressed.
            defaults to Vector.UNIT_RADIANS

        Returns
        -------
        Vector
        """
        assert len(self) == 2, (
            'Rotation axis not defined for greater than 2D vector (this: {})'
            .format(len(self))
        )

        if unit == UNIT_DEGREES:
            theta = math.radians(theta)

        # Just applying the 2D rotation matrix
        dc, ds = math.cos(theta), math.sin(theta)
        x, y = self.values
        x, y = dc * x - ds * y, ds * x + dc * y
        return Vector(x, y)

    def rotate_by_matrix(self, matrix):
        """Rotate this vector by the provided matrix

        Parameters
        ----------
        matrix : sequence
            Must be a square metrix with the same dimensions as this vector

        Returns
        -------
        Vector
        """
        assert all(len(row) == len(matrix) for row in matrix), (
            'Rotation matrix must be square: {}'
            .format(matrix)
        )

        return self.matrix_mult(matrix)

    def matrix_mult(self, matrix):
        """Multiply this vector by a matrix.

        Parameters
        ----------
        matrix : sequence
            Must be a square metrix with the same dimensions as this vector

        Returns
        -------
        Vector
        """
        assert all(len(row) == len(self) for row in matrix), (
            'Matrix must match vector dimensions: {}'
            .format(matrix)
        )

        # Grab a row from the matrix, make it a Vector, take the dot product,
        # and store it as the first component
        product = tuple(Vector(*row) * self for row in matrix)

        return Vector(*product)

    def _dot_product(self, other):
        """Dot product (inner product) of self and other vector

        Parameters
        ----------
        other : Vector

        Returns
        -------
        float
        """
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, other):
        """Multiplication operation

        If multiplied with a `Vector`, returns the dot product.
        If multiplied with a number, returns a new vector containing the
        products of this vector's elements with `other`

        Parameters
        ----------
        other : Vector, int, or float

        Returns
        -------
        float or Vector
        """
        if isinstance(other, Vector):
            return self._dot_product(other)

        operand = float(other)
        products = (a * operand for a in self)
        return Vector(*products)

    def __rmul__(self, other):
        """Multiplication operation when second operand

        Parameters
        ----------
        other : Vector, int, or float

        Returns
        -------
        float or Vector
        """
        return self.__mul__(other)

    def __div__(self, other):
        """Division operation

        Parameters
        ----------
        other : int or float

        Returns
        -------
        Vector
        """
        operand = float(other)
        quotients = tuple(a / operand for a in self)
        return Vector(*quotients)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple(a + b for a, b in zip(self, other))
        return Vector(*added)

    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        subbed = tuple(a - b for a, b in zip(self, other))
        return Vector(*subbed)

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return str(self.values)
