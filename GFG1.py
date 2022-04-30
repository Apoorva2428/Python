#Typecasting and doubling the numbers
"""n1=input("Enter your number: ")
n2=int(n1)
result=n2*2
print("Your doubled number is: ",result)"""

#Swapping 
"""a=int(input("Value of a: "))
b=int(input("Value of b: "))
c=a
a=b
b=c
print("Value after swapping",a,b)"""

#concatenate 
"""a=input("enter the value of a: ")
b=input("enter the value of b: ")
print("concatenate value",a+b)"""

#Union
"""set_a=input("Enter the values for set a: ")
set_b=input("Enter the values for set b: ")
print("Union of both set: ",set_a.union(set_b))"""
#Cannot take inputs???
"""set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {7, 8, 9, 10}
print("set1 U set2 : ", set1.union(set2))"""

#Subset (ISSUBSET)
"""a = {1, 4, 3}
b = {1, 4, 3, 2}
print(a.issubset(b))"""

#Printing with space/without space
"""a="Hello World"
b="Hello"
print(a+b)"""

#Arithmetic operators
"""a=8
b=3
print("First Number: ",a)
print("Second Number: ",b)
p=a+b
q=a-b
r=a*b
s=a/b
t=a//b
u=a%b
v=a**b

print("Addition: ",p)
print("Subtraction: ",q)
print("Multiplication: ",r)
print("Division: ",s)
print("Floor Division: ",t)
print("Modulus: ",u)
print("Exponential: ",v)"""

#Logical operators
"""a=int(input("enter a: "))
b=int(input("enter b: "))
p=a and b
q=a or b 
#not operator
print(p,q)"""

#AP term 
"""a=int(input("Enter starting value: "))
b=int(input("Enter common difference: "))
c=int(input("Enter the number of terms: "))
result=(a+(c-1))/b
print(result)
result_2=(a+result)*(c/2)
print(result_2)"""

#Loop 
"""n=5
i=0
while i<10:
    i=i+1
    print(n*i)"""

#Range
"""r=range(10,20)
l=list(r)
print(l)"""

#For loop
"""n=int(input("Enter n: "))
m=int(input("Enter m: "))

for i in range(1,m+1):
    print(i*n)"""

#Divisor 
"""n=int(input("Enter the number: "))
m=2
while m<=n:
    if n%m==0:
        print("Smallest divisor is: ",m)
        break
    m=m+1"""

#Divisor by for loop
"""n=int(input("Enter n: "))
for i in range(2,n+1):
    if n%i==0:
        print(i)
        break"""

#Continue 
"""l=[10,16,17,18,19,15]
for x in l:
    if x%5==0:
        continue
    print(x)"""

#Nested Loop 
"""l=int(input("enter l: "))
for x in range(1,l+1):
    for y in range(1,11):
        print(x*y)"""

#Sqaure printing
"""n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()"""

#Character at even indices
"""n=input("Input your word: ")
m=n[::2]
print(m)"""

#Decresing order
"""n=int(input("Enter your number: "))
i=0
while i<n:
    n=n-1
    print(n, end=" ")"""

#Table difference
"""n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
i=1
for i in range(1,11):
    result1=n1*i
    result2=n2*i
    if n1<n2:
        print("N1 is smaller than N2") 
    else:
        print(result1-result2, end=" ")"""
    
#Right Angle Triangle
"""height=int(input("Enter the height of triangle: "))
for i in range(1,height+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()"""

#Sum of first n natural number
"""n=int(input("Enter the first N natural number: "))
i=1
x=0
while i<=n:
    x=x+i
    i=i+1
print(x)"""

#Factorial of number
"""n=int(input("Enter the number: "))
i=1
x=1
while i<=n:
    x=x*i
    i=i+1
print(x)"""

#Divisor
"""n=int(input("Enter the number: "))
i=1
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")"""

#Checking prime 
"""n=int(input("Enter your number: "))
i=1
for i in range(2,n):
    if n%i==0:
        print("No this is not prime number")
        break
if n%i!=0:
        print("This is a prime number")"""

#Next Prime number
"""n=int(input("Enter the number: "))
x=0
i=0
for n in range(0,n+1):
    x=n+1
    for i in range(2,x+1):
        if x%i==0:
            print(x)"""
"""n=int(input("Enter the number: "))
p=n+1
for i in range(2,p):
        if(p%i==0):
            p=p+1
else:
    print("Next prime number is: ",p,end=" ")"""

#GCD
"""n1=int(input("Enter first number: "))
n2=int(input("Enter the second number: "))
i=1
while (i<=n1 and i<=n2):
    if n1%i==0 and n2%i==0:
        gcd=i
    i=i+1
print("GCD is: ",gcd)"""

#Capitalize and count
"""n=input("Input your sentence: ")
print(n.title())
length=len((n).split())
print(length)"""

#Function
"""def fun1():
    print("hello")
fun1()
"""
#Arguments
"""def arg(a,b):
    print(a+b)
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
arg(a,b)"""

#Return 
"""def return1(i):
    s=2*i
    return s
v=return1(2)
print(v)"""

#Practice
"""def summation(a,b,c):
    summ=a+b+c
    print(summ)
    return summ
print(summation(2,3,4))"""

#Return 2 values
"""def add_multiply(a,b):
    sum = a+b
    multi = a*b
    return (sum,multi)
s,m=add_multiply(5,4)
print(s,m)"""

#Function Harry
"""def a(x,y):
    print("Average of both the numbers: ",(x+y)/2)
v=a(7,5)
print(v)"""

#Try Except
"""n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
try:
    if n1>n2:
        print("Substraction: ",n1-n2)
except Exception as a:
    print(a)
print(n1-n2)"""

#First digit python
"""def first_digit(x):
    while x>=10:
        x=x//10
    return x
x=int(input("Enter the number: "))
print(first_digit(x))"""

#Factorial Number
"""n=int(input("Enter your number for factorial:" ))
i=1
for i in range(1,n):
    s=i+1
    multi=s*n
    print(multi)"""

#Plaindrome
"""n=int(input("Enter a number:"))
t=n
r=0
while(n>0):
    div=n%10
    r=r*10+div
    n=n//10
if(t==r):
    print("This number is palindrome!")
else:
    print("This is not a palindrome!")"""

#Armstrong
"""n=int(input("Enter a number:"))
sum = 0
t = n
while t > 0:
   digit = t % 10
   sum = sum + digit ** 3
   t //= 10

if n == sum:
   print("This is an Armstrong number")
else:
   print("This is not an Armstrong number")"""

#Greatest
"""n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if n1>n2:
    if n1>n3:
        print("Greatest number is: ",n1)
    else:
        print("Greatest number is: ",n3)

elif n2>n3:
    print("Greatest number is: ",n2)
else:
    print("Greatest number is: ",n3)"""

"""if n1<n2:
    if n1<n3:
        print(n1,"Smallest one is: ")
    else:
        print(n3,"Smallest one is: ")

elif n2<n3:
    print(n2, "Smallest")
else:
    print(n3,"Smallest")"""


"""def calc_area():
    r=int(input("Enter radius of circle: "))
    pi=22/7
    area= pi*r**2
    print("Area of the circle", str(r) + " is:", area)

n=int(input("Enter number of circles to calculate the area: "))
for i in range(n):
    calc_area()"""

"""def calc_area():
    a=int(input("Enter radius of circle:"))
    pi=22/7
    area= pi*a*a
    print("Area of the circle",area)

n=int(input("Enter number of circles to calculate the area:"))
for n in range(1,n+1):
    calc_area(n)"""

"""def calc_area():
    a=int(input("Enter radius of circle:"))
    b=str(a)
    pi=22/7
    area= pi*a*a
    print("Area of the circle of radius",b +", is: " ,area)
    return area

n=int(input("Enter number of circles to calculate the area:"))
for n in range(1,n+1):
    calc_area()"""


"""def calc_area():
    a=int(input("Enter radius of circle:"))
    b=str(a)
    pi=22/7
    area= pi*a*a
    print("Area of the circle of radius",b +", is: " ,area)
    return area

n=int(input("Enter number of circles to calculate the area:"))
for n in range(1,n+1):
    calc_area(n)"""

"""def calc_area(radius):
    pi=22/7
    area = (pi * (radius ** 2))
    print("Area of the circle of radius", str(radius) + " is: ", area)
    return area

n = int(input("Enter number of circles to calculate the area: "))
for i in range(n):
    radius = int(input("Enter radius of circle: "))
    calc_area(radius)"""

"""def calc_area():
    r=int(input("Enter radius of circle: "))
    pi=22/7
    area= pi*r**2
    print("Area of the circle", str(r) + " is:", area)
    return area

n=int(input("Enter number of circles to calculate the area: "))
for i in range(n):
    calc_area()"""

"""def multi():
    for i in range(1,11):
        a=n*i
    print(n,' x ', i, ' = ',a)
for n in range(2,21):
    print("Table of ", n)
multi()"""


def table():
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i)

num = int(input("Enter the number for table in between (2,20): "))
if 2<=num<=20:
    print(table())
else:
    print("Invalid Input")
