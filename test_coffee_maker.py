import unittest
from unittest.mock import patch
from coffee_maker import CoffeeMaker
from menu import MenuItem

class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_power_off(self):
        """Test the power off function"""
        machine = CoffeeMaker()
        machine.power_off()
        self.assertFalse(machine.is_powered_on())

    def test_resource_counter(self):
        """Test the resource counter when there's enough resources"""
        machine = CoffeeMaker()
        drink = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
        self.assertTrue(machine.is_resource_sufficient(drink))

    def test_resource_counter_water(self):
        """Test the resource counter when there's not enough water"""
        machine = CoffeeMaker()
        drink = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
        machine.resources["water"] = 0
        self.assertFalse(machine.is_resource_sufficient(drink))

    def test_resource_counter_coffee(self):
        """Test the resource counter when there's not enough coffee"""
        machine = CoffeeMaker()
        drink = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
        machine.resources["coffee"] = 0
        self.assertFalse(machine.is_resource_sufficient(drink))

    def test_resource_counter_milk(self):
        """Test the resource counter when there's not enough milk"""
        machine = CoffeeMaker()
        drink = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
        machine.resources["milk"] = 0
        self.assertFalse(machine.is_resource_sufficient(drink))

if __name__ == "__main__":
    unittest.main(verbosity=2)