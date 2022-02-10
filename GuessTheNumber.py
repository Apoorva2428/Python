print("You have to guess the number in between 1-10")
n = 5
print("Enter your guessed number")
n1= int(input())
if n1>6:
    print("Your guessed number is larger than my number")
elif n1==5:
    print("You have guessed the correct answer")
if n1<4:
    print("Your guessed number is smaller than my number")