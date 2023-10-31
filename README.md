# Bank_App

`import os`: Import the `os` module for working with the operating system.

 `def load_user_accounts():`: Define a function to load user account information from a file.

 `user_accounts = {}`: Initialize an empty dictionary to store user account data.

`if os.path.exists('Bank Data.txt'):`: Check if the file "Bank Data.txt" exists.

`with open('Bank Data.txt', 'r') as file:`: Open the file for reading using a context manager.

`for line in file:`: Iterate through each line in the file.

`account_info = line.strip().split(',')`: Split each line into a list of username, password, and balance.

`username, balance = account_info[0], float(account_info[2])`: Extract the username and balance, converting balance to a float.

`user_accounts[username] = balance`: Update the `user_accounts` dictionary with username and balance.

`return user_accounts`: Return the user account data.

`def save_user_accounts(user_accounts):`: Define a function to save user account information to a file.

`with open('Bank Data.txt', 'w') as file:`: Open the file for writing using a context manager.

`for username, balance in user_accounts.items():`: Iterate through the user account data.

`file.write(f"{username},{balance}\n")`: Write the username and balance to the file.

`def create_account(user_accounts, username, initial_balance, password):`: Define a function to create a new user account.

`if username in user_accounts:`: Check if the username already exists.

`print("Account already exists. Transaction canceled.")`: Print a message if the account already exists.

`with open('Bank Data.txt', 'a') as file:`: Open the file for appending using a context manager.

`file.write(f"{username},{password},{initial_balance}\n")`: Write the new account info to the file.

`print(f"New account created with username: {username} and an initial balance of R{initial_balance}")`: Confirm the new account creation.

`user_accounts[username] = initial_balance`: Update the `user_accounts` dictionary with the new account.

`def deposit(user_accounts, username, amount):`: Define a function for making a deposit.

`if username in user_accounts:`: Check if the account exists.

`user_accounts[username] += amount`: Increase the account balance by the deposited amount.

`save_user_accounts(user_accounts)`: Update the data file with the new balance.

`log_transaction(username, "Deposit", amount, user_accounts[username])`: Log the deposit transaction.

`print(f"Deposited R{amount}. New balance: R{user_accounts[username]}")`: Confirm the deposit and show the updated balance.

`else:`: If the account doesn't exist.

`print("Account not found. Would you like to create a new account?")`: Prompt to create a new account.

`create_new_account = input("Enter 'yes' to create a new account: ").lower()`: Take user input to create a new account.

`if create_new_account == 'yes':`: If the user wants to create a new account.

`initial_balance = float(input("Enter the initial balance for the new account: R"))`: Prompt for the initial balance.

`password = input("Enter your password: ")`: Prompt for a password.

`create_account(user_accounts, username, initial_balance, password)`: Create a new account with provided details.

`print("Transaction canceled.")`: Cancel the transaction if the user doesn't want to create a new account.

`def withdraw(user_accounts, username, amount):`: Define a function for making a withdrawal.

`if username in user_accounts:`: Check if the account exists.

`if user_accounts[username] >= amount:`: Check if there are sufficient funds for withdrawal.

`user_accounts[username] -= amount`: Subtract the withdrawal amount from the balance.

`save_user_accounts(user_accounts)`: Update the data file with the new balance after the withdrawal.

`log_transaction(username, "Withdrawal", amount, user_accounts[username])`: Log the withdrawal transaction.

