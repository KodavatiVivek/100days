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
profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def addresource():
    add_goingon= True
    while add_goingon:
        c = input("Do you need to add the ingredients Yes: y No:n\n").lower()
        if c == "y":
            add_ingredient = input("which ingredient you want to add to machine")
            resources[add_ingredient] += int(input("Enter hou much ml your adding"))
        else:
            add_goingon = False
            print(f"Ingredients are added. Check the inverntory\n")


def resource_sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"Sorry there was no enough {items}ingredients to make coffee")
            print(profit)
            return False
        elif order_ingredients[items] == resources[items]:
            print(f"We are low on supplies\n")
            return True
        return True

def user_money():
    print("please insert the no of coins\n")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Thanks for your payment, Here is your change{change}. Please wait for your coffee")
        global profit
        profit+=drink_cost
        return True
    else:
        print(f"Sorry your money is insufficient for this drink. Money is refunded:{money_received}")
        return False

def make_coffee(drink_name,order_ingredients):
    for items in order_ingredients:
        resources[items]-=order_ingredients[items]
    print(f"Thanks for your patience. Here is your {drink_name} ☕️. Enjoy your time!\n")


def machine():
    is_on = True
    while is_on:
        print("Please select a choice from below\n")
        drink = input("1. For drink :- What would you like? (espresso/latte/cappuccino):\n2.To turnoff the machine enter: off\n3.To see the reportof coffee machine Enter report\n4.To add items to resource type add").lower()
        if drink == "off":
            is_on = False
        elif drink == "report":
            print(f"The remaining water,milk,coffe in coffee machine:-\n")
            print(f"Remaining water:- {resources['water']}\n")
            print(f"Remaining Milk:- {resources['milk']}\n")
            print(f"Remaining coffee:- {resources['coffee']}\n")
            print(f"Our Profit:- {profit}\n")
        elif drink == "add":
            addresource()
        else:
            users_choice = input(
                f"Cost of the selected drink {drink}:-$ {MENU[drink]['cost']}.\n Do You wish to continue Yes: Y, No: n\n").lower()
            if users_choice == "y":
                drinks = MENU[drink]
                if resource_sufficient(drinks["ingredients"]):
                    user_amount = user_money()
                    if transaction_successful(user_amount, drinks["cost"]):
                        make_coffee(drink, drinks["ingredients"])
                    else:
                        nexttime = input(
                            "Do you want try again. Yes or No\n. Hope this time you have calculated amount correctly to enjoy the coffee.").lower()
                        if nexttime == "yes":
                            machine()
            else:
                print("Please move for the next person\n")
                machine()



machine()