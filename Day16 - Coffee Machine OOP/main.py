from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

on = True

while on:

    options = menu.get_items()
    user = input(f"What Would You Like To Drink ? ({options}) : ")
    if user == "report":
        coffee_maker.report()
        money_machine.report()
    elif user == "off":
        on = False
    else:
        drink = menu.find_drink(user)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
    
    


