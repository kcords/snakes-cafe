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


def order_item():
    pass


strings = {
    "menu_header": """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""",
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
    "confirmation": "{} order{} of {} has been added to your meal"
}


if __name__ == "__main__":
    open_cafe()

