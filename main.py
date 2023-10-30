import os

#
def load_user_accounts():
    """
    Function to create or load user accounts

    """
    user_accounts = {}
    if os.path.exists('Bank Data.txt'):
        with open('Bank Data.txt', 'r') as file:
            for line in file:
                account_info = line.strip().split(',')
                username, balance = account_info[0], float(account_info[1])
                user_accounts[username] = balance
    return user_accounts

# Function to save user accounts to a file
def save_user_accounts(user_accounts):
    with open('Bank Data.txt', 'w') as file:
        for username, balance in user_accounts.items():
            file.write(f"{username},{balance}\n")

# Function to create a new account
def create_account(user_accounts, username, initial_balance):
    user_accounts[username] = initial_balance
    save_user_accounts(user_accounts)
    print(f"New account created with an initial balance of R{initial_balance}")

# Function to perform a deposit and log the transaction
def deposit(user_accounts, username, amount):
    if username in user_accounts:
        user_accounts[username] += amount
        save_user_accounts(user_accounts)
        log_transaction(username, "Deposit", amount)
        print(f"Deposited R{amount}. New balance: R{user_accounts[username]}")
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            create_account(user_accounts, username, initial_balance)
        else:
            print("Transaction canceled.")

# Function to perform a withdrawal and log the transaction
def withdraw(user_accounts, username, amount):
    if username in user_accounts:
        if user_accounts[username] >= amount:
            user_accounts[username] -= amount
            save_user_accounts(user_accounts)
            log_transaction(username, "Withdrawal", amount)
            print(f"Withdrew R{amount}. New balance: R{user_accounts[username]}")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            create_account(user_accounts, username, initial_balance)
        else:
            print("Transaction canceled.")

# Function to log a transaction
def log_transaction(username, transaction_type, amount):
    with open('transactionlog.txt', 'a') as log_file:
        log_file.write(f"{username},{transaction_type},R{amount}\n")

# Main program
user_accounts = load_user_accounts()

while True:
    print("Would you like to make a transaction? (yes or no)")
    user_answer1 = input().lower()

    if user_answer1 != 'yes':
        break

    print("Would you like to make a deposit or withdrawal? (deposit or withdraw)")
    transaction_type = input().lower()

    if transaction_type != 'deposit' and transaction_type != 'withdraw':
        print("Invalid transaction type. Please choose 'deposit' or 'withdraw'.")
        continue

    username = input("Enter your account username: ")

    if username not in user_accounts:
        print(f"Account '{username}' not found.")
        create_new_account = input("Account not found. Would you like to create a new account? (yes or no)").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            create_account(user_accounts, username, initial_balance)
        else:
            print("Transaction canceled.")
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
