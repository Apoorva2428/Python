#Chars at even index
"""n1=input("Input string: ")
n2=list(n1)
for i in n2[::2]:
    print(i)"""

#First 10 natural numbers using while loop
"""n1=0
while n1<10:
    n1=n1+1
    print("First 10 natural number: ",n1)"""

#Pattern printing
"""n1=5
for i in range(1,n1+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print("")"""

#Calculate the sum of all numbers from 1 to a given number
"""s = 0
n = int(input("Enter number "))
# for i in range(1, n + 1, 1):
#     s += i
# print("Sum is: ", s)
for i in range(1,n+1):
    s=i+s
print(s)"""

#Multiplication of a given number
"""n1=int(input("Enter the number: "))
i=1
for i in range(0,10):
    i=i+1
    multi=i*n1
    print(multi)"""

#Display number from a list using loop
"""numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)"""

#Printing prime numbers in loop
"""n1=int(input("Enter starting point: "))
n2=int(input("Enter end point: "))
for num in range(n1,n2+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)"""

#Cube of numbers
"""n=int(input("Enter number: "))
i=1
for i in range(1,n+1):
    cube=i**3
    print(cube)"""

#Create function
"""def name_age(n,a):
    print(n,a)
name_age("Apoorva",21)"""

#Subject
"""s_1 = 91
s_2 = 92
s_3 = 93
s_4 = 94
s_5 = 95
print("Marks of five subjects: ",s_1,s_2,s_3,s_4,s_5)

total = s_1 + s_2 + s_3 + s_4 + s_5
average = total / 5.0
percentage = (total / 500.0) * 100

print("The Total marks is: ", total, "/ 500.00")
print("The Average marks is: ", average)
print("The Percentage is: ", percentage, "%")"""


#CM M KM 
"""cm =2345
print("Length in cm: ",cm)
meter = cm / 100.0
kilometer = cm / 100000.0
print("Length in meter = ",meter , "m")
print("Length in Kilometer = ",kilometer , "km")"""

#List Tuple
"""n=(input("Enter the numbers: "))
list=n.split(",")
tuple=tuple(list)
print(list)
print(tuple)"""

#Colour List
"""color_list = ["Red","Green","White" ,"Black"]
print(color_list[0::3])"""

#Exam Schedule
"""exam_st_date = (11, 12, 2014)
print("%i / %i / %i"%exam_st_date)"""

#n+nn+nnn
