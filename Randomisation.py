#Random no print
"""import random
random_integer=random.randint(1,100)
print(random_integer)

random_float=random.random()
print(random_float)"""

#Heads Or Tails
"""import random
random_side=random.randint(0,1)
if random_side==1:
    print("Heads")
else:
    print("Tails")"""

#Banker Roulette
"""import random
names=input("Who will pay give the names\n")
banker=names.split(",")
n1=(len(banker))
n2=random.randint(0,n1-1)
who_will_pay=names[n2]
print(who_will_pay+" The person who is going to pay today.")
"""
#Row Column
"""row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = (input("Where do you want to put the treasure? "))
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")"""

#Rock Paper Scissor 
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock, paper, scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_input])

computer_input=random.randint(0,2)
print("Computer choice")
print(game_images[computer_input])

if user_input >= 3 or user_input < 0: 
  print("You typed an invalid number, you lose!") 
elif user_input == 0 and computer_input == 2:
  print("You win!")
elif computer_input == 0 and user_input == 2:
  print("You lose")
elif computer_input > user_input:
  print("You lose")
elif user_input > computer_input:
  print("You win!")
elif computer_input == user_input:
  print("It's a draw")