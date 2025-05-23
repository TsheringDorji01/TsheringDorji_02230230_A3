class InvalidInputException(Exception):
    """Exception raised for invalid user input."""
    pass

class InvalidTransferException(Exception):
    """Exception raised for invalid transfer requests."""
    pass

class BankAccount:   # A class representing a bank account.
    def __init__(self, account_number, name, balance=0):   # Constructor to initialize the account.
        self.account_number = account_number
        self.name = name
        self.balance = balance   # Initial balance is set to 0 by default.

    def deposit(self, amount):   # Method to deposit money into the account.
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):   # Method to withdraw money from the account.
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def display(self):   # Method to display account details.
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")

    def top_up_mobile(self, phone_number, amount):   # Method to top up a mobile phone number.
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Topped up {amount} to mobile number {phone_number}.")
        else:
            raise InvalidInputException("Invalid top-up amount or insufficient balance.")


def processUserInput(choice, accounts):   # Function to process user input and perform actions based on the choice.
    try:   # Check if the choice is valid.
        if choice == '1':
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            if acc_num in accounts:
                print("Account already exists.")
            else:
                accounts[acc_num] = BankAccount(acc_num, name)
                print("Account created successfully.")
        elif choice == '2':
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[acc_num].deposit(amount)
            else:
                print("Account not found.")
        elif choice == '3':
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[acc_num].withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '4':
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                accounts[acc_num].display()
            else:
                print("Account not found.")
        elif choice == '5':
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                phone = input("Enter mobile phone number: ")
                amount = float(input("Enter top-up amount: "))
                try:
                    accounts[acc_num].top_up_mobile(phone, amount)
                except InvalidInputException as e:
                    print(e)
            else:
                print("Account not found.")
        elif choice == '6':
            print("Thank you for using the banking system.")
            return False
        else:
            raise InvalidInputException("Invalid menu choice.")
    except (ValueError, InvalidInputException, InvalidTransferException) as e:
        print(f"Error: {e}")
    return True

def main():
    """Main function to run the banking system."""
    accounts = {}
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Mobile Phone Top-Up")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if not processUserInput(choice, accounts):
            break

if __name__ == "__main__":
    main()