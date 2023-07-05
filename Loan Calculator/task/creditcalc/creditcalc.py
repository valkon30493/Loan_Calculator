import argparse
import math

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Loan calculator")

parser.add_argument("--type", choices=["diff", "annuity"],
                    help="Choose only one of the two options: diff or annuity")
parser.add_argument("--principal", type=int, help="Loan principal")
parser.add_argument("--payment", type=int, help="Monthly payment amount")
parser.add_argument("--periods", type=int, help="Number of periods(months)")
parser.add_argument("--interest", type=float, help="Annual interest rate")

args = parser.parse_args()

# Incorrect parameters
# Type and interest should always be provided
if not args.type or not args.interest:
    print("Incorrect parameters")

# Type should always be equal to either "diff" or "annuity"
if args.type not in ["diff", "annuity"]:
    print("Incorrect parameters")

if args.type == "diff":
    if args.payment:
        print("Incorrect parameters")


if args.principal and args.principal < 0 or args.payment and args.payment < 0 or \
        args.periods and args.periods < 0 or args.interest and args.interest < 0:
    print("Negative values are not acceptable")


# function to calculate the amount of payments for the two different types
def calculate_payment(principal, periods, interest):
    if args.type == "annuity":
        nominal_rate = interest / (12 * 100)
        payment = principal * ((nominal_rate * pow(1 + nominal_rate, periods)) / (pow(1 + nominal_rate, periods) - 1))
        monthly_payment = math.ceil(payment)
        overpayment = (monthly_payment * periods) - principal

        print(f"Your annuity payment = {monthly_payment}!")
        print(f"Overpayment = {overpayment}")

    if args.type == "diff":
        nominal_rate = interest / (12 * 100)
        total = 0
        for k in range(1, periods + 1):
            payment = principal / periods + nominal_rate * (principal - (principal * (k - 1)) / periods)
            monthly_payment = math.ceil(payment)
            total = total + monthly_payment
            print(f"Month {k}: payment is {monthly_payment}")
        overpayment = total - principal
        print(f"Overpayment = {overpayment}")


# function to calculate the loan principal
def calculate_principal(payment, periods, interest):
    nominal_rate = interest / (12 * 100)
    principal = payment / ((nominal_rate * pow(1 + nominal_rate, periods)) / (pow(1 + nominal_rate, periods) - 1))
    total = payment * periods
    overpayment = total - principal
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {overpayment}")


# function to calculate how long it will take to repay the loan
def calculate_periods(principal, payment, interest):
    nominal_rate = interest / (12 * 100)
    periods = math.ceil(math.log(payment / (payment - (nominal_rate * principal)), 1 + nominal_rate))
    years = math.floor(periods // 12)
    months = periods % 12
    if years == periods // 12:
        print(f"It will take {years} years to repay this loan!")
    elif years == 0:
        print(f"It will take {months} months to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")
    total = periods * payment
    overpayment = total - principal
    print(f"Overpayment = {overpayment}")


if args.type and args.principal and args.periods and args.interest:
    calculate_payment(args.principal, args.periods, args.interest)
elif args.type and args.payment and args.periods and args.interest:
    calculate_principal(args.payment, args.periods, args.interest)
elif args.type and args.principal and args.payment and args.interest:
    calculate_periods(args.principal, args.payment, args.interest)