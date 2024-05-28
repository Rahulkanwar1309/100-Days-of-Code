import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    
    print(logo.logo)
    print("")
    
    num1 = float(input("What is your First Number : "))
    for symbol in operations:
        print(symbol)

    keep_going = True

    while keep_going:
        operation = input("pick your operation : ")
        num2 = float(input("What is your Second Number : "))

        operation_function = operations[operation]
        answer = operation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        keepGoing = input(f"Do you want to keep going with {answer} (yes or no) : ")
        if keepGoing == "yes":
            num1 = answer
        else:
            keep_going = False
            calculator()

calculator()





