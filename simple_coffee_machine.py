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

money_in_machine = 0

drink_options = ["espresso", "latte", "cappuccino"]

finished = False

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${money_in_machine}")

def check_resources_sufficient(the_option):
    for key in MENU[the_option]["ingredients"]:
        if key in resources:
            if resources[key] < MENU[the_option]["ingredients"][key]:
                print(f"Sorry there is not enough {key}.")
                return False
    return True

def update_resources(the_option):
    for key in MENU[the_option]["ingredients"]:
        if key in resources:
            resources[key] -= MENU[the_option]["ingredients"][key]


def transaction_successful(the_option, the_quarters, the_dimes, the_nickels, the_pennies):
    global money_in_machine
    paid = (0.25 * the_quarters) + (0.10 * the_dimes) + (0.05 * the_nickels) + (0.01 * the_pennies)
    cost = MENU[the_option]["cost"]
    if paid >= cost:
        change = round(paid - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        money_in_machine += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

while not finished:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == "report":
        report()
        continue
    elif option == "off":
        print("Have a good day!")
        finished = True
    elif option not in drink_options:
        print("Sorry, we do not have that drink.")
        continue
    else:
        if check_resources_sufficient(option):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            if transaction_successful(option, quarters, dimes, nickels, pennies):
                update_resources(option)
                print(f"Here is your {option}. ☕ Enjoy!")

        else:
            continue
