import tkinter as tk
from tkinter import messagebox
import random

# Custom exception for invalid input
class InputError(Exception):
    """Exception raised for errors in user input."""
    pass

# Custom exception for failed transfers
class TransferException(Exception):
    """Exception raised when a transfer operation is not allowed."""
    pass

# Core account functionality
class SimpleAccount:
    """Handles basic banking operations for an account holder."""
    def __init__(self, holder, balance=0, acc_number=None):
        self.holder = holder
        self.balance = balance
        self.mobile_credit = 0
        self.acc_number = acc_number if acc_number else self._generate_acc_number()

    @staticmethod
    def _generate_acc_number():
        """Generates an 8-digit account number."""
        return str(random.randint(10000000, 99999999))

    def add_funds(self, amount):
        """Adds funds to the account."""
        if amount <= 0:
            raise InputError("Amount must be greater than zero.")
        self.balance += amount

    def deduct_funds(self, amount):
        """Deducts funds from the account."""
        if amount <= 0 or amount > self.balance:
            raise InputError("Invalid amount requested.")
        self.balance -= amount

    def send_funds(self, recipient, amount):
        """Transfers funds to another account."""
        if self == recipient or amount <= 0 or amount > self.balance:
            raise TransferException("Transfer conditions not met.")
        self.deduct_funds(amount)
        recipient.add_funds(amount)

    def recharge_mobile(self, amount):
        """Transfers funds from account to mobile balance."""
        if amount <= 0 or amount > self.balance:
            raise InputError("Invalid recharge amount.")
        self.balance -= amount
        self.mobile_credit += amount

    def __str__(self):
        return f"Account Holder: {self.holder}, Balance: Nu.{self.balance}, Mobile Credit: Nu.{self.mobile_credit}"

# Account registry
user_accounts = {
    "Tshering": SimpleAccount("Tshering", 1000),
    "Dorji": SimpleAccount("Dorji", 500)
}

def register_account(name, initial_amount=0):
    if name in user_accounts:
        raise InputError("Username already exists.")
    new_user = SimpleAccount(name, initial_amount)
    user_accounts[name] = new_user
    print(f"Created account for {name} | Account Number: {new_user.acc_number}")
    return new_user

def handle_user_choice(option, user):
    try:
        if option == "1":
            print(user)
        elif option == "2":
            amount = float(input("Enter deposit amount (Nu): "))
            user.add_funds(amount)
        elif option == "3":
            amount = float(input("Enter withdrawal amount (Nu): "))
            user.deduct_funds(amount)
        elif option == "4":
            recipient_name = input("Enter recipient's name: ")
            if recipient_name not in user_accounts:
                raise TransferException("Recipient not found.")
            amount = float(input("Enter transfer amount (Nu): "))
            user.send_funds(user_accounts[recipient_name], amount)
        elif option == "5":
            amount = float(input("Enter top-up amount (Nu): "))
            user.recharge_mobile(amount)
        elif option == "6":
            confirm = input("Delete your account? Type 'yes' to confirm: ")
            if confirm.lower() == "yes":
                del user_accounts[user.holder]
                print("Account has been deleted.")
                return None
        elif option == "7":
            print("Thank you for banking with us. Goodbye!")
            return None
        else:
            raise InputError("Menu option not recognized.")
    except (ValueError, InputError, TransferException) as err:
        print("Error:", err)
    return user

def run_bank_terminal():
    print("\n Welcome to SmartBank")
    username = input("Enter your username: ")
    if username not in user_accounts:
        print("No existing account found. Registering new user...")
        register_account(username)
    user = user_accounts[username]
    print(f"Hello, {user.holder}! Your account number is {user.acc_number}.")
    while user:
        print("\nMenu")
        print("1. View Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Transfer Money")
        print("5. Mobile Recharge")
        print("6. Close Account")
        print("7. Exit")
        choice = input("Please select an option: ")
        user = handle_user_choice(choice, user)

# GUI Class
class SmartBankGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartBank - GUI")
        self.user = None
        self.init_login()

    def init_login(self):
        tk.Label(self.root, text="Username:").pack()
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()
        tk.Button(self.root, text="Login", command=self.authenticate).pack()

    def authenticate(self):
        username = self.entry_name.get()
        if username not in user_accounts:
            user_accounts[username] = SimpleAccount(username)
        self.user = user_accounts[username]
        self.display_menu()

    def display_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"Welcome, {self.user.holder}!").pack()
        tk.Button(self.root, text="View Balance", command=self.display_balance).pack()
        tk.Button(self.root, text="Deposit", command=self.prompt_deposit).pack()
        tk.Button(self.root, text="Withdraw", command=self.prompt_withdraw).pack()
        tk.Button(self.root, text="Recharge", command=self.prompt_recharge).pack()

    def display_balance(self):
        messagebox.showinfo("Account Balance", str(self.user))

    def prompt_deposit(self):
        amt = float(input("Enter amount to deposit: Nu."))
        self.user.add_funds(amt)
        self.display_balance()

    def prompt_withdraw(self):
        amt = float(input("Enter amount to withdraw: Nu."))
        self.user.deduct_funds(amt)
        self.display_balance()

    def prompt_recharge(self):
        amt = float(input("Enter mobile recharge amount: Nu."))
        self.user.recharge_mobile(amt)
        self.display_balance()

if __name__ == "__main__":
    run_bank_terminal()