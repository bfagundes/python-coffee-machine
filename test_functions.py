import unittest
from unittest.mock import patch
from functions import enough_ingredients, consume_ingredients, receive_coins
from data import resources

class TestFunctions(unittest.TestCase):
    def setUp(self):
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100

    def test_enough_ingredients_default(self):
        """Test for enough ingredients with starting resources"""
        self.assertTrue(enough_ingredients("latte"))
        self.assertTrue(enough_ingredients("espresso"))
        self.assertTrue(enough_ingredients("cappuccino"))

    def test_consume_ingredients_latte(self):
        """Test the consumption of ingredients for latte"""
        consume_ingredients("latte")
        self.assertEqual(resources["water"],100)
        self.assertEqual(resources["milk"],50)
        self.assertEqual(resources["coffee"],76)

    def test_consume_ingredients_espresso(self):
        """Test the consumption of ingredients for espresso"""
        consume_ingredients("espresso")
        self.assertEqual(resources["water"],250)
        self.assertEqual(resources["milk"],200)
        self.assertEqual(resources["coffee"],82)

    def test_consume_ingredients_cappuccino(self):
        """Test the consumption of ingredients for cappuccino"""
        consume_ingredients("cappuccino")
        self.assertEqual(resources["water"],50)
        self.assertEqual(resources["milk"],100)
        self.assertEqual(resources["coffee"],76)

    @patch("builtins.input", side_effect=["4", "3", "2", "1"])
    def test_receive_coins(self, mock_input):
        """Test the coins calc"""
        result = receive_coins()
        expected = (4 * 0.25) + (3 * 0.1) + (2 * 0.05) + (1 * 0.01)  # 1.41
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)