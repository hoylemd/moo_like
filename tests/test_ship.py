from unittest import TestCase

from ship import Ship
from vector import Vector


class TestShip(TestCase):
    def test_take_damage__shield_absorb(self):
        """Should not damage hull, only shields"""
        sut = Ship('Guinea', 100, 50, 5, 200, 25)

        sut.take_damage(45)
        self.assertEqual(sut.hull, sut.max_hull)
        self.assertEqual(sut.shield, sut.max_shield - 45)

    def test_move_to__vector(self):
        """Should Replace the ship's position"""
        sut = Ship('Guinea', 100, 50, 5, 200, 25)

        new_vector = Vector(2, 3)
        sut._move_to(new_vector)

        self.assertIs(sut._position, new_vector)

    def test_move_to__components(self):
        """Should Replace the ship's position"""
        sut = Ship('Guinea', 100, 50, 5, 200, 25)

        sut._move_to(7, -2)

        self.assertItemsEqual(sut._position, (7, -2,))

    def test_set_course__vector(self):
        """Should replace the ship's destination"""
        sut = Ship('Guinea', 100, 50, 5, 200, 25)

        new_vector = Vector(2, 3)
        sut.set_course(new_vector)

        self.assertIs(sut._destination, new_vector)

    def test_set_course__components(self):
        """Should Replace the ship's position"""
        sut = Ship('Guinea', 100, 50, 5, 200, 25)

        sut.set_course(7, -2)

        self.assertItemsEqual(sut._destination, (7, -2,))
