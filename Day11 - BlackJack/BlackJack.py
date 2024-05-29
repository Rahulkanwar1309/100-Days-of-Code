import random
import logo
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
    
    print(logo.logo)
    a = random.choice(cards)
    b = random.choice(cards) 

    intial_hand = [a, b]

    print(f"Your hand is : {intial_hand}, current score = {sum(intial_hand)}")

    c1 = random.choice(cards)

    computers_hand = [c1]

    print(f" Computer's first card : {computers_hand}, computer's score = {c1}")
    hit = True

    while hit:

        hit_or_pass = input("Do you want to get another card 'y' or 'n'")

        if hit_or_pass == "y":
            c = random.choice(cards)
            intial_hand.append(c)
            print(f"Your final hand is : {intial_hand}, current score = {sum(intial_hand)}")

            if sum(intial_hand) > 21 :
                print("You Lose....")
                hit = False

        elif hit_or_pass == "n":

            print(f"Your final hand is : {intial_hand}, current score = {sum(intial_hand)}")
            
            hit = False
    while sum(computers_hand) < 17:
        c2 = random.choice(cards)
        computers_hand.append(c2)
    
    print(f"Computer's final hand is : {computers_hand}, current score = {sum(computers_hand)}")    
    
    if sum(computers_hand) > 21 or sum(intial_hand) > sum(computers_hand):
        print("You Win !!")
    elif sum(computers_hand) > sum(intial_hand):
        print("You Lose...")
    else:
        print("It is a draw")

play = True

while play:        
    play = input("Do you want to play a Game of Black Jack ('y' or 'n')")

    if play == "y":
        os.system('clear')
        blackjack()

    else:
        play = False       