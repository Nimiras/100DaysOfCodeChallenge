from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

running = True
menu = Menu()
coffee_maker = CoffeeMaker()
moneymachine = MoneyMachine()

while running:
    command = input(f"What would you like? ({menu.get_items()}): ")
    if command == "report":
        coffee_maker.report()
        moneymachine.report()
    elif command == command == "off":
        print("shutting down ...")
        running = False
    elif command == "espresso" or command == "latte" or command == "cappuccino":
        drink = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Wrong input")