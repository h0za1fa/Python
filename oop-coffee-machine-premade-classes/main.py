from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on == True:
    print(f'What would you like to order {menu.get_items()[:-1]}')
    order=input('Place your order: ')
    order_available=menu.find_drink(order)
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
        
    elif not order_available: 
        order_available
    else:
        print(f'That would be ${order_available.cost} ')
        if coffee_maker.is_resource_sufficient(order_available) and money_machine.make_payment(order_available.cost):
           coffee_maker.make_coffee(order_available)
        
        