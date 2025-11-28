class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account balance (encapsulation: private attribute)"""
        self.__account_balance = initial_balance  # __ makes it private

    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist"""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance"""
        print(f"Current Balance: ${self.__account_balance:.2f}")