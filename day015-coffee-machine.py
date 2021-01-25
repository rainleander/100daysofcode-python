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
    "money": 0,
}

coffee_machine_on = True


def print_report():
    """prints the current available resources of the coffee machine"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def check_resources(coffee_type):
    """checks if the requested coffee ingredients are available"""
    if coffee_type == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return True
        else:
            print("Sorry - there is not enough water.")

    if coffee_type == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            return True
        elif resources["milk"] >= 150 and resources["coffee"] >= 24:
            print("Sorry - there is not enough water.")
        elif resources["water"] >= 200 and resources["coffee"] >= 24:
            print("Sorry - there is not enough milk.")
        else:
            print("Sorry - there is not enough milk nor water.")

    if coffee_type == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            return True
        elif resources["milk"] >= 100 and resources["coffee"] >= 24:
            print("Sorry - there is not enough water.")
        elif coffee_type == "cappuccino" and resources["water"] >= 250 and resources["coffee"] >= 24:
            print("Sorry - there is not enough milk.")
        else:
            print("Sorry - there is not enough milk nor water.")


def process_coins():
    """calculate the amount of money paid based on the coins entered"""
    number_of_quarters = int(input("How many quarters? "))
    number_of_dimes = int(input("How many dimes? "))
    number_of_nickels = int(input("How many nickels? "))
    number_of_pennies = int(input("How many pennies? "))

    quarters = number_of_quarters * 0.25
    dimes = number_of_dimes * 0.10
    nickels = number_of_nickels * 0.05
    pennies = number_of_pennies * 0.01

    total_inserted = quarters + dimes + nickels + pennies
    return total_inserted


def check_transaction(total_coins, coffee_cost):
    """checks that the user has inserted enough money to purchase the drink selected"""
    if coffee_cost == "espresso" and total_coins >= 1.5:
        change = round(total_coins - 1.5, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += 1.5
        return True
    elif coffee_cost == "latte" and total_coins >= 2.5:
        change = round(total_coins - 2.5, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += 2.5
        return True
    elif coffee_cost == "cappuccino" and total_coins >= 3.0:
        change = round(total_coins - 3.0, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += 3.0
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(coffee):
    """if the transaction is successful and there are enough resources to make the drink the user selected,
    the ingredients to make the drink are removed from the coffee machine resources"""
    if coffee == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
        print("Here is your espresso. Enjoy!")
    if coffee == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        print("Here is your latte. Enjoy!")
    if coffee == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        print("Here is your cappuccino. Enjoy!")


while resources["water"] > 50 and coffee_machine_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "report":
        print_report()
    elif prompt == "espresso":
        if check_resources("espresso"):
            print("Please insert coins.")
            if check_transaction(process_coins(), "espresso"):
                make_coffee("espresso")
    elif prompt == "latte":
        if check_resources("latte"):
            print("Please insert coins.")
            if check_transaction(process_coins(), "latte"):
                make_coffee("latte")
    elif prompt == "cappuccino":
        if check_resources("cappuccino"):
            print("Please insert coins.")
            if check_transaction(process_coins(), "cappuccino"):
                make_coffee("cappuccino")
    elif prompt == "off":
        coffee_machine_on = False
    else:
        print(f"Please only input 'espresso', 'latte', or 'cappuccino'.")

print("This Coffee Machine is Out of Order")
