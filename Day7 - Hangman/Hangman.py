from hangman_art import logo 
from hangman_art import stages
from word_list import wordlist
import random

print(logo)
print("")
print("Welcome to HANGMAN !!")

word = random.choice(wordlist)

print(word)
print("")
print("It is a", len(word), " letter word")
print("")

word_blank = []

lives = 6
hangman = -1

for i in word:
    word_blank.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess your letter:").lower()
    
    for i in word:
        letter = word.index(i)
        if (guess == i):
            word_blank[letter] = i

    if guess not in word:
        lives -= 1
        print(f"You have guessed {guess}, and hence its not in the word YOU LOSE A LIFE!")
        print(stages[hangman])
        hangman -= 1
       
    print(word_blank) 
    
    if "_" not in word_blank:
        end_of_game = True
        print("You Have Won")

    if lives == 0:
        end_of_game = True
        print(stages[0])
        print("You Lost!!")
        



