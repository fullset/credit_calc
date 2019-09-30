import sys
import datetime
from calendar import monthrange, isleap


def calc_next_month(
        year_start: int,
        month_start: int,
        day_start: int
) -> datetime:
    temp_date = datetime.datetime(year_start + int(month_start / 12), int((month_start % 12) + 1), 1)

    days_current_month = monthrange(temp_date.year, temp_date.month)[1]

    if days_current_month < day_start:
        return datetime.datetime(temp_date.year, temp_date.month, days_current_month)
    else:
        return datetime.datetime(temp_date.year, temp_date.month, day_start)


def calc_date(
        year_start: int,
        month_start: int,
        day_start: int,
        periods_count: int
) -> datetime:
    temp_date = datetime.datetime(year_start + int(month_start / 12), int((month_start % 12) + 1), 1)
    for i in range(periods_count - 1):
        temp_date = datetime.datetime(
            temp_date.year + int(temp_date.month / 12),
            int((temp_date.month % 12) + 1),
            1
        )

    days_current_month = monthrange(temp_date.year, temp_date.month)[1]

    if days_current_month < day_start:
        return datetime.datetime(temp_date.year, temp_date.month, days_current_month)
    else:
        return datetime.datetime(temp_date.year, temp_date.month, day_start)


def calc_annuity_payment(principal: int, periods: int, interest: int) -> float:
    i = interest / 1200
    K = (i * ((1 + i) ** periods)) / ((1 + i) ** periods - 1)
    return K * principal


def calc_diff_payment(
        principal_value: int,
        periods_value: int,
        interest_value: int,
        period: int,
        start_date: datetime
) -> float:
    current_date = calc_date(start_date.year, start_date.month, start_date.day, period)
    days_current_month = monthrange(current_date.year, current_date.month)[1]
    days_current_year = 366 if isleap(current_date.year) else 365

    body = principal_value / periods_value
    percents = (principal_value - body * (period - 1)) * interest_value * days_current_month / (100 * days_current_year)
    return body + percents


if len(sys.argv) < 4:
    print('''
        You should start program with 6 args: 
        - credit principal;
        - count of periods;
        - credit interest rate;
        - year of start date;
        - month of start date;
        - day of start date.
        ''')
    exit(0)

principal = int(sys.argv[1])
periods = int(sys.argv[2])
interest = int(sys.argv[3])
year = int(sys.argv[4])
month = int(sys.argv[5])
day = int(sys.argv[6])

repayment_date = calc_date(year, month, day, periods)
format_str = '{0}:  {1:.2f} | {2:.2f} | {3:.2f}'

annuity_payment = calc_annuity_payment(principal, periods, interest)
date = calc_next_month(year, month, day)

for i in range(1, periods + 1):
    diff_payment = calc_diff_payment(principal, periods, interest, i, datetime.datetime(year, month, day))
    print(format_str.format(
        date.date(),
        diff_payment,
        annuity_payment,
        diff_payment - annuity_payment
    ))
    date = calc_next_month(date.year, date.month, day)

overpayment = annuity_payment * periods - principal

print('Your everymonth payment: {0:.2f}'.format(annuity_payment))
print('Your overpayment is: {0:.2f}'.format(overpayment))
print(repayment_date.date())
