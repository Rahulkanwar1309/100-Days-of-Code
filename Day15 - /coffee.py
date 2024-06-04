from data import MENU, resources



def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print (f"""
    Water : {water}
    Milk : {milk}
    Coffee : {coffee}
    Money : {money}
    """)

def resource_check(check):
    for i in resources:
        if resources[i] < check[i]:
            return False
        else:
            return True
        
def money(quarters, dimes , nickles, pennies):

    print("Kindly Enter the money:")
    q = input("Kindly Enter Your Quarters :")
    d = input("Kindly Enter Your Dimes :")
    n = input("Kindly Enter Your Nickels :")
    p = input("Kindly Enter Your Pennies :")

    money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if money < needed_money:
        return "Sorry that's not enough money. Money refunded."
    else:
        m =  money - needed_nomey
        resources["money"] += m 
        return m

def coffee():
    
    on = True
    
    while on:
        user = input("What Would You Like To Drink ? (espresso/latte/cappuccino) : ")
        if user == "off":
            on = False
        elif user == "report":
            report()
        else:
            check = MENU[user]
            resource_check(check)


coffee()
            


def menu():
    for i in MENU:
        for j in i:
            cost = j+1

    