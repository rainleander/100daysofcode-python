from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_on = True

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while coffee_machine_on:
    options = menu.get_items()
    coffee_request = input(f"What would you like? ({options}): ")
    if coffee_request == "off":
        coffee_machine_on = False
    elif coffee_request == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_request)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
