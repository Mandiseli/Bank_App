import os
import re
from datetime import datetime
import atexit  # Import the atexit module
import random
import string
import datetime

# Define regex patterns for username and password
username_pattern = r"^[a-zA-Z0-9_]{3,20}$"
password_pattern = r"^[a-zA-Z0-9_]{6}$"


def is_valid_username(username):
    return re.match(username_pattern, username)


def is_valid_password(password):
    return re.match(password_pattern, password)


def load_user_accounts():
    user_accounts = {}
    if os.path.exists('Bank Data.txt'):
        with open('Bank Data.txt', 'r') as file:
            for line in file:
                account_info = line.strip().split(',')
                if len(account_info) == 3:
                    username, password, balance = account_info
                    if is_valid_username(username) and is_valid_password(password):
                        try:
                            user_accounts[username] = {'balance': float(balance), 'password': password}
                        except ValueError:
                            print("=====BANK APP=====")
    return user_accounts


def save_user_accounts(user_accounts):
    with open('Bank Data.txt', 'w') as file:
        for username, account_info in user_accounts.items():
            balance = account_info['balance']
            password = account_info['password']
            file.write(f"{username},{password},{balance}\n")


def create_account(user_accounts, username, initial_balance, password):
    if username in user_accounts:
        print("Account already exists. Transaction canceled.")
    else:
        user_accounts[username] = {'balance': initial_balance, 'password': password}
        save_user_accounts(user_accounts)
        print("==========================================================")
        print(f"New account created with username: {username} and an initial balance of R{initial_balance}")
        print("==========================================================")


def suggest_username(username):
    # Generate 2 random characters
    random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(2))

    # Append the random characters to the original username
    suggested_username = username + random_chars.upper()

    return suggested_username


def deposit(user_accounts, username, amount):
    if username in user_accounts:
        if amount > 0:
            user_accounts[username]['balance'] += amount
            save_user_accounts(user_accounts)
            log_transaction(username, "Deposit", amount, user_accounts[username]['balance'])
            print("=====DEPOSIT=====")
            print(f"Deposited R{amount}. New balance: R{user_accounts[username]['balance']}")
            print("=====DEPOSIT=====")
        else:
            print("Invalid deposit amount. Amount must be positive.")
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            password = input("Enter your password: ")
            create_account(user_accounts, username, initial_balance, password)
        else:
            print("Transaction canceled.")


def withdraw(user_accounts, username, amount):
    if username in user_accounts:
        balance = user_accounts[username]['balance']
        if balance >= amount:
            if amount > 0:
                user_accounts[username]['balance'] -= amount
                save_user_accounts(user_accounts)
                log_transaction(username, "Withdrawal", amount, user_accounts[username]['balance'])
                print("======WITHDRAWAL======")
                print(f"Withdrew R{amount}. New balance: R{user_accounts[username]['balance']}")
            else:
                print("Invalid withdrawal amount. Amount must be positive.")
        else:
            print("Insufficient funds.")
            print("Your Balance is R", user_accounts[username]['balance'])
            amount_str = input("Enter amount? R")
            amount_str = amount_str.replace(" ", "")  # Remove spaces
            amount = float(amount_str)
            withdraw(user_accounts, username, amount)  # Recursive function
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            password = input("Enter your password: ")
            create_account(user_accounts, username, initial_balance, password)
        else:
            print("Transaction canceled.")


def log_transaction(username, transaction_type, amount, balance):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('transactionlog.txt', 'a') as log_file:
        log_file.write(f"{timestamp}, {username},{transaction_type},R{amount:.2f},Current Balance: R{balance:.2f}\n")


def view_transactions(username):
    with open('transactionlog.txt', 'r') as log_file:
        print("===== TRANSACTIONS =====")
        for line in log_file:
            transaction_info = line.strip().split(',')
            if len(transaction_info) == 5 and transaction_info[1].strip() == username:
                timestamp, _, transaction_type, amount, current_balance = transaction_info
                amount = float(amount[1:])  # Convert amount to float, excluding the 'R' symbol
                # Extract the numeric part from current_balance and convert it to float
                current_balance = float(current_balance[current_balance.index('R') + 1:])
                transaction_time = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime(
                    "%Y-%m-%d %H:%M:%S")
                print(f"Timestamp: {transaction_time}")
                print(f"{transaction_type}: R{amount:.2f}, Current Balance: R{current_balance:.2f}")
        print("===== END OF TRANSACTIONS =====")


# Register a function to save user accounts when the program exits
atexit.register(save_user_accounts)
