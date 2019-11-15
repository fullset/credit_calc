# write your code here
import math
import argparse


def check_params() -> None:
    none_count = 0

    if args.payment_type is None or args.interest is None:
        print('Incorrect parameters')
        exit(0)

    if args.payment is None:
        none_count = none_count + 1
    if args.periods is None:
        none_count = none_count + 1
    if args.principal is None:
        none_count = none_count + 1

    if none_count != 1:
        print('Incorrect parameters')
        exit(0)

    if args.payment_type == 'diff' and args.payment is not None:
        print('Incorrect parameters')
        exit(0)


def calc_diff_payment(_args):
    epsilon = 0.00001
    principal = _args.principal
    periods = _args.periods
    interest = _args.interest / 1200

    payments = []

    for m in range(1, periods + 1):
        diff = principal - principal * (m - 1) / periods
        diff = principal / periods + interest * diff

        if abs(diff - int(diff)) < epsilon:
            diff = int(diff)
        else:
            diff = int(diff) + 1

        print('Month {}: paid out {}'.format(m, diff))
        payments.append(diff)

    paid = sum(item for item in payments)
    print("Overpayment: {}".format(int(paid - principal)))


def calc_annuity_payment(_args):
    epsilon = 0.00001
    principal = _args.principal
    months = _args.periods
    interest = _args.interest / 1200

    annuity = principal * (interest * (1 + interest) ** months)
    annuity = annuity / ((1 + interest) ** months - 1)

    if abs(annuity - int(annuity)) < epsilon:
        annuity = int(annuity)
    else:
        annuity = int(annuity) + 1

    print('Your annuity payment is {}!'.format(annuity))
    print("Overpayment: {}".format(int(months * annuity - principal)))


def calc_periods(_args):
    epsilon = 0.00001
    payment = _args.payment
    principal = _args.principal
    interest = _args.interest / 1200

    months = math.log(
        payment / (payment - principal * interest),
        1 + interest
    )
    if abs(int(months) * payment - principal) > epsilon:
        months = int(months) + 1
    else:
        months = int(months)

    if months < 12:
        print('It takes {} months to repay the credit'.format(months))
    elif months % 12 == 0:
        print('It takes {} years to repay the credit'.format(months / 12))
    else:
        print('It takes {} years {} months to repay the credit'.format(
            int(months / 12),
            months % 12
        ))
    print("Overpayment: {}".format(int(months * payment - principal)))


def calc_principal(_args):
    payment = _args.payment
    months = _args.periods
    interest = _args.interest / 1200

    principal = payment / (interest * (1 + interest) ** months)
    principal = principal * ((1 + interest) ** months - 1)

    print('Your credit principal is {}!'.format(int(principal)))
    print("Overpayment: {}".format(int(months * payment) - int(principal)))


parser = argparse.ArgumentParser()
parser.add_argument('--type', dest='payment_type', choices=['diff', 'annuity'])
parser.add_argument('--payment', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--principal', type=float)
args = parser.parse_args()

check_params()

if args.payment_type == 'diff':
    calc_diff_payment(args)
else:
    if args.payment is None:
        calc_annuity_payment(args)
    elif args.periods is None:
        calc_periods(args)
    else:
        calc_principal(args)
