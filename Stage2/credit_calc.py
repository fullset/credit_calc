import datetime

principal = int(input('Enter principal of credit:'))
periods = int(input('Enter count of periods:'))
interest = float(input('Enter interest rate: '))

print('Enter year, month and day of taking credit:')
year, month, day = map(int, input().split())
print(year)
print(month)
print(day)

repayment_date = datetime.datetime(year + int(periods / 12), int((periods % 12) + month), day)

i = interest / 1200
K = (i * ((1 + i) ** periods)) / ((1 + i) ** periods - 1)
A = K * principal

overpayment = A * periods - principal

print('Your everymonth payment: {0:.2f}'.format(A))
print('Your overpayment is: {0:.2f}'.format(overpayment))
print(repayment_date.date())

