"""total=0
for n in range(1, 101):
    total+=n
    print(total)"""

#Adding Even 
"""total=0
for n in range(2,101,2):
    total+=n
print(total)"""

#FizzBuzz Program
for n in range(1,101):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%5==0:
        print("Buzz")
    elif n%3==0:
        print("Fizz")
    else:
        print(n)