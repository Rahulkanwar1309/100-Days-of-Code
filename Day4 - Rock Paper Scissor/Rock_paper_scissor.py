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

import random

print("Welcome to The Rock Paper Scissor game")
print("")

user_input = int(input("what will you choose? (0 for Rock, 1 for Paper, 2 for Scissors : "))
print("")

if user_input == 0 :
    print("Your chose Rock")
    print(rock)
    print("")
elif user_input == 1 :
    print("Your chose Paper")
    print(paper)
    print("")
elif user_input == 2 :
    print("Your chose Scissors")
    print(scissors)
    print("")
else:
    print("Enter valid input, Try Again")
    

computer_chooses = random.randint(0,2)

if computer_chooses == 0 :
    print("Computer chose Rock")
    print(rock)
    print("")
elif computer_chooses == 1 :
    print("Computer chose Paper")
    print(paper)
    print("")
else :
    print("Computer chose Scissors")
    print(scissors)
    print("")

if computer_chooses == 0:
    if user_input == 0:
        print("It's a draw")
    elif user_input == 1:
        print("You Win!!")
    elif user_input == 2:
        print("You Lose...")
    else:
        print("You lost because you did not input a valid number")

if computer_chooses == 1:
    if user_input == 0:
        print("You Lose...")
    elif user_input == 1:
        print("It's a draw")
    elif user_input == 2:
        print("You Win!!")
    else:
        print("You lost because you did not input a valid number")

if computer_chooses == 2:
    if user_input == 0:
        print("You Win!!")
    elif user_input == 1:
        print("You Lose...")
    elif user_input == 2:
        print("It's a draw")
    else:
        print("You lost because you did not input a valid number")