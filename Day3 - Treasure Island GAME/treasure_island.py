print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print('')
print("Welcome to the Treasure Island")
print("Your goal today is to made smart decision that will take you to your treasure")
print("")
print("LETS BEGIN")
print("")

print("You came deep into a forest and are now stand where the road splits")
print("Which direction road will you pick? (left or right)")

road = input("Pick carefully : ")
print("")

if road == "right":
    print("Now that road brought you to a lake")
    lake = input("Will you wait for a boat or will you swim through it? (W : wait and S : swim) ")
    print("")
    if lake == "W":
        print("When you crossed teh lake there was a temple, you entered it")
        print("There are 3 doors inside Red, Blue and Yellow")
        doors = input("Which door will you pick? (R/B/Y) ")
        print("")
        if doors == "R":
            print("There was fire behind it which burnt you")
            print("GAME OVER")
        elif doors == "B":
            print("There was a hungry tiger behind it")
            print("GAME OVER")
        elif doors == "Y":
            print("CONGRATS")
            print("You got the treasure")
            print("YOU WIN")
    elif lake == "S":
        print("There were crocodiles in the lake, you died")
        print("GAME OVER")
    else:
        print("Enter valid response, Try Again")
elif road == "left":
    print("You crossed paths with another group of not so friendly Treasure Hunters, and the kicked you off the island")
    print("GAME OVER")
else:
    print("Enter valid response, Try Again")