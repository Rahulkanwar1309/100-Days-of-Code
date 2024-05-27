import os 
import art 

print(art.logo)
print("")

bids = {}

more_people = True

while more_people:
    
    name = input("What is your name : ")
    bid = int(input("What is your bid : $"))

    bids[name] = bid

    people_check = input("Are there more bidders : (yes or no)")

    if people_check == "yes":
        os.system('clear')
    elif people_check == "no":
        os.system('clear')
        more_people = False
        
highest_bid = 0
highest_bidder = ""

for i in bids:
    if highest_bid < bids[i]:
        highest_bid = bids[i]
        highest_bidder = i

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

