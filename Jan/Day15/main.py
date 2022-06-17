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

COINS = {
    "quaters":  0.25,
    "dimes":    0.1,
    "nickles":  0.05,
    "pennies":  0.01,
}

running = True
global money
money = 0
def enougth_ingredients(drink):
    """Returns True when there are enough ingreedients in the machine to dispend a drink and False if not."""
    ingredients = MENU[drink]["ingredients"]
    if drink == "espresso":
        if ingredients["water"] <= resources["water"] and ingredients["coffee"] <= resources["coffee"]:
            return True
        else:
            if ingredients["water"] > resources["water"]:
                print("There is not enough water in the machine")
            if ingredients["coffee"] > resources["coffee"]:
                print("There is not enough coffee in the machine")
            return False
    else:
        if ingredients["water"] <= resources["water"] and ingredients["milk"] <= resources["milk"] and ingredients["coffee"] <= resources["coffee"]:
            return True
        else:
            if ingredients["water"] > resources["water"]:
                print("There is not enough water in the machine")
            if ingredients["milk"] > resources["milk"]:
                print("There is not enough milk in the machine")
            if ingredients["coffee"] > resources["coffee"]:
                print("There is not enough coffee in the machine")
            return False

def process_coin():
    """Asks the user how many coins they're want to insert and returns the sum of all the inserted coins"""
    print("How many coins do you want to insert?")
    quaters = int(input("Quaters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    return quaters * COINS["quaters"] + dimes * COINS["dimes"] + nickles * COINS["nickles"] + pennies * COINS["pennies"]

def transaction(cost, sum, drink):
    """
    Checks the cost and the amount of money that was put in the function to determin if the user gave the machine enough money and if so
    removes the ingredients or outputs the change
    """
    if sum < cost:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif sum >= cost:
        global money
        money += cost
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        if drink != "espresso":
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        print(f"You inserted {sum}$\n"
              f"The drink costs {cost}$")
        if sum > cost:
            print(f"Here is {str(sum - cost)} $ in change!")
        print("Enjoy your drink")


while running:
    command = input("What would you like? (espresso/latte/cappuccino): ")
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
            sum = process_coin()
            transaction(MENU[command]["cost"], sum, command)

    else:
        print("Wrong input")