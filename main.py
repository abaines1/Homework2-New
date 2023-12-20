import database

menu_prompt = """ --- Menu ---
1) View Inventory
2) Search Inventory
3) Update Inventory
4) Employee Information
5) Manufacture Information
6) Delivery Information
7) Exit.

"""


def prompt_add_item():
    ItemName = input('What is the name of the item? ')
    ItemCategory = input('Under what category does this item fall under? ')
    ItemCost = int(input('What does each of the items cost? (per item) '))
    ItemQuantity = int(input('How many of this item are we adding? '))
    ManufacturerID = int(input('What is the ManufacturerID for the item? '))

    database.add_item(ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID)


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
    3) Update Quantity of Item
    4) Go Back
    """

    while (user_input := input(update_inv_prompt)) != "4":
        if user_input == "1":
            prompt_add_item()
        elif user_input == "2":
            ItemID = input("What is the ItemID you would like to delete? ")
            database.remove_item(ItemID)
        elif user_input == "3":
            _id = input("What is the ID of the item you would like to update? ")
            quantity = input("What is new quantity of the item? ")
            database.updateItemStock(quantity, _id)
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


def inventory_menu():
    menu = """ --- Inventory Menu ---
    1) View Total Inventory (In and Out of Stock)
    2) View In Stock Inventory
    3) View Out of Stock Inventory 
    4) Go Back
    """

    while (user_input := input(menu)) != "4":
        if user_input == "1":
            listTotalInventory()
        elif user_input == "2":
            listInStockInventory()
        elif user_input == "3":
            listOutStockInventory()
        else:
            print('Error: Please input 4 to go back! ')


def manufacturer_menu():
    menu = """ --- Manufacture Information Menu ---
    1) Add Manufacturer
    2) Remove Manufacturer
    3) View Manufacturers 
    4) Go Back
    
    """

    while (user_input := input(menu)) != "4":
        if user_input == "1":
            add_manufacturer_menu()
        elif user_input == "2":
            removeId = input("What is the ID of the Manufacturer you would like to remove?")
            database.removeManufacturer(removeId)
        elif user_input == "3":
            listManufacturers()
        else:
            print('Error: Please input 4 to go back! ')


def add_manufacturer_menu():
    ManufacturerName = input("What is the name of the Manufacturer? ")
    ManufacturerAddress = input("What is the address for the Manufacturer? ")
    DayOfDelivery = input("What is the day this Manufacturer delivers? ")

    database.add_manufacture(ManufacturerName, ManufacturerAddress, DayOfDelivery)


def search_menu():
    menu = """ --- Search --- 
    1) Search By Name
    2) Search By Category
    3) Go Back
    """
    while (user_input := input(menu)) != "4":
        if user_input == "1":
            searchName = database.searchByName(input('What is the name of the item you are searching for? '))

            for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in searchName:
                print(f" ID: {_id} ||| Name: {ItemName} ||| Category: {ItemCategory} ||| "
                      f"Cost: {ItemCost} ||| Quantity: {ItemQuantity} ||| ManuID: {ManufacturerID} ")

        elif user_input == "2":
            searchCategory = database.searchByCategory(input('What is the category of item you are looking for? '))

            for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in searchCategory:
                print(f" ID: {_id} ||| Name: {ItemName} ||| Category: {ItemCategory} ||| "
                      f"Cost: {ItemCost} ||| Quantity: {ItemQuantity} ||| ManuID: {ManufacturerID} ")

        elif user_input == "3":
            pass
        else:
            print('Error: Please input 4 to go back! ')


def listManufacturers():
    manufacturers = database.viewManufacturers()

    for _id, ManufacturerName, ManufacturerAddress, DayOfDelivery in manufacturers:
        print(f" --- Manufacturers --- "
              f"ID: {_id} ||| Name: {ManufacturerName} ||| Address: {ManufacturerAddress} ||| Day of Deliveries: {DayOfDelivery}")


def listTotalInventory():
    inventory = database.viewInventory()

    for ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID, ManufacturerName, ManufacturerAddress, DayOfDelivery in inventory:
        print(f"Item: {ItemName} ||| Category: {ItemCategory} ||| {ItemCost} Quantity: {ItemQuantity} "
              f"ManID: {ManufacturerID} ||| ManufacturerName: {ManufacturerName} ||| ManuAddress: {ManufacturerAddress} ||| Day of Delivery: {DayOfDelivery}")


def listInStockInventory():
    inStock = database.viewInStock()

    for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in inStock:
        print(
            f" --- Items In Stock ---- \n"
            f"Item: {ItemName}  ||| Category: {ItemCategory} ||| Cost: {ItemCost}  ||| Quantity: {ItemQuantity} ||| ManufacturerID: {ManufacturerID} \n")


def listOutStockInventory():
    OutOfStock = database.viewOutOfStock()

    for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in OutOfStock:
        print(
            f" --- Items In Stock ---- \n"
            f"Item: {ItemName}  ||| Category: {ItemCategory} ||| Cost: {ItemCost}  ||| Quantity: {ItemQuantity} ||| ManufacturerID: {ManufacturerID} \n")


if __name__ == "__main__":
    # <-------- Main, program starts here.
    database.create_tables()

    while (user_input := input(menu_prompt)) != "7":
        if user_input == "1":
            inventory_menu()
        elif user_input == "2":
            search_menu()
        elif user_input == "3":
            prompt_update_inventory()
        elif user_input == "4":
            prompt_employee_menu()
        elif user_input == "5":
            manufacturer_menu()
        else:
            print("Invalid Input. Try Again")
