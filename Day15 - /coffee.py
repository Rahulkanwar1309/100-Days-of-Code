from data import MENU, resources

profit = 0

def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    
    print (f"""
    Water : {water}
    Milk : {milk}
    Coffee : {coffee}
    Money : {profit}
    """)

def resource_check(check):
    for i in check:
        if check[i] > resources[i]:
            return False
    return True
        
def money():

    print("Kindly Enter the money:")
    quarters = int(input("Kindly Enter Your Quarters :"))
    dimes = int(input("Kindly Enter Your Dimes :"))
    nickles = int(input("Kindly Enter Your Nickels :"))
    pennies = int(input("Kindly Enter Your Pennies :"))

    money_inserted = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    return money_inserted

def money_check(money_taken, drink_cost):
    if money_taken >= drink_cost:
        change = round(money_taken - drink_cost, 2)
        if change != 0:
            print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True
        
    else:
        print("Sorry you did not insert enough money.")
        print("Money refunded")
        return False
    
def make_coffee(drink_name, stuff_needed):
    for i in stuff_needed:
        resources[i] -= stuff_needed[i]
    print(f"Here is your {drink_name}")

def coffee():
    
    on = True
    
    while on:
        user = input("What Would You Like To Drink ? (espresso/latte/cappuccino) : ")
        if user == "off":
            on = False
        elif user == "report":
            report()
        else:
            drink = MENU[user]
            if resource_check(drink["ingredients"]):
                payment = money()
                if money_check(payment, drink["cost"]):
                    make_coffee(user, drink["ingredients"])
coffee() 