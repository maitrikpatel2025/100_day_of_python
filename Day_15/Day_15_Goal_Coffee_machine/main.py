from menu import MENU, resources
import math
total_water = resources['water']
total_milk = resources['milk']
total_coffee = resources['coffee']
total_money = resources['money']

def cost_for_coffee(order_details):
    global end_Order
    global total_money
    quarters = int(input("how many quarters? :"))
    dimes = int(input("how many dimes? :"))
    nickles = int(input("how many nickles? :"))
    pennies = int(input("how many pennies? :"))
    amount = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    if MENU[order_details]['cost'] > amount:
        print("sorry that's not enough money. money refund")
    elif MENU[order_details]['cost'] < amount:
        change = amount - MENU[order_details]['cost']
        total_money = MENU[order_details]['cost']
        print(f"Here is ${float(change)} change")
        print(f"Here is your {order_details} Enjoy")


def left_over(order_details,main_ing,ing):
    if main_ing < MENU[order_details]['ingredients'][ing]:
        return f"sorry there is not enough {ing}"



def amount_left(order_details,ing):
    global total_water, total_milk, total_coffee, total_money
    if ing == "water":
        left_over(order_details, total_water, ing)
        return total_water - MENU[order_details]['ingredients'][ing]
    elif ing == "milk":
        left_over(order_details,total_milk, ing)
        return total_milk - MENU[order_details]['ingredients'][ing]
    elif ing == "coffee":
        left_over(order_details,total_coffee, ing)
        return total_coffee - MENU[order_details]['ingredients'][ing]
    else:
        return MENU[order_details]['ingredients'][ing]

def make_order(order_details):
    global total_water, total_milk, total_coffee, total_money

    water_left = amount_left(order_details, "water")
    milk_left = amount_left(order_details, "milk")
    coffee_left = amount_left(order_details, "coffee")

    total_water = water_left
    total_milk = milk_left
    total_coffee = coffee_left



def coffee_maker(od):
    global total_water, total_milk, total_coffee, total_money
    if od.lower() == 'report':
        print(f"""
        water: {total_water}ml 
        milk: {total_milk}ml 
        coffee:{total_coffee}g 
        money: ${total_money}
        """)
    elif od.lower() == "espresso":
        make_order("espresso")
        cost_for_coffee("espresso")
    elif od.lower() == "latte":
        make_order("latte")
        cost_for_coffee("latte")
    elif od.lower() == "cappuccino":
        make_order("cappuccino")
    else:
        print(f"""
               water: {total_water}ml 
               milk: {total_milk}ml 
               coffee:{total_coffee}g 
               money: ${total_money}
               """)

end_Order = False

while not end_Order:
    order = input("what would you like? (espresso/latte/cappuccino) : ")
    coffee_maker(order)