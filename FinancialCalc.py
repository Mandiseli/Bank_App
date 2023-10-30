import math


def compound_interest(p, r, t):
    """
    :param p: deposited amount
    :param r: Interest rate
    :param t: Years
    :return: compound interest calculated
    """
    amount = p * math.pow((1 + r / 100), t)
    return amount


def simple_interest(p, r, t):
    amount = p * (1 + r / 100 * t)
    return amount  # Return the result instead of printing it


def calc_bond(p, r, t):
    x = r * p / (1 - math.pow(1 + r, -t))  # Fixed bond calculation formula
    return x


print("============================")
print("====FINANCIAL CALCULATOR====")
print("============================")

while True:
    print("============================")
    option1 = input("Choose either 'Investment' or 'Bond': ").strip().lower()

    if option1 == "exit":
        break

    if option1 == "investment":
        try:
            invest_amount = float(input("Enter the amount: "))
            interest_rate = float(input("Enter interest rate: "))
            years = int(input("Enter the number of years: "))

            interest = input("Choose 'Compound Interest' or 'Simple Interest': ").strip().lower()

            if interest == "compound":
                result = compound_interest(invest_amount, interest_rate, years)
                if result is not None:
                    print("Compound Interest:", result)
            elif interest == "simple":
                result = simple_interest(invest_amount, interest_rate, years)
                if result is not None:
                    print("Simple Interest:", result)
            else:
                print("Invalid interest type.")
        except ValueError:
            print("Invalid input. Please enter valid numbers for principal, interest rate, and time.")
    elif option1 == "bond":
        try:
            invest_amount = float(input("Enter the amount: "))
            interest_rate = float(input("Enter interest rate: "))
            years = int(input("Enter the number of years: "))

            result = calc_bond(invest_amount, interest_rate / 100, years)
            if result is not None:
                print("Bond Repayment: R", result)
        except ValueError:
            print("Invalid input. Please enter valid numbers for principal, interest rate, and time.")
    else:
        print("Invalid option. Please choose 'Investment' or 'Bond'.")
