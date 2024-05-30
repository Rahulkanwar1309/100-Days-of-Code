import random

num = random.randint(1, 101)

print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")

def games():
    guess = int(input("Guess The Number: "))
    if guess > num:
        print("Too High")
        return False
    elif guess < num:
        print("Too Low")
        return False
    else:
        print("You Win !!")
        return True

game = True
while game:
    difficulty = input("What difficulty do you want 'hard' or 'easy'? ")
    
    if difficulty.lower() == "hard":
        tries = 5
    elif difficulty.lower() == "easy":
        tires = 10
    else:
        print("Invalid difficulty. Try again.")
        continue
    
    for i in range(tries):
        if games():
            game = False
            break
        print(f"You have {tries - i - 1} attempts remaining")
    
    if game: 
        print("You Lose...")
        break  
