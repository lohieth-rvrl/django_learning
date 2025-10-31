import os
import random
import string
from datetime import datetime

def log_transaction(transaction_type):
    def decorator(func):
        def wrapper(self, amount, *args, **kwargs):
            result = func(self, amount, *args, **kwargs)
            if result:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ac_number = self.get_ac_number()
                log_entry = (
                    f"[{timestamp}] -> type: {transaction_type.capitalize()}, \naccount Number: {ac_number}, amount: ${amount:,.2f}."
                )
                print("\nTransaction Successful!")
                print(f"Log -> {log_entry}")
                with open("transaction_log.txt", "a") as log_file:
                    log_file.write(log_entry + "\n")
            return result
        return wrapper
    return decorator


class Account:
    def __init__(self, initial_deposit=0.0, password=""):
        self.ac_number = ''.join(random.choices(string.digits, k=6))
        self.balance = 0.0
        self.password = password
        if initial_deposit > 0:
            self.deposit(initial_deposit)

    def get_ac_number(self):
        return self.ac_number

    def get_balance(self):
        return self.balance

    def verify_password(self, password):
        return self.password == password

    @log_transaction("deposit")
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError as e:
            print(f"{e} - invalid input")
            return False

        if amount > 0:
            self.balance += amount
            return True
        print("no negative or zero deposit allowed")
        return False

    @log_transaction("withdraw")
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError as e:
            print(f"{e} - invalid input")
            return False

        if amount <= 0:
            print("no negative or zero withdraw allowed")
            return False

        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("invalid")
            print(f"balance -> ${self.balance:,.2f}.")
            return False


class SavingsAccount(Account):
    def __init__(self, initial_deposit=0.0, password="", interest_rate=0.02):
        super().__init__(initial_deposit, password)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        if interest > 0:
            self.balance += interest
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = (
                f"[{timestamp}] --> type: interest applied, \naccount Number: {self.ac_number}, amount: ${interest:,.2f}."
            )
            print(f"\nInterest Applied: {log_entry}")
            with open("transaction_log.txt", "a") as log_file:
                log_file.write(log_entry + "\n")
            return interest
        return 0.0


class CheckingAccount(Account):
    def __init__(self, initial_deposit=0.0, password="", transaction_limit=1000.0):
        super().__init__(initial_deposit, password)
        self.transaction_limit = transaction_limit

    @log_transaction("withdraw")
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            return super().withdraw(amount)

        if amount > self.transaction_limit:
            print(f"limit exceeded -> ${self.transaction_limit:,.2f}.")
            return False
        return super().withdraw(amount)

    @log_transaction("deposit")
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            return super().deposit(amount)

        if amount > self.transaction_limit:
            print(f"Deposit limit exceeded. Max limit is ${self.transaction_limit:,.2f}.")
            return False
        return super().deposit(amount)


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.get_ac_number()] = account

    def get_account(self, ac_number, password, suppress_output=False):
        account = self.accounts.get(ac_number)
        if account and account.verify_password(password):
            return account
        if not suppress_output:
            print("account not found or incorrect password.")
        return None

    def total_balance(self):
        total = 0.0
        for account in self.accounts.values():
            total += account.get_balance()
        return total


bank = Bank()

while True:
    print("\n-------- Welcome to MyBank --------")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View balance")
    print("5. Apply Interest (Savings Only)")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("invalid input")
        continue

    if choice == 1:
        print("\n-------- Create Account --------")
        while True:
            password = input("enter the password: ")
            confirm_password = input("re-enter the password: ")
            if password == confirm_password and len(password) >= 4:
                break
            elif len(password) < 4:
                print("password must be at least 4 characters long.")
            else:
                print("passwords do not match")

        while True:
            print("\nAccount Types: ")
            print("1. Savings account (with interest)")
            print("2. Checking account (with transaction limit)")
            ac_type = input("Choose (1/2): ")

            try:
                amount_str = input("enter the initial deposit amount (default 0.0): ")
                amount = float(amount_str) if amount_str else 0.0
                if amount < 0:
                    print("no negative values")
                    continue
            except ValueError:
                print("invalid input (default 0.0)")
                amount = 0.0

            if ac_type == '1':
                try:
                    rate_str = input("enter the interest rate in percentage (default 2%): ")
                    rate = float(rate_str) / 100 if rate_str else 0.02
                    if rate < 0:
                        print("no negative values")
                        continue
                    account = SavingsAccount(amount, password, rate)
                except ValueError:
                    print("invalid input (default 2%)")
                    account = SavingsAccount(amount, password)
            elif ac_type == '2':
                try:
                    limit_str = input("Enter the transaction limit (default $1000.00): ")
                    limit = float(limit_str) if limit_str else 1000.0
                    account = CheckingAccount(amount, password, limit)
                except ValueError:
                    print("invalid input (default $1000.00)")
                    account = CheckingAccount(amount, password)
            else:
                print("invalid choice")
                continue

            bank.add_account(account)
            print(f"\nAccount created successfully! \nAccount Number -> {account.get_ac_number()}")
            break

    elif choice == 2:
        print("\n-------- Deposit --------")
        ac_number = input("enter the account number: ")
        password = input("enter the password: ")
        account = bank.get_account(ac_number, password, suppress_output=True)
        if account:
            try:
                amount = float(input("enter the amount: "))
                if account.deposit(amount):
                    print(f"deposit completed \nbalance -> ${account.get_balance():,.2f}")
            except ValueError:
                print("invalid input")
        else:
            print("account not found or incorrect password.")

    elif choice == 3:
        print("\n-------- Withdraw --------")
        ac_number = input("enter the account number: ")
        password = input("enter the password: ")
        account = bank.get_account(ac_number, password, suppress_output=True)

        if account:
            try:
                amount = float(input("enter the withdrawal amount: "))
                if account.withdraw(amount):
                    print(f"withdrawal completed \nbalance -> ${account.get_balance():,.2f}")
            except ValueError:
                print("invalid input")
        else:
            print("account not found or incorrect password.")

    elif choice == 4:
        print("\n-------- View Balance --------")
        ac_number = input("enter the account number: ")
        password = input("enter the password: ")
        account = bank.get_account(ac_number, password, suppress_output=True)
        if account:
            print(f"balance -> account {ac_number}: ${account.get_balance():,.2f}")
        else:
            print("account not found or incorrect password.")

    elif choice == 5:
        print("\n-------- Apply Interest --------")
        ac_number = input("enter the account number: ")
        password = input("enter the password: ")
        account = bank.get_account(ac_number, password, suppress_output=True)
        if account:
            if isinstance(account, SavingsAccount):
                interest = account.apply_interest()
                if interest > 0:
                    print(f"interest -> ${interest:,.2f} applied.\nbalance -> ${account.get_balance():,.2f}")
                else:
                    print("no interest applied")
            else:
                print("only for savings account")
        else:
            print("account not found or incorrect password.")

    elif choice == 6:
        print("-------- Exit --------")
        break

    else:
        print("invalid choice")
