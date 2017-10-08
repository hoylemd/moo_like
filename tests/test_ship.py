from unittest import TestCase

from ship import Ship
from vector import Vector


class TestShip(TestCase):
    def setUp(self):
        self.ship = Ship(
            name='Guinea',
            max_hull=100,
            max_shield=50,
            speed=5,
            range=200,
            damage=25,
        )

    def test_take_damage__shield_absorb(self):
        """Should not damage hull, only shields"""
        self.ship.take_damage(45)
        self.assertEqual(self.ship.hull, self.ship.max_hull)
        self.assertEqual(self.ship.shield, self.ship.max_shield - 45)

    def test_move_to__vector(self):
        """Should Replace the ship's position"""
        new_vector = Vector(2, 3)
        self.ship._move_to(new_vector)

        self.assertIs(self.ship._position, new_vector)

    def test_move_to__components(self):
        """Should Replace the ship's position"""
        self.ship._move_to(7, -2)

        self.assertItemsEqual(self.ship._position, (7, -2,))

    def test_set_course__vector(self):
        """Should replace the ship's destination"""
        new_vector = Vector(2, 3)
        self.ship.set_course(new_vector)

        self.assertIs(self.ship._destination, new_vector)

    def test_set_course__components(self):
        """Should replace the ship's position"""
        self.ship.set_course(7, -2)

        self.assertItemsEqual(self.ship._destination, (7, -2,))

    def test_damage_shield__insufficient(self):
        """Should return 0 when less damage than shield applied"""
        self.assertEqual(self.ship._damage_shield(40), 0)

    def test_damage_shield__more(self):
        """Should return extra damage when more damage than shield applied"""
        self.assertEqual(self.ship._damage_shield(75), 25)
