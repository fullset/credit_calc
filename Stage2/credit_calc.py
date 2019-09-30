import datetime
from calendar import monthrange


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


principal = int(input('Enter principal of credit:'))
periods = int(input('Enter count of periods:'))
interest = float(input('Enter interest rate: '))

print('Enter year, month and day of taking credit:')
year, month, day = map(int, input().split())
print(year)
print(month)
print(day)

repayment_date = calc_date(year, month, day, periods)

i = interest / 1200
K = (i * ((1 + i) ** periods)) / ((1 + i) ** periods - 1)
A = K * principal

overpayment = A * periods - principal

print('Your everymonth payment: {0:.2f}'.format(A))
print('Your overpayment is: {0:.2f}'.format(overpayment))
print(repayment_date.date())

