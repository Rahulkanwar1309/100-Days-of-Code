from data import MENU, resources

user = input("What Would You Like To Drink ? (espresso/latte/cappuccino) : ")

def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"""
    Water : {water}
    Milk : {milk}
    Coffee : {coffee}
    Money : {money}
    """)

def resource_check():
    