import database

menu_prompt = """ --- Menu ---
1) View Inventory
2) Search Inventory
3) Update Inventory
4) Employee Information
5) Manufacture Information
6) Delivery Information
7) Order Menu 
8) Exit.

"""


def prompt_add_item_and_manufacturer_delivery():
    ItemName = input('What is the name of the item? ')
    ItemCategory = input('Under what category does this item fall under? ')
    ItemCost = float(input('What does each of the items cost? (per item $xx.xx) '))
    ItemQuantity = int(input('How many of this item are we adding? '))
    ManufacturerName = input('What is the name of the Manufacturer? ')

    database.add_item_with_manufacturer(ItemName, ItemCategory, ItemCost, ItemQuantity,
                                        ManufacturerName)

# 1) When creating orders, it says after inputing ManuID (***why manu id isnt this the company's employee?***)
# 2) If there are no orders, return (currently no orders)
def order_menu():
    menu = """ --- Order Menu --- \n
    1) Create Order
    2) Delete Order
    3) View Orders
    4) Go Back
    """

    while (user_input := input(menu)) != "4":
        if user_input == "1":
            DateOrdered = input("Input the date the order was placed: (mm-dd-yy)")
            ManufacturerID = input("What is the manufacturer id? ")

            database.create_order_and_delivery(DateOrdered, ManufacturerID)

        elif user_input == "2":
            removeID = input("What is the ID of the Order you are trying to delete?")
            database.remove_order(removeID)
        elif user_input == "3":
            orders = database.viewOrders()

            for orderID, dateOrdered, manufacturerID in orders:
                print(f"ID: {orderID} ||| Date Ordered: {dateOrdered} ||| ManufacturerID: {manufacturerID}")
        else:
            print('Error: Please input 4 to go back! ')


def add_employee_menu():
    EmpFirstName = input("What is your first name? ")
    EmpLastName = input("What is your last name? ")
    EmployeePhone = input("What is your phone number? ")
    EmployeeUserName = input("What is your user name? ")

    database.add_employee(EmpFirstName, EmpLastName, EmployeePhone, EmployeeUserName)


# def prompt_update_inventory():
#     update_inv_prompt = """ --- Chose One of the Following ---
#     1) Add Items
#     2) Remove Items
#     3) Update Quantity of Item
#     4) Go Back
#     """

#     while (user_input := input(update_inv_prompt)) != "4":
#         if user_input == "1":
#             prompt_add_item_and_manufacturer_delivery()
#         elif user_input == "2":
#             ItemID = input("What is the ItemID you would like to delete? ")
#             database.remove_item(ItemID)
#         elif user_input == "3":
#             _id = input("What is the ID of the item you would like to update? ")
#             quantity = input("What is new quantity of the item? ")
#             database.updateItemStock(quantity, _id)
#         else:
#             print('Error: Please input 3 to go back! ')

# 1) If there are no employees, return currently no employees
def prompt_employee_menu():
    employee_menu = """ --- Employee Menu ---
    1) View Employees
    2) Add Employee
    3) Remove Employee
    4) Go Back
    """

    while (user_input := input(employee_menu)) != "4":
        if user_input == "1":
            listEmployees()
        elif user_input == "2":
            add_employee_menu()
        elif user_input == "3":
            EmployeeID = input('Please input the EmployeeID of the person you would like to remove: ')
            database.remove_employee(EmployeeID)
        elif user_input == "4":
            pass
        else:
            print('Error: Please input 4 to go back! ')


def inventory_menu():
    main_menu = """ --- Inventory Menu ---
    1) View Inventory
    2) Update Inventory
    3) Search Inventory
    4) Go Back
    """

    view_inv_menu = """ --- View Inventory ---
    1) Total Inventory
    2) In Stock Inventory
    3) Out of Stock Inventory 
    4) Go Back
    """

    update_inv_menu = """ --- Update Inventory ---
    1) Add a New Item
    2) Remove an Item
    3) Update Quantity of an Item
    4) Go Back
    """

    # while (user_input := input(menu)) != "4":
    #     if user_input == "1":
    #         listTotalInventory()
    #     elif user_input == "2":
    #         listInStockInventory()
    #     elif user_input == "3":
    #         listOutStockInventory()
    #     else:
    #         print('Error: Please input 4 to go back! ')

    while (user_input := input(main_menu)) != "4":
        # View Inventory
        # 1) Price Not in the Print() when viewing inventory && seperator between Price, Quantity, 
        # and ManID in View Inventory *** COMPLETED 6/16 at 220 ***
        # ***************************************************************************************** #
        if user_input == "1":

            while (user_input2 := input(view_inv_menu)) != "4":
                # Total Inventory
                if user_input2 == "1":
                    listTotalInventory()
                # In Stock Inventory
                elif user_input2 == "2":
                    listInStockInventory()
                # Out of Stock
                elif user_input2 == "3":
                    listOutStockInventory()
                # Go Back
                elif user_input2 == "4":
                    pass
                else:
                    print("Error: Invalid input. Please input 4 to go back.")

        # Update Inventory
        elif user_input == "2":

            while (user_input3 := input(update_inv_menu)) != "4":

                # 1) When adding an item to inventory, if the price is 13.99, the database can only accept an int (change to float) *** COMPLETED 6/16 230pm ***
                if user_input3 == "1":

                    prompt_add_item_and_manufacturer_delivery()

                elif user_input3 == "2":
                    # 1) "Item Deleted" if successful alert [*** COMPLETE 6/16 430PM ***]
                    # 2) Print Inventory Before deleting an item  [*** COMPLETE 6/16 430PM ***]

                    listTotalInventory()
                    print("\n")

                    ItemID = input("What is the ItemID you would like to delete? ")
                    database.remove_item(ItemID)

                elif user_input3 == "3":

                    # 1) Update Quantity of an Item *** COMPLETED 6/19 1137AM ***
                    # - When asking about ID of what you are updating, after selecting, print the items details to insure the item selected is the correct option
                    # - If no item exists, alert the user (inventory is empty or item id selected does not exist)
                    # - When changing quantity of items in stock, maybe when prompting show how many items are currently in stock in the system? 
                    # - Maybe print something like {ItemName} now has Quantity of {Quantity}


                    listTotalInventory()
                    print("\n")
                    
                    # try:
                    #     _id = input("What is the ID of the item you would like to update? ")
                    #     quantity = input("What is new quantity of the item? ")
                    #     database.updateItemStock(quantity, _id)
                    # except: 
                    #     print("That ID for the item was not found. Try again.")

                    _id = input("What is the ID of the item you would like to update? ")

                    item = database.doesItemExist(_id)

                    if item:
                        quantity = input("What is the new quantity of the item? ")
                        database.updateItemStock(quantity, _id)

                        print(f"The item {item[1]} has an updated quantity of {quantity}")
                    else:
                        print(f"Error. We couldn't find an item with the ID {_id}. Try again.")
                # --- stopped here 6/19 1145am --- 
                elif user_input3 == "4":
                    pass 
                else:
                    print('Error: Please input 3 to go back! ')

        # Search Inventory
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Error: Invalid Input. Input 4 to go back to the main menu.")

# 1) Seperator between ManAddress and DayOfDelivery in View Manufacturers *** COMPLETED 6/16 AT 1254***
def manufacturer_menu():
    menu = """ --- Manufacture Information Menu ---
    1) View Manufacturers
    2) Go Back
   """
    while (user_input := input(menu)) != "2":
        if user_input == "1":
            manufacturers = database.viewManufacturers()

            for manuID, manuName, manuAddress, manuDayDelivery in manufacturers:
                print(
                    f"ManufacturerID: {manuID} ||| ManufacturerName: {manuName} ||| ManufacturerAddress: {manuAddress} ||| Day of Delivery: {manuDayDelivery}")
        elif user_input == "2":
            pass
        else:
            print("Error")

# 1) when going back in Search menu it needs to be go back on 3 not 4
def search_menu():
    menu = """ --- Search --- 
    1) Search By Name
    2) Search By Category
    3) Go Back
    """
    while (user_input := input(menu)) != "4":
        if user_input == "1":
            searchName = database.searchByName(input('What is the name of the item you are searching for? '))
            print(searchName)

            if searchName:
                for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in searchName:
                    if ItemQuantity != 0:
                        print(f" ID: {_id} ||| Name: {ItemName} ||| Category: {ItemCategory} ||| "
                              f"Cost: {ItemCost} ||| Quantity: {ItemQuantity} ||| ManuID: {ManufacturerID} ")
                    else:
                        getDeliveryDay = database.getNextDeliveryDate(ManufacturerID)
                        print(f"Oh no! It looks like Item {ItemName} is Out of Stock. \n"
                              f"Looks like {ItemName} will be delivered to us on {getDeliveryDay[0]}")
            elif not searchName:
                print("Oh no! It looks like we couldn't find that item. Try searching something else!")
            else:
                print("Error! Try again")

        elif user_input == "2":
            searchCategory = database.searchByCategory(input('What is the category of item you are looking for? '))

            if searchCategory:
                for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in searchCategory:
                    print(f" ID: {_id} ||| Name: {ItemName} ||| Category: {ItemCategory} ||| "
                          f"Cost: {ItemCost} ||| Quantity: {ItemQuantity} ||| ManuID: {ManufacturerID} ")
            elif not searchCategory:
                print("Oh no! It looks like we couldn't find that item category. Try searching something else!")
            else:
                print("Error! Try again!")

        elif user_input == "3":
            pass
        else:
            print('Error: Please input 4 to go back! ')

# 1) If there are no deliveries, return (Currently no deliveries)
def delivery_menu():
    menu = """ --- Delivery Menu ---
    1) View Deliveries
    2) Update Delivery Employee
    3) Go Back 
    """

    while (user_input := input(menu)) != "3":
        if user_input == "1":
            deliveries = database.viewDeliveries()
            for _id, orderID, manID, empId, empFirstName, empLastName, empPhone, empAddress, empUserName in deliveries:
                print(f"DeliveryID: {_id} ||| OrderID: {orderID} ||| ManufacturerID: {manID} ||| EmployeeID: {empId}"
                      f"EmployeeFirstName: {empFirstName} ||| EmployeeLastName: {empLastName} ||| "
                      f"EmployeePhoneNumber: {empPhone} ||| EmployeeAddress: {empAddress} ||| "
                      f"EmployeeUserName: {empUserName}")
        elif user_input == "2":

            DeliveryID = input("What is the DeliveryID of the Delivery you are Updating")
            EmployeeID = input("What is the EmployeeID of the person who will deliver the order? ")

            database.updateDeliveryDriver(DeliveryID, EmployeeID)
        else:
            print('Error: Please input 3 to go back! ')


def listManufacturers():
    manufacturers = database.viewManufacturers()

    for _id, ManufacturerName, ManufacturerAddress, DayOfDelivery in manufacturers:
        print(f" --- Manufacturers --- "
              f"ID: {_id} ||| Name: {ManufacturerName} ||| Address: {ManufacturerAddress} ||| Day of Deliveries: {DayOfDelivery}")

# 1) Add ItemID to print statement
def listTotalInventory():
    inventory = database.viewInventory()

    if inventory:
        for ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID, ManufacturerName, ManufacturerAddress, DayOfDelivery in inventory:
            print("\n")
            print(f"Item: {ItemName} ||| Category: {ItemCategory} ||| Item Cost: ${ItemCost} ||| Quantity: {ItemQuantity} ||| "
                f"ManID: {ManufacturerID} ||| ManufacturerName: {ManufacturerName} ||| ManuAddress: {ManufacturerAddress} ||| Day of Delivery: {DayOfDelivery}")
            print("\n", "************************************************************************************************")
    else:
        print("No inventory found. Please add data to the database and retry.")

def listInStockInventory():
    inStock = database.viewInStock()

    for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in inStock:
        print(
            f" --- Items In Stock ---- \n"
            f"Item: {ItemName}  ||| Category: {ItemCategory} ||| Cost: ${ItemCost}  ||| Quantity: {ItemQuantity} ||| ManufacturerID: {ManufacturerID} \n")


def listOutStockInventory():
    OutOfStock = database.viewOutOfStock()

    for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in OutOfStock:
        print(
            f" --- Items In Stock ---- \n"
            f"Item: {ItemName}  ||| Category: {ItemCategory} ||| Cost: ${ItemCost}  ||| Quantity: {ItemQuantity} ||| ManufacturerID: {ManufacturerID} \n")

def listEmployees():
    employees = database.viewEmployees()

    if employees:
        for empID, firstName, lastName, phoneNumber, userName in employees:
            print(f"EmployeeID: {empID} ||| First Name: {firstName} Last Name: {lastName} ||| Phone Number: {phoneNumber} ||| Username: {userName}")
    else:
        print("There are no employees. Add employees to the database before continuing.")

if __name__ == "__main__":
    # <-------- Main, program starts here.
    database.create_tables()

    while (user_input := input(menu_prompt)) != "8":
        if user_input == "1":
            inventory_menu()
        elif user_input == "2":
            search_menu()
        elif user_input == "3":
            pass
        elif user_input == "4":
            prompt_employee_menu()
        elif user_input == "5":
            manufacturer_menu()
        elif user_input == "6":
            delivery_menu()
        elif user_input == "7":
            order_menu()
        else:
            print("Invalid Input. Try Again")
