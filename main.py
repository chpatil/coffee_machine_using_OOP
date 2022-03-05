from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu_object=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

TO_CONTINUE=True
while(TO_CONTINUE):
    MenuItems=menu_object.menu
    MENU_ITEMS=menu_object.get_items().split("/")
    user_input=str(input(f"What would you like? ({menu_object.get_items()}):").lower())
    if user_input in MENU_ITEMS:
        for i in MenuItems:
            if i.name==user_input:
                selected_menu_item=i
                break
            else:
                continue
        if coffee_maker.is_resource_sufficient(selected_menu_item):
            if money_machine.money_received<selected_menu_item.cost:
                money_machine.make_payment(selected_menu_item.cost)
                coffee_maker.make_coffee(selected_menu_item)
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif user_input=="report":
        coffee_maker.report()
        money_machine.report()
    elif user_input=="off":
        TO_CONTINUE=False
    else:
        print("Please enter proper input")