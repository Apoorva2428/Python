while(True):
    print("Enter a number:")
    n1=int(input())
    if n1>100:
        print("The number entered is greater than 100")
        break
    else:
        print("The number is not greater than 100")
        continue