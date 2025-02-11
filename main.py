from data import resources, MENU

money_balance = 0

def turn_off():
    print(f"The machine is turning off..")
    exit(0)

def print_report():
    print(f"Coffee Machine Resource Report:")
    print(f"- Water: {resources["water"]}ml")
    print(f"- Milk: {resources["milk"]}ml")
    print(f"- Coffee: {resources["coffee"]}g")
    print(f"- Money: ${money_balance}")

# App Loop
machine_on = True
while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino) ")

    # Detected turn off trigger
    if user_input == "off":
        turn_off()
    
    # Detected report trigger
    elif user_input == "report":
        print_report() 