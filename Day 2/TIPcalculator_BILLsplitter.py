print("Welcome to tip Calculator! ")
bill = float(input("What was the total bill? \n"))
tip = float(input("How much tip will you like to give? (in %) \n"))

total_bill = bill + ((tip/100)*bill)

print("Your total bill after tip is ", total_bill)

split = input("Do you wan to split the bill? (Y or N) \n")


if split == 'Y':
    number_of_people = int(input("How many people to split the bill? \n"))
    per_person = total_bill/number_of_people
    print("Each person should pay: ", per_person)
elif split == 'N':
    print("Have a Good Day!!")
else:
    print("Pick a valid input, Try Again")
    