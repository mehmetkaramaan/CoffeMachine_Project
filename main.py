from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee = CoffeeMaker()
money_machine = MoneyMachine()
on_off = True
while on_off:
    menu_ = Menu()
    response = input(f"What would you like ? {menu_.get_items()} ")
    if response == 'report':
        coffee.report()
    elif response == 'off':
        on_off = 'off'
    else :
        drink = menu_.find_drink(response)
        if coffee.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee.make_coffee(drink)




