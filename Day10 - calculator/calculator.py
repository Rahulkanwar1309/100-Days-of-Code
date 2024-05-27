import logo

print(logo.logo)
print("")

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

num1 = int(input("What is your First Number : "))
for symbol in operations:
    print(symbol)
operation = input("pick your operation : ")
num2 = int(input("What is your Second Number : "))

operation_function = operations[operation]
answer = operation_function(num1, num2)

print(f"{num1} {operation} {num2} = {answer}")





