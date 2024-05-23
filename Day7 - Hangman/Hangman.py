from hangman_art import logo 
from hangman_art import stages
import random
from word_list import wordlist

print(logo)
print("")
print("Welcome to HANGMAN !!")



word = random.choice(wordlist)
print(word)

guess = input("Guess your letter:")

word_blank = []

word_blank.append("_" * len(word))

print(word_blank)




for i in word:
    if (guess == i):
        print("True") 
        index = word.index(i)
        word_blank[word[index]]=word[index]
        print(word_blank)
    else:
        print("False") 
    