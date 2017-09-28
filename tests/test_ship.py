from unittest import TestCase
from ship import Ship


class TestShip(TestCase):
    def test_take_damage__shield_absorb(self):
        ship = Ship('Guinea', 100, 50, 5, 200, 25)

        ship.take_damage(45)
        self.assertEqual(ship.hull, ship.max_hull)
        self.assertEqual(ship.shield, ship.max_shield - 45)
