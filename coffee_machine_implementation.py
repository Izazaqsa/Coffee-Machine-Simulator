coffee_menu = [
    {
        "name": "Espresso",
        "price": 1.5,
        "ingredient_required": { 
            "water": 20,
            "coffee": 10
        }
    },
    {
        "name": "Latte",
        "price": 2.5,
        "ingredient_required": {
            "water": 10,
            "milk": 20,
            "coffee": 5
        }
    },
    {
        "name": "Cappuccino",
        "price": 3.0,
        "ingredient_required": {
            "water": 10,
            "milk": 10,
            "coffee": 5
        }
    },
    {
        "name": "Mocha",
        "price": 3.5,
        "ingredient_required": {
            "water": 10,
            "milk": 20,
            "coffee": 8,
            "chocolate": 5
        }
    },
    {
        "name": "Flat White",
        "price": 2.8,
        "ingredient_required": {
            "water": 20, 
            "milk": 15, 
            "coffee": 5  
        }
    }
]

resources = {
    'water': 100,
    'milk': 500,
    'coffee': 300,
    'chocolate': 200,
    'profit': 0
}

def display_menu():
    print("\n--- COFFEE MENU ---")
    for coffee in coffee_menu:
        print(f"Name : {coffee['name']:12} ||   Price : ${coffee['price']:.2f}")
    print("-------------------")

def deduction(name):
    for coffee in coffee_menu:
        if name == coffee['name']:
            for ingredient, amount_required in coffee['ingredient_required'].items():
                if ingredient in resources:
                    resources[ingredient] -= amount_required
            # Adding price to profit
            resources['profit'] += coffee['price']

def check_resources(coffee_obj):
    """ the function will check whether we have enough resources to make coffee or not ? """
    for ingredient, amount_required in coffee_obj['ingredient_required'].items():
        if resources.get(ingredient, 0) < amount_required:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def chosing_items(name):
    selected_coffee = None
    for coffee in coffee_menu:
        if coffee['name'].lower() == name.lower():
            selected_coffee = coffee
            break
            
    if not selected_coffee:
        print("Invalid choice. Please select a valid coffee or type 'admin'.")
        return

    # Check resources accurately
    if not check_resources(selected_coffee):
        return

    print('We have the resources to make a coffee for you.')
    tries = 3
    while tries != 0:
        try:
            amount = float(input(f"The price is ${selected_coffee['price']}. Pay the amount: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if amount == selected_coffee['price']:
            print(f"Here is your coffee! Enjoy it.")
            deduction(selected_coffee['name'])
            break 
        elif amount > selected_coffee['price']:
            change = round(amount - selected_coffee['price'], 2)
            print(f"Here is your coffee! Enjoy it and also keep your change: ${change}")
            deduction(selected_coffee['name'])
            break
        else:
            tries -= 1
            if tries != 0:
                print(f"You paid less than required. Please try again. You have {tries} tries left.")
            else:
                print('Sorry, you are out of tries!')

def show_resources():
    print("\n=== RESOURCE REPORT ===")
    for key, value in resources.items():
        unit = "ml" if key in ['water', 'milk'] else "g" if key in ['coffee', 'chocolate'] else "$"
        if key == 'profit':
            print(f"{key.title()}: ${value:.2f}")
        else:
            print(f"{key.title()}: {value}{unit}")
    print("=======================")

def refill_resources():
    print("\n--- REFILL MODE ---")
    for item in resources:
        if item != 'profit':
            try:
                amount = int(input(f"Enter amount of {item} to add: "))
                resources[item] += amount
            except ValueError:
                print("Invalid input, skipping.")
    print("Resources refilled successfully!")

def admin_portal():
    """Separate loop environment for administrators"""
    password = input("Enter Admin Password: ")
    if password != "admin123":  # Secret key to get in
        print("Incorrect password. Access Denied.")
        return True # Keep machine running, back to customer mode

    print("\nWelcome to the Admin Portal!")
    while True:
        print("\nAdmin Options: [1] Report [2] Refill [3] Exit Admin [4] Shut Down Machine")
        admin_choice = input("Select an option: ")
        
        if admin_choice == '1':
            show_resources()
        elif admin_choice == '2':
            refill_resources()
        elif admin_choice == '3':
            print("Exiting Admin Portal...")
            return True # Return to customer loop
        elif admin_choice == '4':
            print("Shutting down the system completely...")
            return False # Break the entire application loop

# --- Main Application Execution ---
machine_on = True 
while machine_on:
    display_menu()
    choice = input("What would you like to have? (Or type 'admin' for management): ").strip().title()
    
    if choice == "Admin":
        # Enter admin portal. If it returns False, the machine shuts down.
        machine_on = admin_portal()
    else:
        chosing_items(choice)
        print (f"Would you like to order again ?")
        while True: 
            ordering_again = input("Type yes for ordering while no for exit : ").lower()
            if ordering_again == "yes":
                choice = input("What would you like to have? (Or type 'admin' for management): ").strip().title()
                chosing_items(choice)

            else : 
                break
        input("\nPress Enter to clear screen for the next customer...")

print("\nThanks for using our automated machine!\nGood bye!")