from functions import turn_off, print_report, receive_order

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