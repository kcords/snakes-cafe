def open_cafe():
    offer_menu()
    prompt_diner()


def offer_menu():
    print(strings["menu_header"])
    print_menu_items()
    print(strings["order_prompt"])



def print_menu_items():
    for category, category_items in strings["menu_items"].items():
        print()
        print(category)
        print("-" * len(category))
        [print(menu_item) for menu_item in category_items]


def prompt_diner():
    order_active = True
    while order_active:
        ordered = input("> ")
        if ordered == 'quit':
            order_active = False
            break
        order_item(ordered)


def order_item(menu_item):
    menu_item = validate_menu_item(menu_item)
    if menu_item is None:
        print(strings["invalid_item"])
        return
    count = 1 if menu_item not in ordered_items else ordered_items[menu_item] + 1
    ordered_items[menu_item] = count
    print()
    print(strings["confirmation"].format(count, "s" if count > 1 else "", menu_item))
    print()


ordered_items = {}

def validate_menu_item(menu_item):
    menu_item = menu_item.title()
    for category, items in strings["menu_items"].items():
        if menu_item in items:
            return menu_item


strings = {
    "menu_header": """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""",
    "order_prompt": """
***********************************
** What would you like to order? **
***********************************
""",
    "menu_items": {
        "Appetizers": ("Wings", "Cookies", "Spring Rolls"),
        "Entrees": ("Salmon", "Steak", "Meat Tornado", "A Literal Garden"),
        "Desserts": ("Ice Cream", "Cake", "Pie"),
        "Drinks": ("Coffee", "Tea", "Unicorn Tears")
    },
    "confirmation": "** {} order{} of {} has been added to your meal **",
    "invalid_item": """
Not a valid menu item, please order something else.
"""
}


if __name__ == "__main__":
    open_cafe()

