import unittest
from TsheringDorji_02230230_A3 import SimpleAccount, InputError, TransferException

class TestSimpleAccount(unittest.TestCase):
    """Unit tests for SimpleAccount class operations."""

    def setUp(self):
        self.user1 = SimpleAccount("Tshering", 500)
        self.user2 = SimpleAccount("Dorji", 300)

    def test_deposit_valid_amount(self):
        self.user1.add_funds(200)
        self.assertEqual(self.user1.balance, 700)

    def test_deposit_negative_amount_raises_error(self):
        with self.assertRaises(InputError):
            self.user1.add_funds(-50)

    def test_withdraw_valid_amount(self):
        self.user1.deduct_funds(100)
        self.assertEqual(self.user1.balance, 400)

    def test_withdraw_more_than_balance_raises_error(self):
        with self.assertRaises(InputError):
            self.user1.deduct_funds(600)

    def test_valid_transfer(self):
        self.user1.send_funds(self.user2, 200)
        self.assertEqual(self.user1.balance, 300)
        self.assertEqual(self.user2.balance, 500)

    def test_transfer_to_self_raises_error(self):
        with self.assertRaises(TransferException):
            self.user1.send_funds(self.user1, 100)

    def test_valid_mobile_top_up(self):
        self.user1.recharge_mobile(100)
        self.assertEqual(self.user1.mobile_credit, 100)
        self.assertEqual(self.user1.balance, 400)

    def test_mobile_top_up_exceeding_balance_raises_error(self):
        with self.assertRaises(InputError):
            self.user1.recharge_mobile(600)

    def test_account_deletion_simulation(self):
        accounts = {"Tshering": self.user1, "Dorji": self.user2}
        del accounts["Tshering"]
        self.assertNotIn("Tshering", accounts)

    def test_zero_deposit_raises_error(self):
        with self.assertRaises(InputError):
            self.user1.add_funds(0)

    def test_zero_withdraw_raises_error(self):
        with self.assertRaises(InputError):
            self.user1.deduct_funds(0)

    def test_zero_topup_raises_error(self):
        with self.assertRaises(InputError):
            self.user1.recharge_mobile(0)

    def test_transfer_exceeding_balance_raises_error(self):
        with self.assertRaises(TransferException):
            self.user1.send_funds(self.user2, 10000)

    def test_transfer_negative_amount_raises_error(self):
        with self.assertRaises(TransferException):
            self.user1.send_funds(self.user2, -50)

    def test_create_account_with_negative_balance_allowed(self):
        test_user = SimpleAccount("NegativeUser", -100)
        self.assertEqual(test_user.balance, -100)

    def test_string_representation_includes_details(self):
        info = str(self.user1)
        self.assertIn("Tshering", info)
        self.assertIn("Balance", info)

if __name__ == "__main__":
    unittest.main()