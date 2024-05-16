import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Random Password Generator!")

required_letters= int(input("How many letters would you like in your password?\n")) 
required_symbols = int(input(f"How many symbols would you like?\n"))
required_numbers = int(input(f"How many numbers would you like?\n"))

password_list =  []


for i in range(1, required_letters + 1):
    char = random.choice(letters)
    password_list.append(char)

for i in range(1, required_numbers + 1):
    num = random.choice(numbers)
    password_list.append(num)

for i in range(1, required_symbols + 1):
    symb = random.choice(symbols)
    password_list.append(symb)


random.shuffle(password_list)

password = "".join(password_list)

print(password)