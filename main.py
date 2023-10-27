import os

# Function to create or load user accounts
def load_user_accounts():
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
    print(f"New account created with an initial balance of ${initial_balance}")

# Function to perform a deposit
def deposit(user_accounts, username, amount):
    if username in user_accounts:
        user_accounts[username] += amount
        save_user_accounts(user_accounts)
        print(f"Deposited ${amount}. New balance: ${user_accounts[username]}")
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: $"))
            create_account(user_accounts, username, initial_balance)
        else:
            print("Transaction canceled.")

# Function to perform a withdrawal
def withdraw(user_accounts, username, amount):
    if username in user_accounts:
        if user_accounts[username] >= amount:
            user_accounts[username] -= amount
            save_user_accounts(user_accounts)
            print(f"Withdrew ${amount}. New balance: ${user_accounts[username]}")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found. Would you like to create a new account?")
        create_new_account = input("Enter 'yes' to create a new account: ").lower()
        if create_new_account == 'yes':
            initial_balance = float(input("Enter the initial balance for the new account: $"))
            create_account(user_accounts, username, initial_balance)
        else:
            print("Transaction canceled.")

# Main program
user_accounts = load_user_accounts()

while True:
    print("Would you like to make a transaction? (yes or no)")
    user_response = input().lower()

    if user_response != 'yes':
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
            initial_balance = float(input("Enter the initial balance for the new account: $"))
            create_account(user_accounts, username, initial_balance)
        else:
            print("Transaction canceled.")
            continue

    if transaction_type == 'deposit':
        try:
            amount = float(input("How much would you like to deposit? $"))
            deposit(user_accounts, username, amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif transaction_type == 'withdraw':
        try:
            amount = float(input("How much would you like to withdraw? $"))
            withdraw(user_accounts, username, amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("Thank you for using the Bank Application")
