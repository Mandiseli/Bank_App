import os
import re
from datetime import datetime

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


def deposit(user_accounts, username, amount):
    if username in user_accounts:
        entered_password = input("Enter your password: ")
        if entered_password == user_accounts[username]['password']:
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
            print("Password doesn't match. Transaction canceled.")
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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
    with open('transactionlog.txt', 'a') as log_file:
        log_file.write(f"{timestamp}, {username},{transaction_type},R{amount},Current Balance: R{balance}\n")


def view_transactions(username):
    with open('transactionlog.txt', 'r') as log_file:
        print("===== TRANSACTIONS =====")
        for line in log_file:
            transaction_info = line.strip().split(',')
            if len(transaction_info) == 5 and transaction_info[1] == username:
                timestamp, _, transaction_type, amount, current_balance = transaction_info
                transaction_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                print(f"Timestamp: {transaction_time}")
                print(f"{transaction_type}: R{amount}, Current Balance: R{current_balance}")
        print("===== END OF TRANSACTIONS =====")