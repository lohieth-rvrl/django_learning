import os
import random
import string
from datetime import datetime

# --- 🎯 Decorator Implementation ---

def log_transaction(func):
    """
    Decorator to log banking transactions.
    Logs the transaction type, account number, amount, and timestamp.
    """
    def wrapper(self, amount, *args, **kwargs):
        # The wrapped function (deposit/withdraw) is called first.
        # It's assumed the function is a method of the Account class and
        # returns True on successful transaction.
        success = func(self, amount, *args, **kwargs)

        if success:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Extract transaction type from the function name
            transaction_type = func.__name__.capitalize()

            log_message = (
                f"[{timestamp}]: Transaction Type: {transaction_type}, "
                f"Account Number: {self.account_number}, Amount: ${amount:,.2f}."
            )

            # Log to CLI
            print(f"\n✅ **Transaction Successful!**")
            print(f"**Transaction Log:** {log_message}")

            # Optionally, log to a file (uncomment if file logging is desired)
            # with open("bank_transactions.log", "a") as f:
            #     f.write(log_message + "\n")

        return success
    return wrapper

# --- 🏦 Account Classes Implementation ---

class Account:
    """Base class for all bank accounts."""

    def __init__(self, password, initial_deposit=0.0):
        # Generate a unique 8-digit account number
        self.account_number = ''.join(random.choices(string.digits, k=8))
        self.__balance = max(0.0, initial_deposit) # Private attribute for balance
        self.__password = password # Private attribute for password
        print(f"Account created successfully! Your Account Number is: **{self.account_number}**")

    def verify_password(self, password):
        """Checks if the provided password matches the account password."""
        return self.__password == password

    def get_account_number(self):
        """Returns the account number."""
        return self.account_number

    def get_balance(self):
        """Retrieves the current account balance."""
        return self.__balance

    @log_transaction
    def deposit(self, amount):
        """Deposits funds into the account."""
        try:
            amount = float(amount)
            if amount <= 0:
                print("❌ Deposit amount must be positive.")
                return False
            self.__balance += amount
            print(f"Deposit of ${amount:,.2f} successful.")
            return True
        except ValueError:
            print("❌ Invalid amount format.")
            return False

    @log_transaction
    def withdraw(self, amount):
        """Withdraws funds from the account."""
        try:
            amount = float(amount)
            if amount <= 0:
                print("❌ Withdrawal amount must be positive.")
                return False
            if amount > self.__balance:
                print("❌ Insufficient funds.")
                return False

            self._apply_withdrawal_logic(amount)
            return True

        except ValueError:
            print("❌ Invalid amount format.")
            return False

    def _apply_withdrawal_logic(self, amount):
        """Helper for withdrawal logic, can be overridden by subclasses."""
        self.__balance -= amount
        print(f"Withdrawal of ${amount:,.2f} successful.")


class SavingsAccount(Account):
    """Subclass for Savings Accounts, including interest functionality."""
    INTEREST_RATE = 0.03 # 3% annual interest rate

    def __init__(self, password, initial_deposit=0.0):
        super().__init__(password, initial_deposit)
        print(f"Savings Account setup. Current interest rate: {self.INTEREST_RATE * 100}%.")

    def apply_interest(self):
        """Calculates and deposits annual interest."""
        interest = self.get_balance() * self.INTEREST_RATE
        # Deposit the interest without logging it as a user-initiated transaction
        self.deposit_interest(interest)
        print(f"\n⭐ Interest of ${interest:,.2f} applied to account {self.get_account_number()}.")

    # Helper function for interest deposit to avoid the standard log_transaction
    # being triggered for automated interest application.
    def deposit_interest(self, interest):
        """Deposits interest without standard transaction logging."""
        self._Account__balance += interest


class CheckingAccount(Account):
    """Subclass for Checking Accounts, with a transaction limit."""
    TRANSACTION_LIMIT = 500.00 # Maximum withdrawal/deposit per transaction

    def __init__(self, password, initial_deposit=0.0):
        super().__init__(password, initial_deposit)
        print(f"Checking Account setup. Per-transaction limit: ${self.TRANSACTION_LIMIT:,.2f}.")

    @log_transaction
    def deposit(self, amount):
        """Deposits funds, enforcing the transaction limit."""
        try:
            amount = float(amount)
            if amount > self.TRANSACTION_LIMIT:
                print(f"❌ Deposit exceeds the Checking Account limit of ${self.TRANSACTION_LIMIT:,.2f}.")
                return False
            return super().deposit.__wrapped__(self, amount) # Call the base method logic, avoiding re-logging
        except ValueError:
            print("❌ Invalid amount format.")
            return False

    @log_transaction
    def withdraw(self, amount):
        """Withdraws funds, enforcing the transaction limit."""
        try:
            amount = float(amount)
            if amount > self.TRANSACTION_LIMIT:
                print(f"❌ Withdrawal exceeds the Checking Account limit of ${self.TRANSACTION_LIMIT:,.2f}.")
                return False
            return super().withdraw.__wrapped__(self, amount) # Call the base method logic, avoiding re-logging
        except ValueError:
            print("❌ Invalid amount format.")
            return False


class Bank:
    """Manages all bank accounts."""

    def __init__(self):
        self.accounts = {} # Dictionary to store accounts: {account_number: Account_object}

    def add_account(self, account):
        """Adds a new account to the bank's records."""
        self.accounts[account.get_account_number()] = account

    def get_account(self, account_number, password=None):
        """
        Retrieves an account by number and optionally verifies the password.
        Returns the Account object or None if invalid.
        """
        account = self.accounts.get(account_number)

        if not account:
            print("❌ Error: Account number not found.")
            return None

        if password is not None and not account.verify_password(password):
            print("❌ Error: Incorrect password.")
            return None

        return account

    def get_total_balance(self):
        """Calculates the sum of all balances in the bank."""
        total = sum(account.get_balance() for account in self.accounts.values())
        return total

# --- 💻 CLI and Testing Implementation ---

def create_account_cli(bank):
    """Handles the account creation process via CLI."""
    while True:
        password = input("Enter a password for the new account: ")
        confirm_password = input("Confirm the password: ")

        if password != confirm_password:
            print("❌ Passwords do not match. Please try again.")
            continue

        if len(password) < 4:
            print("❌ Password must be at least 4 characters long.")
            continue

        break

    while True:
        print("\nSelect Account Type:")
        print("1. Savings Account (with interest)")
        print("2. Checking Account (with transaction limit)")
        acc_type_choice = input("Enter choice (1 or 2): ")

        if acc_type_choice == '1':
            initial_deposit = input("Enter initial deposit amount (Savings, default 0): ")
            try:
                initial_deposit = float(initial_deposit) if initial_deposit else 0.0
                new_account = SavingsAccount(password, initial_deposit)
                break
            except ValueError:
                print("❌ Invalid deposit amount. Please enter a number.")
        elif acc_type_choice == '2':
            initial_deposit = input("Enter initial deposit amount (Checking, default 0): ")
            try:
                initial_deposit = float(initial_deposit) if initial_deposit else 0.0
                new_account = CheckingAccount(password, initial_deposit)
                break
            except ValueError:
                print("❌ Invalid deposit amount. Please enter a number.")
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

    bank.add_account(new_account)


def transaction_cli(bank, transaction_type):
    """Handles deposit or withdrawal transactions via CLI."""
    print(f"\n--- {transaction_type.capitalize()} ---")
    acc_num = input("Enter Account Number: ")
    password = input("Enter Password: ")
    amount_str = input(f"Enter {transaction_type} amount: ")

    try:
        amount = float(amount_str)
    except ValueError:
        print("❌ Invalid amount format.")
        return

    account = bank.get_account(acc_num, password)

    if account:
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)

def view_balance_cli(bank):
    """Handles viewing account balance via CLI."""
    print("\n--- View Balance ---")
    acc_num = input("Enter Account Number: ")
    password = input("Enter Password: ")

    account = bank.get_account(acc_num, password)

    if account:
        balance = account.get_balance()
        print(f"\n🏦 Current Balance for Account {acc_num}: **${balance:,.2f}**")

        # Example of subclass-specific action (optional, for demonstration)
        if isinstance(account, SavingsAccount):
            print("💡 This is a Savings Account. You can apply interest.")

# --- Main Program Loop ---

bank = Bank()

print(" Welcome to the Python OOP Bank! ")

while True:
    print("\n--- Main Menu ---")
    print("1. Create Account")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. View Balance")
    print("5. Apply Interest (Savings Accounts Only)")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    try:
        choice = int(choice)
    except ValueError:
        print("❌ Invalid input. Please enter a number from 1 to 6.")
        continue

    if choice == 1:
        create_account_cli(bank)

    elif choice == 2:
        transaction_cli(bank, 'deposit')

    elif choice == 3:
        transaction_cli(bank, 'withdraw')

    elif choice == 4:
        view_balance_cli(bank)

    elif choice == 5:
        print("\n--- Apply Interest ---")
        acc_num = input("Enter Account Number: ")
        password = input("Enter Password: ")

        account = bank.get_account(acc_num, password)

        if account:
            if isinstance(account, SavingsAccount):
                account.apply_interest()
            else:
                print("❌ Interest can only be applied to Savings Accounts.")

    elif choice == 6:
        print(f"\n👋 Thank you for banking with us! Total funds managed: **${bank.get_total_balance():,.2f}**")
        break

    else:
        print("❌ Invalid choice. Please select a valid option (1-6).")

    print("--------------------")