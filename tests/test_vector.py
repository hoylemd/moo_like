from unittest import TestCase
from vector import Vector


class TestVector(TestCase):
    def test_construct__2d(self):
        sut = Vector(3, 4)
        self.assertIsNotNone(sut)
        self.assertItemsEqual(sut, [3, 4])

    def test_norm(self):
        sut = Vector(3, 4)
        self.assertEqual(sut.norm(), 5)
