# Simple Function
"""def calc_area():
    pi = 22 / 7
    area = pi * radius ** 2
    print(f"The area of circle is {area:.2f}")


for i in range(10):
    radius = int(input("Enter the radius of circle: "))
    calc_area()
"""
# Parameterized Function
"""def calc_area(radius):
    pi = 22 / 7
    area = pi * radius ** 2
    print(f"The area of circle is {area:.2f}")


for i in range(10):
    r = int(input("Enter the radius of circle: "))
    calc_area(r)"""

# Simple Function with Return
"""def calc_area():
    pi = 22 / 7
    area = pi * radius ** 2
    return area


for i in range(10):
    radius = int(input("Enter the radius of circle: "))
    print(f"The area of circle is {calc_area:.2f}")"""

# Parameterized Function with Return
"""def calc_area(radius):
    pi = 22 / 7
    area = pi * radius ** 2
    return area


for i in range(10):
    r = int(input("Enter the radius of circle: "))
    print(f"The area of circle is {calc_area(r):.2f}")"""


# Simple Function
def print_table():
    for i in range(2, 21):
        print(num, ' x ', i, ' = ', num * i)

num = int(input("Please Enter your number to print multiplication table: "))
print_table()

"""def print_table(num):
    for i in range(2, 21):
        print(num, ' x ', i, ' = ', num * i)

n = int(input("Please Enter your number to print multiplication table: "))
print_table(n)"""

"""def print_table():
    table = [num * i for i in range(2, 21)]
    return table

num = int(input("Please Enter a number to print its multiplication table: "))
table_returned = list(print_table())
k = 1
for j in table_returned:
    print(num, ' x ', k + 1, ' = ', j)
    k += 1"""

"""def print_table(num):
    table = [num * i for i in range(2, 21)]
    return table

n = int(input("Please Enter a number to print its multiplication table: "))
table_returned = list(print_table(n))
k = 1
for j in table_returned:
    print(n, ' x ', k + 1, ' = ', j)
    k += 1"""