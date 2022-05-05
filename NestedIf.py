#RollerCoaster Ride
"""height=int(input("Enter your height in cm: "))
if height>=180:
    print("Allowed to ride")
    age=int(input("Enter your age: "))
    if age>10:
        print("You have to pay $15 for ride.")
    else:
        print("You have to pay $7 for ride.")
else:
    print("Not allowed")"""

#BMI calculator 2.0
"""height=float(input("Enter your height in m: "))
weight=int(input("Enter your weight in kg: "))
BMI=round(weight/height**2)
print("Your BMI is: ",BMI)
if BMI<=18.5:
    print("You are underweight")
elif 18.5<BMI<=25:
    print("You have normal weight")
elif 25<BMI<=30:
    print("You are overweight")
elif 30<BMI<=35:
    print("You are obese")
else:
    print("You are clinically obese")"""

#Leap-Year 
"""year=int(input("Enter the year: "))
if year%4==0:
    print("This year is leap year.")
else:
    print("This is not a leap year")"""

#Roller-Coaster with Photo
height=int(input("Enter your height in cm: "))
bill=0
if height>=180:
    print("Allowed to ride")
    age=int(input("Enter your age: "))
    if age>10:
        bill=15
        print("You have to pay $15 for ride.")
    else:
        bill=7
        print("You have to pay $7 for ride.")
    wants_photo=input("Do you want photo for ride? $3/photo Press Y or N ")
    if wants_photo=="Y":
        print("Your total bill is: ",int(bill+3))
    else:
        print("Ok Enjoy the ride")
else:
    print("Not allowed")