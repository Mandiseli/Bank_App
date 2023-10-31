import os

def load_user_accounts():
    user_accounts = {}
    if os.path.exists('Bank Data.txt'):
        with open('Bank Data.txt', 'r') as file:
            for line in file:
                account_info = line.strip().split(',')
                if len(account_info) == 3:
                    username, password, balance = account_info
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
    with open('transactionlog.txt', 'a') as log_file:
        log_file.write(f"{username},{transaction_type},R{amount},Current Balance: R{balance}\n")

def main_menu():
    print("1. New account")
    print("2. Login")
    print("3. Exit")

def transaction_menu():
    print("Current Balance for {}: R{:.2f}".format(username, user_accounts[username]['balance']))
    print("Would you like to deposit or withdraw?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

# Main program
user_accounts = load_user_accounts()

while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter your desired username: ").upper()
        if username == "":
            print("Username cannot be empty. Transaction canceled.")
            continue
        if username in user_accounts:
            print("Username already exists. Please choose another username.")
            continue
        user_password = input("Enter your password: ")
        confirm_password = input("Please confirm password: ")
        if user_password != confirm_password:
            print("Password doesn't match")
            continue
        initial_balance_str = input("Enter the initial balance for the new account: R")
        initial_balance_str = initial_balance_str.replace(" ", "")  # Remove spaces
        initial_balance = float(initial_balance_str)
        create_account(user_accounts, username, initial_balance, user_password)

        while True:
            transaction_menu()
            transaction_choice = input("Enter your choice: ")
            if transaction_choice == "1":
                try:
                    amount_str = input("How much would you like to deposit? R")
                    amount_str = amount_str.replace(" ", "")  # Remove spaces
                    amount = float(amount_str)
                    deposit(user_accounts, username, amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif transaction_choice == "2":
                try:
                    amount_str = input("How much would you like to withdraw? R")
                    amount_str = amount_str.replace(" ", "")  # Remove spaces
                    amount = float(amount_str)
                    withdraw(user_accounts, username, amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                break

    elif choice == "2":
        username = input("Enter your account username: ").upper()
        if username == "":
            print("Username cannot be empty. Transaction canceled.")
            continue
        user_password = input("Enter your password: ")
        if username not in user_accounts or user_accounts[username]['password'] != user_password:
            print("Invalid username or password. Please try again.")
            continue

        while True:
            transaction_menu()
            transaction_choice = input("Enter your choice: ")
            if transaction_choice == "1":
                try:
                    amount_str = input("How much would you like to deposit? R")
                    amount_str = amount_str.replace(" ", "")  # Remove spaces
                    amount = float(amount_str)
                    deposit(user_accounts, username, amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif transaction_choice == "2":
                try:
                    amount_str = input("How much would you like to withdraw? R")
                    amount_str = amount_str.replace(" ", "")  # Remove spaces
                    amount = float(amount_str)
                    withdraw(user_accounts, username, amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                break

    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


print("Thank you for using our Bank Application")