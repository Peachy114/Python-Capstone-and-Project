coffee = {
    "espresso": {
        "ingredients" : {
            "water": 50,
            "coffee": 18,
            },
        "price": 15
    },

    "latte": {
        "ingredients" : {
            "water": 200,
            "coffee": 24,
            "milk": 150
            },
        "price": 20
    },

    "cappuccino": {
        "ingredients" : {
            "water": 250,
            "coffee": 24,
            "milk":100
            },
        "price": 30
    },
}

report = {
    "water": 300,
    "milk": 200,
    "coffee":100,
    "income":0
}


# STARTING OF THE PROGRAM
def calculate():
    """calculate the money"""
    while True:
        print('\n')
        print('Please insert coins.')
        try:
            total_money = (
                int(input("How many 5-peso coins: ")) * 5 +
                int(input("How many 10-peso coins: ")) * 10 +
                int(input("How many 20-peso coins: ")) * 20
            )
            print('Calculating wait a sec ~')
            print(f"you've inserted total of {total_money} Pesos.")
            return total_money
        except ValueError:
            print('❌ Please insert valid coin numbers only.')
            continue


def check_resources(order):
    """check the resources"""
    print('\n')
    print('Please wait while checking the resources.')
    for item, amount in coffee[order]['ingredients'].items(): #items() for pair key:value
        if report[item] < amount:
            print(f'Sorry not enough {item}. Money refunded.')
            print("\n")
            return False
    print('Done checking ~')
    return True


def makeCoffee(order, change):
    """make the coffee and returns with your order"""
    print('\n')
    print('Making a coffee brr brr ~')
    for item, amount in coffee[order]["ingredients"].items(): #pair ulit
        report[item] -= amount
    report['income'] += coffee[order]['price']
    print('\n')
    print(f"Here's your order {order}☕.")
    if change:
        print(f"Here is your change {change} pesos.  Enjoy and Thank you! 💕")
        print('\n')
    else: 
        print("Enjoy and Thank you! 💕")
        print('\n')


def check_report():
    """check the current resources"""
    print('Current Resources Available:')
    print(f'Water: {report["water"]}ml')
    print(f'Milk: {report["milk"]}ml')
    print(f'Coffee: {report["coffee"]}g')
    print(f'Income: {report["income"]} Pesos')
    print('\n')

# Start of the programm
while True:
    order = input("💕 Welcome to Chibi Coffee ⭐\n"
    "Espresso --- 15 pesos.\n"
    "Latte ------ 20 pesos.\n"
    "Cappuccino - 30 pesos.\n"
    "Type 'report' to view resources or 'off' to exit.\n"
    "🤩 Order Here: ").lower()

    if order == 'off':
        print('Signing Off. Bye ~ 💕')
        break

    elif order == 'report':
        print('\n')
        check_report()

    elif order in coffee:
        if not check_resources(order): #IF NOT enough resources than loop again from the START.
           continue
        total_money = calculate()
        if total_money >= coffee[order]["price"]: #if customer money is GREATER than cost PRICE.
            makeCoffee(order, total_money - coffee[order]["price"])
        
        else:
            print('\n')
            print('Sorry not enough money. Money refunded 💸')
            continue
    else:
        print('\n')
        print("Please choose a valid option from the menu.")



