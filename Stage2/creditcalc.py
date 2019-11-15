# write your code here
epsilon = 0.00001
principal = float(input('Enter the credit principal: '))

print(
    """What do you want to calculate? 
type “m” - for count of months, 
type “p” - for monthly payment:"""
)

type = input()

if type is 'm':
    payment = float(input('Enter monthly payment: '))
    months = principal / payment
    if abs(int(months) * payment - principal) > epsilon:
        months = int(months) + 1
    else:
        months = int(months)
    print('It takes {} months to repay the credit'.format(months))
elif type is 'p':
    months = int(input('Enter count of months: '))
    payment = principal / months
    if abs(months * int(payment) - principal) < epsilon:
        payment = int(payment)
        print('Your monthly payment: {}'.format(payment))
    else:
        payment = int(payment) + 1
        last_payment = int(principal - payment * (months - 1))
        print('Your monthly payment = {} with last month payment = {}'.format(
            payment, last_payment
        ))
else:
    print(
        'I can\'t calculate this: "{}". Please type "p" or "m"'.format(type)
    )
