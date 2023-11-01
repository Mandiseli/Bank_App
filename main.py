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
                        print(f"Skipping invalid data: {line}")
                else:
                    print("WELCOME TO ONLINE BANKING")
    return user_accounts


def save_user_accounts(user_accounts):
    with open('Bank Data.txt', 'w') as file:
        for username, account_info in user_accounts.items():
            balance = account_info['balance']
            password = account_info['password']
            file.write(f"{username},{"Password:", password},{"Balance:", balance}\n")


def create_account(user_accounts, username, initial_balance, password):
    if username in user_accounts:
        print("Account already exists. Transaction canceled.")
    else:
        user_accounts[username] = {'balance': initial_balance, 'password': password}
        save_user_accounts(user_accounts)
        print("==========================================================")
        print(f"New account created with username: {username} and an initial balance of R{initial_balance}")
        print("==========================================================")



def login(username, user_accounts):
    entered_password = input("Enter your password: ")
    if entered_password == user_accounts[username]['password']:
        print("Login successful.")
        return True
    else:
        print("Password doesn't match. Login failed.")
        return False


def deposit(user_accounts, username, amount):
    if username in user_accounts:
        entered_password = input("Enter your password: ")
        if entered_password == user_accounts[username]['password']:
            user_accounts[username]['balance'] += amount
            save_user_accounts(user_accounts)
            log_transaction(username, "Deposit", amount, user_accounts[username]['balance'])
            print("=====DEPOSIT=====")
            print(f"Deposited R{amount}. New balance: R{user_accounts[username]['balance']}")
            print("=====DEPOSIT=====")
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
    # if username in user_accounts:
    balance = user_accounts[username]['balance']
    if balance >= amount:
        user_accounts[username]['balance'] -= amount
        save_user_accounts(user_accounts)
        log_transaction(username, "Withdrawal", amount, user_accounts[username]['balance'])
        print("======WITHDRAWAL======")
        print(f"Withdrew R{amount}. New balance: R{user_accounts[username]['balance']}")
    else:
        print("Balance", user_accounts[username]['balance'])
        print("Insufficient funds,enter less amount less")
        amount = input()
        withdraw(user_accounts, username, amount)

    # else:
    #     print("Account not found. Would you like to create a new account?")
    #     create_new_account = input("Enter 'yes' to create a new account: ").lower()
    #     if create_new_account == 'yes':
    #         initial_balance = float(input("Enter the initial balance for the new account: R"))
    #         password = input("Enter your password: ")
    #         create_account(user_accounts, username, initial_balance, password)
    #     else:
    #         print("Transaction canceled.")


def log_transaction(username, transaction_type, amount, balance):
    with open('transactionlog.txt', 'a') as log_file:
        log_file.write(f"{username},{transaction_type},R{amount},Current Balance: R{balance}\n")




while True:
    # Main program
    user_accounts = load_user_accounts()
    # print(user_accounts)
    print("Would you like to make a transaction? (yes or no)")
    user_answer1 = input().lower()

    if user_answer1 != 'yes':
        break

    username = input("Enter your account username: ").upper()
    if username not in user_accounts:
        print(f"Account '{username}' not found.")
        create_new_account = input("Would you like to create a new account? (yes or no)").lower()
        if create_new_account == 'yes':
            user_password = input("Enter your password: ")
            confirm_password = input("Please confirm password: ")
            if user_password != confirm_password:
                print("Password doesn't match")
                continue
            initial_balance = float(input("Enter the initial balance for the new account: R"))
            create_account(user_accounts, username, initial_balance, user_password)
        else:
            print("Transaction canceled.")
            continue
    else:
        if login(username, user_accounts):

            # user_password = input("Enter your password: ")
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
