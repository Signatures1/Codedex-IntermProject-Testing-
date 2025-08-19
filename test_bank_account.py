import unittest
from bank_account import BankAccount

class Test_BankAccount(unittest.TestCase):

    def setUp(self):
      self.account = BankAccount(100)

    def tearDown(self):
        self.account = None
    
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-1)

    def test_withdraw_sufficient_funds(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(101)

    def test_withdraw_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-1)

if __name__ == '__main__':
    unittest.main()