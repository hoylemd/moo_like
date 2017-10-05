from unittest import TestCase
from mock import patch

from vector import Vector, TAU


class TestVector(TestCase):
    def assertItemsAlmostEqual(self, a, b, message=None):
        """Asserts that every member of a and b are == to 7 decimal places"""
        self.assertItemsEqual(
            (round(element, 7) for element in a),
            (round(element, 7) for element in b),
            None,
        )

    def test_construct__2d(self):
        """Should invoke a vector with the provided components"""
        sut = Vector(3, 4)
        self.assertIsNotNone(sut)
        self.assertItemsEqual(sut, (3, 4,))

    def test_argument_45(self):
        """Should return the correct angle in Radians"""
        sut = Vector(1, 1)
        self.assertAlmostEqual(sut.argument(), TAU / 8)

    def test_argument_45__degrees(self):
        """Should return the correct angle in Degrees"""
        sut = Vector(1, 1)
        angle = sut.argument(unit=Vector.UNIT_DEGREES)
        self.assertAlmostEqual(angle, 45)

    def test_argument__neg_90(self):
        """Should return the correct, reversed angle in Radians"""
        sut = Vector(-1, 0)
        self.assertAlmostEqual(sut.argument(), 3 * TAU / 4)

    def test_norm(self):
        """Should return the correct norm/magnitude"""
        sut = Vector(3, 4)
        self.assertEqual(sut.norm(), 5)

    def test_normalize(self):
        """Should return the correct unit vector"""
        sut = Vector(7, -2)
        unit_vector = sut.normalize()
        self.assertAlmostEqual(sut.argument(), unit_vector.argument())
        self.assertItemsAlmostEqual(unit_vector, (0.9615239, -0.2747211,))

    def test_rotate_by_angle__quarter_tau(self):
        """Should rotate the vector a quarter turn"""
        sut = Vector(3, 2)
        rotated_vector = sut.rotate_by_angle(TAU/4.)
        self.assertItemsAlmostEqual(rotated_vector, (-2, 3))

    def test_rotate_by_angle__180_degrees(self):
        """Should rotate the vector all the way around"""
        sut = Vector(3, -4.5)
        rotated_vector = sut.rotate_by_angle(180, unit=Vector.UNIT_DEGREES)
        self.assertItemsAlmostEqual(rotated_vector, (-3, 4.5))

    def test_dot_product(self):
        """Should compute sum of inter-vector components"""
        sut = Vector(1, 2)
        operand = Vector(3, -1)
        expected = (1 * 3) + (2 * -1)

        product = sut._dot_product(operand)
        self.assertEqual(product, expected)

    def test_mult__number(self):
        """Should multiply each component by the operand"""
        sut = Vector(2, -4)
        product = sut * 3
        self.assertItemsEqual(product, (6, -12))

    def test_mult__vector(self):
        """Should compute the dot product of the two vectors"""
        sut = Vector(4, 5)
        operand = Vector(2, 3)

        with patch('vector.Vector._dot_product') as dot_product_mock:
            sut * operand

        dot_product_mock.assert_called_once()

    def test_mult__string(self):
        """Should raise exception"""
        sut = Vector(7, 5)

        with self.assertRaises(ValueError):
            sut * 'string'

    def test_rmult(self):
        """Should call __mul__"""
        sut = Vector(1, -3)

        with patch('vector.Vector.__mul__') as mul_mock:
            5 * sut

        mul_mock.assert_called_once()
