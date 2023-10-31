import os


def load_user_accounts():
    user_accounts = {}
    if os.path.exists('Bank Data.txt'):
        with open('Bank Data.txt', 'r') as file:
            for line in file:
                account_info = line.strip().split(',')
                username, balance = account_info[0], float(account_info[2])  # Corrected the index for balance
                user_accounts[username] = balance
    return user_accounts


def save_user_accounts(user_accounts):
    with open('Bank Data.txt', 'w') as file:
        for username, balance in user_accounts.items():
            file.write(f"{username},{balance}\n")


def create_account(user_accounts, username, initial_balance, password):  # Added password as a parameter
    # Check if the username already exists
    if username in user_accounts:
        print("Account already exists. Transaction canceled.")
        return

    # Save the username, password, and initial balance in 'Bank Data.txt'
    with open('Bank Data.txt', 'a') as file:
        file.write(f"{username},{password},{initial_balance}\n")

    print(f"New account created with username: {username} and an initial balance of R{initial_balance}")
    user_accounts[username] = initial_balance


def deposit(user_accounts, username, amount):
    if username in user_accounts:
        # Increment the balance by the deposit amount
        user_accounts[username] += amount
        save_user_accounts(user_accounts)
        log_transaction(username, "Deposit", amount, user_accounts[username])
        print(f"Deposited R{amount}. New balance: R{user_accounts[username]}")
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            password = input("Enter your password: ")  # Added password input
            create_account(user_accounts, username, initial_balance, password)
        else:
            print("Transaction canceled.")


def withdraw(user_accounts, username, amount):
    if username in user_accounts:
        if user_accounts[username] >= amount:
            # Decrement the balance by the withdrawal amount
            user_accounts[username] -= amount
            save_user_accounts(user_accounts)
            log_transaction(username, "Withdrawal", amount, user_accounts[username])
            print(f"Withdrew R{amount}. New balance: R{user_accounts[username]}")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            password = input("Enter your password: ")  # Added password input
            create_account(user_accounts, username, initial_balance, password)
        else:
            print("Transaction canceled.")


def log_transaction(username, transaction_type, amount, balance):
    with open('transactionlog.txt', 'a') as log_file:
        log_file.write(f"{username},{transaction_type},R{amount},Current Balance: R{balance}\n")


# Main program
user_accounts = load_user_accounts()

while True:
    print("Would you like to make a transaction? (yes or no)")
    user_answer1 = input().lower()

    if user_answer1 != 'yes':
        break

    username = input("Enter your account username: ")
    if username not in user_accounts:
        print(f"Account '{username}' not found.")
        create_new_account = input("Would you like to create a new account? (yes or no)").lower()
        if create_new_account == 'yes':
            user_password = input("Enter your password: ")  # Added password input
            confirm_password = input("Please confirm password: ")
            if user_password != confirm_password:
                print("Password doesn't match")
                continue
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            create_account(user_accounts, username, initial_balance, user_password)  # Passed the password
        else:
            print("Transaction canceled.")
            continue

    print("Would you like to make a deposit or withdrawal? (deposit or withdraw)")
    transaction_type = input().lower()

    if transaction_type != 'deposit' and transaction_type != 'withdraw':
        print("Invalid transaction type. Please choose 'deposit' or 'withdraw'.")
        continue

    if transaction_type == 'deposit':
        try:
            amount = float(input("How much would you like to deposit? R"))
            deposit(user_accounts, username, amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif transaction_type == 'withdraw':
        try:
            amount = float(input("How much would you like to withdraw? R"))
            withdraw(user_accounts, username, amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("Thank you for using the Bank Application")
import os


def load_user_accounts():
    user_accounts = {}
    if os.path.exists('Bank Data.txt'):
        with open('Bank Data.txt', 'r') as file:
            for line in file:
                account_info = line.strip().split(',')
                username, balance = account_info[0], float(account_info[2])  # Corrected the index for balance
                user_accounts[username] = balance
    return user_accounts


def save_user_accounts(user_accounts):
    with open('Bank Data.txt', 'w') as file:
        for username, balance in user_accounts.items():
            file.write(f"{username},{balance}\n")


def create_account(user_accounts, username, initial_balance, password):  # Added password as a parameter
    # Check if the username already exists
    if username in user_accounts:
        print("Account already exists. Transaction canceled.")
        return

    # Save the username, password, and initial balance in 'Bank Data.txt'
    with open('Bank Data.txt', 'a') as file:
        file.write(f"{username},{password},{initial_balance}\n")

    print(f"New account created with username: {username} and an initial balance of R{initial_balance}")
    user_accounts[username] = initial_balance


def deposit(user_accounts, username, amount):
    if username in user_accounts:
        # Increment the balance by the deposit amount
        user_accounts[username] += amount
        save_user_accounts(user_accounts)
        log_transaction(username, "Deposit", amount, user_accounts[username])
        print(f"Deposited R{amount}. New balance: R{user_accounts[username]}")
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            password = input("Enter your password: ")  # Added password input
            create_account(user_accounts, username, initial_balance, password)
        else:
            print("Transaction canceled.")


def withdraw(user_accounts, username, amount):
    if username in user_accounts:
        if user_accounts[username] >= amount:
            # Decrement the balance by the withdrawal amount
            user_accounts[username] -= amount
            save_user_accounts(user_accounts)
            log_transaction(username, "Withdrawal", amount, user_accounts[username])
            print(f"Withdrew R{amount}. New balance: R{user_accounts[username]}")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            password = input("Enter your password: ")  # Added password input
            create_account(user_accounts, username, initial_balance, password)
        else:
            print("Transaction canceled.")


def log_transaction(username, transaction_type, amount, balance):
    with open('transactionlog.txt', 'a') as log_file:
        log_file.write(f"{username},{transaction_type},R{amount},Current Balance: R{balance}\n")


# Main program
user_accounts = load_user_accounts()

while True:
    print("Would you like to make a transaction? (yes or no)")
    user_answer1 = input().lower()

    if user_answer1 != 'yes':
        break

    username = input("Enter your account username: ")
    if username not in user_accounts:
        print(f"Account '{username}' not found.")
        create_new_account = input("Would you like to create a new account? (yes or no)").lower()
        if create_new_account == 'yes':
            user_password = input("Enter your password: ")  # Added password input
            confirm_password = input("Please confirm password: ")
            if user_password != confirm_password:
                print("Password doesn't match")
                continue
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            create_account(user_accounts, username, initial_balance, user_password)  # Passed the password
        else:
            print("Transaction canceled.")
            continue

    print("Would you like to make a deposit or withdrawal? (deposit or withdraw)")
    transaction_type = input().lower()

    if transaction_type != 'deposit' and transaction_type != 'withdraw':
        print("Invalid transaction type. Please choose 'deposit' or 'withdraw'.")
        continue

    if transaction_type == 'deposit':
        try:
            amount = float(input("How much would you like to deposit? R"))
            deposit(user_accounts, username, amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif transaction_type == 'withdraw':
        try:
            amount = float(input("How much would you like to withdraw? R"))
            withdraw(user_accounts, username, amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("Thank you for using the Bank Application")
