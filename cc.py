#1 Number Mirror
"""x=int(input())
print(x)"""

#2 Enormous Input Test
"""n=int(input())
k=int(input)
ans=0
for i in range(n):
    x=int(input())
    if x%k==0:
        ans+=1
print(ans)"""


"""n,k=(input().split(' '))
x=int(n)
y=int(k)
ans=0
for i in range(x):
    a=int(input())
    if a%y==0:
        ans+=1
print(ans)"""

#3 Find Remainder
"""t=int(input())
for i in range(t):
    a,b=(input().split(' '))
    x=int(a)
    y=int(b)
    print(x%y)"""

#4 Sun of digits
"""t=int(input())
sum=0
for i in range(t):
    a=int(input())
    while (n!=0):
        sum=sum+(n%10)
        n=n//10
    print(sum)"""

"""x,y=input().split(' ')
a=int(x)
b=("{0:.2f}".format(y))
b=float(y)
if a%5==0:
    if a<b:
        print(b-a-0.5)
    elif a>b:
        print(b)
else:
    print(b)"""


"""class Student:
    student_id = '20BCS1127'
    student_name = 'Apoorva Patel'

for i, value in Student.__dict__.items():
    if not i.startswith('_'):
        print(f'{i} -> {value}')
print()
print("Adding attribute")
Student.student_class = '601-B'
for i, value in Student.__dict__.items():
    if not i.startswith('_'):
        print(f'{i} -> {value}')
print()
print("Deleting attribute")
del Student.student_name
#deli(Student, 'student_name')
for i, value in Student.__dict__.items():
    if not i.startswith('_'):
        print(f'{i} -> {value}')
"""

"""class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
       
    def area(self):
        return self.length * self.width
   
l=int(input("Please Enter Length of Rectangle : "))
w=int(input("Please Enter width of Rectangle : "))
r = Rectangle(l, w)
print("Area of Rectangle is : ",r.area())"""

class Circle():
    def __init__(self, r):
        self.radius =8 

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14
 
radius = int(input("Enter radius of circle: "))
circle = Circle(radius)
print(circle.area())
print(circle.perimeter())
