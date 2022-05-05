def tax_calc(amount):
    if total_income <= 60000:
        tax = 0.0
    elif 60000 < total_income <= 150000:
        tax = (total_income - 60000) * 5 / 100
    elif 150000 < total_income <= 500000:
        tax = ((total_income - 150000) * 10 / 100)
    else:
        tax = ((total_income - 500000) * 15 / 100)
    return tax

name = input("Enter Name: ")
total_income = int(input("Enter Total Income: "))

print("Name: " + name)
print(f"Tax Payable: {tax_calc(total_income)} ")