MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

running = True
money = 0
def enougth_ingredients(drink):
    ingredients = MENU[drink]
    if drink == "espresso":
        if ingredients["water"] <= resources["water"] and ingredients["milk"] <= resources["milk"]:
            return True
        else:
            return False
    else:
        if ingredients["water"] <= resources["water"] and ingredients["milk"] <= resources["milk"] and ingredients["coffee"] <= resources["coffee"]:
            return True
        else:
            return False



while running:
    command = input("​What would you like? (espresso/latte/cappuccino):​ ")
    if command == "report":
        water = resources["water"]
        coffee = resources["coffee"]
        milk = resources["milk"]
        print(f"Water: {water}\n"
              f"Coffee: {coffee}\n"
              f"Milk: {milk}\n"
              f"Money: {money}")
    elif command == "off":
        print("shutting down ...")
        running = False
    elif command == "espresso" or command == "latte" or command == "cappuccino":
        if enougth_ingredients(command):

    else:
        print("Wrong input")