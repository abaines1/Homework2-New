import database

menu_prompt = """ --- Menu ---
1) View Inventory
2) Search Inventory
3) Update Inventory
4) Employee Information
5) Exit.
"""


def prompt_add_item():
    ItemName = input('What is the name of the item? ')
    ItemCategory = input('Under what category does this item fall under? ')
    ItemCost = int(input('What does each of the items cost? (per item) '))
    ItemQuantity = int(input('How many of this item are we adding? '))

    database.add_item(ItemName, ItemCategory, ItemCost, ItemQuantity)


if __name__ == "__main__":
    # <-------- Main, program starts here.

    database.create_tables()

    while (user_input := input(menu_prompt)) != "7":
        if user_input == "1":
            input(user_input)
        elif user_input == "2":
            print(user_input)
        elif user_input == "3":
            prompt_add_item()
        elif user_input == "4":
            print(user_input)
        else:
            print("Invalid Input. Try Again")
