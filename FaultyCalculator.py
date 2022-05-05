a = input("Operator")
x = int(input("Enter First No."))
y = int(input("Enter Second No."))
print("The Answer is:")
if x== 45 and y==3 and a=="*":
    print("555")
elif x== 56 and y==9 and a=="+":
    print("77")
elif x== 56 and y==6 and a=="/":
    print("4")
elif a== "+" :
    print(x + y)
elif a== "-":
    print(x - y)
elif a== "*":
    print(x * y)
elif a== "/":
    print(x / y)
else:
    print("Cannot perform this operation")