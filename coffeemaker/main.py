from data import MENU, resources

money = 0.00


def print_resources():
    for resource in resources:
        string = f"{resource.title()}:\t {resources[resource]}"
        if resource == "water" or resource == "milk":
            string += "ml"
        else:
            string += "g"
        print(string)
    print(f"Money:\t ${str(round(money, 2))}")


def is_enough_resources_for(menu_item):
    """
    Checks if there is enough resources to make a menu item.
    :param menu_item: the menu item string
    :return: True if there is enough ingredients to make the menu item. Otherwise, returns false.
    """

    def get_ingredients(menu_item):
        return MENU[menu_item]['ingredients']

    ingredients = get_ingredients(menu_item)
    for ingredient in ingredients:
        if resources[str(ingredient)] < ingredients[str(ingredient)]:
            print(f"Not enough for {menu_item}.")
            print(f"Recipe calls for: {ingredients}")
            print(f"Machine has: {resources}\n")
            return False
    return True


def process_coins(menu_item):
    """
    Processes coins and then determines whether user can purchase the menu item. :param menu_item: The menu item
    string :return: A 2-tuple. First element returns True if the user can purchase the menu item. Otherwise,
    false. 2nd Element returns the calculated change of the total coin amount inserted.
    """

    def get_cost(menu_item):
        return MENU[menu_item]["cost"]

    coin_values = [("quarters", 0.25), ("dimes", 0.10), ("nickels", 0.05), ("pennies", 0.01)]

    cost = float(get_cost(menu_item))
    print(f"{menu_item} costs ${cost}")
    print("Please insert coins.")
    total = 0.0

    for coin_type, value in coin_values:
        print(f"total: {total}")
        quantity = int(input(f"How many {coin_type}?: "))
        total += quantity * value
        if total >= cost:
            return True, total - cost
    return False, None


def brew(menu_item):
    """
    Transaction of resources are updated here.
    :param menu_item: The menu item
    :return Profit from transaction of making the coffee
    """
    # Subtract resources
    for ingredient in MENU[menu_item]['ingredients']:
        resources[ingredient] -= MENU[menu_item]['ingredients'][ingredient]

    # Add profit
    return MENU[menu_item]['cost']


on = True
while on:
    request = input("What would you like? (espresso/latte/cappuccino):").lower()
    if request == "off":
        print("Powering off...")
        on = False
    elif request == "report":
        print_resources()
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        if is_enough_resources_for(request):
            enough_coins, change = process_coins(request)
            if enough_coins:
                money += brew(request)
                print(f"Here's your change ${str(round(change, 2))}")
                print(f"And here's your {request}. Enjoy!\n")
            else:
                print("Sorry, that's not enough money. Money refunded.\n")
    else:
        print("Invalid request.")
