#AB Interchange
"""a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=a
a=b
b=c
print("Interchanged values:",a,b)
"""
#Band Name generator
"""city=(input("Whats the name of city u grew up in?\n"))
pet=input("Whats your pet name?\n")
print("Your band name could be",city,pet)
"""
#Length of string
"""print(len("Hello my name is Apoorva"))
"""
#Individual writing
"""n="HELLO"
print(n[3])"""

#String With Integer (Type-Casting)
"""n1=len(input("Enter your name:"))
new_n1=str(n1)
print("Your name has " + new_n1 + " characters")"""

#Adding digits of a number
"""n1=(input("Enter a two digit number\t"))
first_digit=n1[0]
second_digit=n1[1]
print("Adding the digits:",int(first_digit)+int(second_digit))"""

#BMI Calculator
"""weight=int(input("Enter your weight in Kilograms:"))
height=float(input("Enter your height in metres:"))
result=int(weight/height**2)
print("Your BMI is:",result)"""

#Life In Weeks
age=int(input("Enter your age:"))
years_remaining=int(90-age)
days_remaining=int(years_remaining*365)
weeks_remaining=int(years_remaining*52)
months_remaining=int(years_remaining*12)
new_years_remaining=str(years_remaining)
new_days_remaining=str(days_remaining)
new_weeks_remaining=str(weeks_remaining)
new_months_remaining=str(months_remaining)
print("You have"+new_years_remaining+" years remaining, "+new_days_remaining+" days remaining, "+new_months_remaining+" months remaining, "+new_weeks_remaining+" weeks remaining")