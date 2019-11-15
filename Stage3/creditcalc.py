# write your code here
import math
epsilon = 0.00001

print(
    """What do you want to calculate? 
type “n” - for count of months, 
type “a” - for annuity monthly payment,
type “p” - for credit principal"""
)

calc_type = input()

if calc_type is 'n':
    principal = float(input('Enter credit principal: '))
    payment = float(input('Enter monthly payment: '))
    interest = float(input('Enter credit interest: ')) / 1200
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
elif calc_type is 'a':
    principal = float(input('Enter credit principal: '))
    months = float(input('Enter count of periods: '))
    interest = float(input('Enter credit interest: ')) / 1200

    annuity = principal * (interest * (1 + interest) ** months)
    annuity = annuity / ((1 + interest) ** months - 1)

    if abs(annuity - int(annuity)) < epsilon:
        annuity = int(annuity)
    else:
        annuity = int(annuity) + 1

    print('Your annuity payment is {}!'.format(annuity))
elif calc_type is 'p':
    payment = float(input('Enter monthly payment: '))
    months = float(input('Enter count of periods: '))
    interest = float(input('Enter credit interest: ')) / 1200

    principal = payment / (interest * (1 + interest) ** months)
    principal = principal * ((1 + interest) ** months - 1)

    print('Your credit principal is {}!'.format(int(principal)))
else:
    print(
        'I can\'t calculate this: "{}". Please type "a", "p" or "n"'.format(type)
    )
