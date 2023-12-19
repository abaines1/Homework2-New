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


def add_employee_menu():
    EmpFirstName = input("What is your first name? ")
    EmpLastName = input("What is your last name? ")
    EmployeePhone = input("What is your phone number? ")
    EmployeeUserName = input("What is your user name? ")

    database.add_employee(EmpFirstName, EmpLastName, EmployeePhone, EmployeeUserName)


def prompt_update_inventory():
    update_inv_prompt = """ --- Chose One of the Following ---
    1) Add Items
    2) Remove Items
    3) Go back
    """

    while (user_input := input(update_inv_prompt)) != "3":
        if user_input == "1":
            prompt_add_item()
        elif user_input == "2":
            ItemID = input("What is the ItemID you would like to delete? ")
            database.remove_item(ItemID)
        elif user_input == "3":
            pass
        else:
            print('Error: Please input 3 to go back! ')


def prompt_employee_menu():
    employee_menu = """ --- Employee Menu ---
    1) Add Employee
    2) Remove Employee
    3) Go Back
    """

    while (user_input := input(employee_menu)) != "3":
        if user_input == "1":
            add_employee_menu()
        elif user_input == "2":
            EmployeeID = input('Please input the EmployeeID of the person you would like to remove: ')
            database.remove_employee(EmployeeID)
        elif user_input == "3":
            pass
        else:
            print('Error: Please input 3 to go back! ')


if __name__ == "__main__":
    # <-------- Main, program starts here.
    database.create_tables()

    while (user_input := input(menu_prompt)) != "7":
        if user_input == "1":
            input(user_input)
        elif user_input == "2":
            print(user_input)
        elif user_input == "3":
            prompt_update_inventory()
        elif user_input == "4":
            prompt_employee_menu()
        else:
            print("Invalid Input. Try Again")
