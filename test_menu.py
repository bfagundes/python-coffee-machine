import unittest
from menu import Menu, MenuItem

class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_items(self):
        """Test for menu output"""
        menu = Menu()
        output = menu.get_items()
        self.assertEqual(output, "latte/espresso/cappuccino/")

    def test_find_drink(self):
        """Test finding a menu item on the menu"""
        menu = Menu()
        self.assertIsInstance(menu.find_drink("latte"), MenuItem)
        self.assertFalse(menu.find_drink("Invalid_Drink"))

if __name__ == "__main__":
    unittest.main(verbosity=2)