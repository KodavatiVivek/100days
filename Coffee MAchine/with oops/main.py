from menu import Menu, MenuItem
from moneymachine import MoneyMachine
from coffe_maker import CoffeeMaker

menu=Menu()
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()

is_on=True
while is_on:
    print("Please select a choice from below\n")
    drink = input(f"What would you like? ({menu.get_items()})\n")
    if drink == "off":
        is_on = False
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        user_drink=menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(user_drink):
            if money_machine.make_payment(user_drink.cost):
                coffee_maker.make_coffee(user_drink)
