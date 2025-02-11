from data import resources, MENU

money_balance = 0

def turn_off():
    print(f"The machine is turning off..")
    exit(0)

def print_report():
    print(f"Coffee Machine Report:")
    print(f"- Water: {resources["water"]}ml")
    print(f"- Milk: {resources["milk"]}ml")
    print(f"- Coffee: {resources["coffee"]}g")
    print(f"- Money: ${money_balance:.2f}")

def receive_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_coins = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
    return total_coins

def receive_order(drink):
    # Dealing with the payment
    drink_cost = MENU[drink]["cost"]
    print(f"The {drink} costs ${drink_cost:.2f}. Please insert coins.")
    user_payment = receive_coins()
    
    if user_payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return
    
    elif user_payment > drink_cost:
        user_refund = user_payment - drink_cost
        print(f"Here is ${user_refund:.2f} dollars in change.")

    global money_balance
    money_balance += drink_cost

# App Loop
machine_on = True
while machine_on:
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino) ").lower()

    # Detected turn off trigger
    if user_input == "off":
        turn_off()
    
    # Detected report trigger
    elif user_input == "report":
        print_report() 

    # Detected a valid drink order
    elif user_input in ("espresso", "latte", "cappuccino"):
        receive_order(user_input)

    # Option not recognized
    else:
        print(f"Option not recognized. Please enter a valid option.")