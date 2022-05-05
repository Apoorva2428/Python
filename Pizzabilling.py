pizza=input("Enter the size of pizza you wanna order S for small M for mediam L for large ")
bill=0
if pizza=="S":
    bill=15
    print("You have selected small sized pizza for $15")
    peppo=input("Do you want pepporani? Y or N ")
    bills=0
    if peppo=="Y":
        bills=1
        print("Opted pepporani for small sized pizza $1")
    else:
        print("You have selected small sized pizza for $15")

elif pizza=="M":
    bill=20
    print("You have selected mediam sized pizza for $20")
    peppo=input("Do you want pepporani? Y or N ")
    bills=0
    if peppo=="Y":
        bills=2
        print("Opted pepporani for small sized pizza $2")
    else:
        print("You have selected small sized pizza for $20")

if pizza=="L":
    bill=25
    print("You have selected large sized pizza for $25")
    peppo=input("Do you want pepporani? Y or N ")
    if peppo=="Y":
        bills=3
        print("Opted pepporani for small sized pizza $3")
    else:
        print("You have selected small sized pizza for $25")

print("Your total bill is: ",int(bill+bills))
    