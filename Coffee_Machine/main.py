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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Prompt user what would would like? (espresso/latte/cappuccino):
# prompt = input("What would you like? (espresso/latte/cappuccino)").lower()


# TODO: 2. Turn off coffee machine by entering off to the prompt

# if prompt == "off":
#   power_machine = False


# TODO: 3. Print report

# if prompt == "report":
#   print(f"Water: {resources['water']}")
#   print(f"Milk: {resources['milk']}")
#   print(f"Coffee: {resources['coffee']}")


# TODO: 4. check resources sufficient
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough of {item}.")
            return False
    return True




# TODO: 5. Process coins

def check_coins():
    print("Insert coins.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
# TODO: 6. Check transaction successful?
def transaction_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough money for drink. Your money is refunded.")
        return False
# TODO: 7. Make Coffee
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")
power_machine = True

while power_machine:
   prompt = input("What would you like? (espresso/latte/cappuccino)").lower()
   if prompt == "off":
       power_machine = False
   elif prompt == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
   else:
       drink = MENU[prompt]
       if check_resources(drink["ingredients"]):
                   payment = check_coins()
                   if transaction_success(payment, drink["cost"]):
                       make_coffee(prompt, drink["ingredients"])

