def turn_off():
    print(f"The machine is turning off..")
    exit(0)

# App Loop
machine_on = True
while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino) ")

    # Detected turn off trigger
    if user_input == "off":
        turn_off()