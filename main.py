from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while coffee_machine.is_powered_on:
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino) ").lower()

    # Detected turn off trigger
    if user_input == "off":
        coffee_machine.power_off()
        exit(0)

    # Detected report trigger
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()

    # Detected a valid drink order
    elif user_input in ("espresso", "latte", "cappuccino"):
        drink = menu.find_drink(user_input)

        payment_accepted = money_machine.make_payment(drink.cost)
        
        if payment_accepted:
            coffee_machine.make_coffee(drink)

    # Option not recognized
    else:
        print(f"Option not recognized. Please enter a valid option.")