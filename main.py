import database

menu_prompt = """ --- Menu ---
1) View Inventory
2) Search Inventory
3) Update Inventory
4) Employee Information
5) Exit.
"""

if __name__ == "__main__":
    # <-------- Main, program starts here.

    database.create_tables()

    while (user_input := input(menu_prompt)) != "7":
        if user_input == "1":
            input(user_input)
        if user_input == "2":
            print(user_input)
        if user_input == "3":
            print(user_input)
        if user_input == "4":
            print(user_input)
        else:
            print("Invalid Input. Try Again")
