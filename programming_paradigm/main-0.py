
    # main-0.py

import sys
from bank_account import BankAccount

def process_command(account, command_line):
    """Process a single command like 'deposit:50' or 'display'"""
    command, *params = command_line.split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

def main():
    account = BankAccount(100)  # Starting balance

    # If a command is given in sys.argv, use it
    if len(sys.argv) > 1:
        process_command(account, sys.argv[1])
        return

    # Otherwise, enter interactive mode
    print("Welcome to your Bank Account!")
    print("Available commands: deposit:<amount>, withdraw:<amount>, display, exit")

    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        process_command(account, user_input)

if __name__ == "__main__":
    main()
