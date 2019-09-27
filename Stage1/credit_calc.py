principal = int(input('Enter principal of credit:'))
periods = int(input('Enter count of periods:'))
interest = float(input('Enter interest rate: '))

i = interest / 1200
K = (i * ((1 + i) ** periods)) / ((1 + i) ** periods - 1)
A = K * principal

print('Your everymonth payment: {0:.2f}'.format(A))

