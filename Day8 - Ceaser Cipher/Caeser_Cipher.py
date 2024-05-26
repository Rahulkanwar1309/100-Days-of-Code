from caeser_cipher_art import logo

print(logo)
print("")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(given_text, shift_number, cypher_direction):
    ciper_text = ""

    if cypher_direction == "decode":
          shift_number *= -1
    
    for i in given_text:
        if i in letters:
            position = letters.index(i)
            new_position = position + shift_number
            new_letter = letters[new_position]
            ciper_text += new_letter
        else:
             ciper_text += i

    print(f"Your {cypher_direction}d text is {ciper_text}")

repeat = True       
while repeat:
    
    discription = input('Do You want to "encode" or "decode"\n')
    text = input("Type your message : \n").lower()
    shift = int(input("What is your shift : \n"))
    shift = shift % 26

    cipher(text, shift, discription)

    redo = input("Type 'yes' if you want to do it again, else type 'no'")

    if redo == "yes":
        repeat = True
    elif redo == "no":
        repeat = False
        print("Good Bye")

