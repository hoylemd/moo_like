from unittest import TestCase

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
        unit = sut.normalize()
        self.assertAlmostEqual(sut.argument(), unit.argument())
        self.assertItemsEqual((round(comp, 7) for comp in unit),
                              (0.9615239, -0.2747211,))
