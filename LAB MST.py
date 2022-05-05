def calc(cost):
    if cost < 2000:
        amt = cost - (cost * 5 / 100.0)
    elif cost < 5000:
        amt = cost - (cost * 25 / 100.0)
    elif cost < 10000:
        amt = cost - (cost * 35 / 100.0)
    else:
        amt = cost - (cost * 50 / 100.0)
    return amt

price = float(input('Enter the total cost: '))
amount = calc(price)
print('Total amount to be paid = ' + str(amount))