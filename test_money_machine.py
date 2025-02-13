import unittest
from unittest.mock import patch
from money_machine import MoneyMachine

class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    @patch("builtins.input", side_effect=["4", "3", "2", "1"])
    def test_process_coins(self, mock_input):
        """Test the coins processing method"""
        atm = MoneyMachine()
        expected = (4 * 0.25) + (3 * 0.1) + (2 * 0.05) + (1 * 0.01)  # 1.41
        self.assertEqual(atm.process_coins(), expected)

    @patch("builtins.input", side_effect=["6", "0", "0", "0"])
    def test_payment_exact(self, mock_input):
        """Test the payment method with exact value"""
        atm = MoneyMachine()
        self.assertTrue(atm.make_payment(1.5))

    @patch("builtins.input", side_effect=["8", "0", "0", "0"])
    def test_payment_exceeding(self, mock_input):
        """Test the payment method with exceeding money"""
        atm = MoneyMachine()
        self.assertTrue(atm.make_payment(1.5))

    @patch("builtins.input", side_effect=["4", "0", "0", "0"])
    def test_payment_less(self, mock_input):
        """Test the payment method with less money"""
        atm = MoneyMachine()
        self.assertFalse(atm.make_payment(1.5))

if __name__ == "__main__":
    unittest.main(verbosity=2)
