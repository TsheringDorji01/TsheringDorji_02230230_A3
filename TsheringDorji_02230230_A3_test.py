import unittest
from TsheringDorji_02230230_A3 import BankAccount, InvalidInputException

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.acc = BankAccount('123', 'Test User', 100)

    def test_deposit_valid(self):
        self.acc.deposit(50)
        self.assertEqual(self.acc.balance, 150)

    def test_deposit_invalid(self):
        self.acc.deposit(-10)
        self.assertEqual(self.acc.balance, 100)

    def test_withdraw_valid(self):
        self.acc.withdraw(50)
        self.assertEqual(self.acc.balance, 50)

    def test_withdraw_invalid(self):
        self.acc.withdraw(200)
        self.assertEqual(self.acc.balance, 100)

    def test_top_up_valid(self):
        self.acc.top_up_mobile('17806582', 30)
        self.assertEqual(self.acc.balance, 70)

    def test_top_up_invalid(self):
        with self.assertRaises(InvalidInputException):
            self.acc.top_up_mobile('17806582', 200)

    def test_edge_case_zero_deposit(self):
        self.acc.deposit(0)
        self.assertEqual(self.acc.balance, 100)

    def test_edge_case_zero_withdraw(self):
        self.acc.withdraw(0)
        self.assertEqual(self.acc.balance, 100)

if __name__ == '__main__':
    unittest.main()
