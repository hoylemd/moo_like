from unittest import TestCase
from vector import Vector, TAU


class TestVector(TestCase):
    def test_construct__2d(self):
        sut = Vector(3, 4)
        self.assertIsNotNone(sut)
        self.assertItemsEqual(sut, [3, 4])

    def test_norm(self):
        sut = Vector(3, 4)
        self.assertEqual(sut.norm(), 5)

    def test_argument_45(self):
        sut = Vector(1, 1)
        self.assertAlmostEqual(sut.argument(), TAU / 8)

    def test_argument_45__degrees(self):
        sut = Vector(1, 1)
        angle = sut.argument(unit=Vector.UNIT_DEGREES)
        self.assertAlmostEqual(angle, 45)

    def test_argument_neg_90(self):
        sut = Vector(-1, 0)
        self.assertAlmostEqual(sut.argument(), 3 * TAU / 4)
