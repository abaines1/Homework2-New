import database

menu_prompt = """ --- Menu ---
1. Inventory Menu
2. Employee Menu
3. Order Menu
4. Log Off
"""


# ORDER MENUS SECTION
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

            if orders:
                for orderID, dateOrdered, manufacturerID in orders:
                    print(f"ID: {orderID} ||| Date Ordered: {dateOrdered} ||| ManufacturerID: {manufacturerID}")
            else: 
                print("No orders found. Please add data to the database and retry")
        else:
            print('Error: Please input 4 to go back! ')

# EMPLOYEE MENUS SECTION
def employee_menu():
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
            add_employee()
        elif user_input == "3":
            EmployeeID = input('Please input the EmployeeID of the person you would like to remove: ')
            database.remove_employee(EmployeeID)
        elif user_input == "4":
            pass
        else:
            print('Error: Please input 4 to go back! ')

def add_employee():
    EmpFirstName = input("What is your first name? ")
    EmpLastName = input("What is your last name? ")
    EmployeePhone = input("What is your phone number? ")
    EmployeeUserName = input("What is your user name? ")

    database.add_employee(EmpFirstName, EmpLastName, EmployeePhone, EmployeeUserName)

def listEmployees():
    employees = database.viewEmployees()

    if employees:
        for empID, firstName, lastName, phoneNumber, userName in employees:
            print(f"EmployeeID: {empID} ||| First Name: {firstName} Last Name: {lastName} ||| Phone Number: {phoneNumber} ||| Username: {userName}")
    else:
        print("There are no employees. Add employees to the database before continuing.")


# INVENTORY MENUS SECTION
def inventory_menu():
    menu = """ --- Inventory Menu ---
    1) View Total Inventory (In and Out of Stock)
    2) View In Stock Inventory
    3) View Out of Stock Inventory
    4) Search Inventory
    5) Go Back
    """

    while (user_input := input(menu)) != "5":
        if user_input == "1":
            listTotalInventory()
        elif user_input == "2":
            listInStockInventory()
        elif user_input == "3":
            listOutStockInventory()
        elif user_input == "4":
            search_menu()
        else:
            print('Error: Please input 5 to go back! ')

## VIEW INVENTORY FUNCTIONS
def listTotalInventory():
    inventory = database.viewInventory()

    if inventory:
        for ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID, ManufacturerName, ManufacturerAddress, DayOfDelivery in inventory:
            print(f"Item: {ItemName} ||| Category: {ItemCategory} ||| Item Cost: {ItemCost} ||| Quantity: {ItemQuantity} ||| "
                f"\nManID: {ManufacturerID} ||| ManufacturerName: {ManufacturerName} ||| ManuAddress: {ManufacturerAddress} ||| Day of Delivery: {DayOfDelivery}")
    else:
        print("No inventory found. Please add data to the database and retry.")

def listInStockInventory():
    inStock = database.viewInStock()

    if inStock:
        for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in inStock:
            print(
                f" --- Items In Stock ---- \n"
                f"Item: {ItemName}  ||| Category: {ItemCategory} ||| Cost: {ItemCost}  ||| Quantity: {ItemQuantity} ||| ManufacturerID: {ManufacturerID} \n")
    else:
        print("No items in stock. Please add data to the database and retry.")

def listOutStockInventory():
    OutOfStock = database.viewOutOfStock()

    if OutOfStock:
        for _id, ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID in OutOfStock:
            print(
                f" --- Items In Stock ---- \n"
                f"Item: {ItemName}  ||| Category: {ItemCategory} ||| Cost: {ItemCost}  ||| Quantity: {ItemQuantity} ||| ManufacturerID: {ManufacturerID} \n")
    else:
        print("No items currently out of stock.")

### UPDATE INVENTORY FUNCTIONS
def prompt_add_item_and_manufacturer_delivery():
    ItemName = input('What is the name of the item? ')
    ItemCategory = input('Under what category does this item fall under? ')
    ItemCost = float(input('What does each of the items cost? (per item) '))
    ItemQuantity = int(input('How many of this item are we adding? '))
    ManufacturerName = input('What is the name of the Manufacturer? ')

    database.add_item_with_manufacturer(ItemName, ItemCategory, ItemCost, ItemQuantity,
                                        ManufacturerName)

def prompt_update_inventory():

    update_inv_prompt = """ --- Chose One of the Following ---
    1) Add Items
    2) Remove Items
    3) Update Quantity of Item
    4) Go Back
    """

    while (user_input := input(update_inv_prompt)) != "4":
        if user_input == "1":
            prompt_add_item_and_manufacturer_delivery()
        elif user_input == "2":
            ItemID = input("What is the ItemID you would like to delete? ")
            database.remove_item(ItemID)
        elif user_input == "3":
            _id = input("What is the ID of the item you would like to update? ")
            quantity = input("What is new quantity of the item? ")
            database.updateItemStock(quantity, _id)
        else:
            print('Error: Please input 3 to go back! ')

#### MANUFACTURER MENUS SECTION
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

#### SEARCH INVENTORY SECTION
def search_menu():
    menu = """ --- Search --- 
    1) Search By Name
    2) Search By Category
    3) Go Back
    """
    while (user_input := input(menu)) != "3":
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


# DELIVERY MENUS SECTION
def delivery_menu():
    menu = """ --- Delivery Menu ---
    1) View Deliveries
    2) Update Delivery Employee
    3) Go Back 
    """

    while (user_input := input(menu)) != "3":
        if user_input == "1":
            deliveries = database.viewDeliveries()
            deliveries_size = len(deliveries)
            if deliveries_size > 0:
                for _id, orderID, manID, empId, empFirstName, empLastName, empPhone, empAddress, empUserName in deliveries:
                    print(f"DeliveryID: {_id} ||| OrderID: {orderID} ||| ManufacturerID: {manID} ||| EmployeeID: {empId}"
                        f"EmployeeFirstName: {empFirstName} ||| EmployeeLastName: {empLastName} ||| "
                        f"EmployeePhoneNumber: {empPhone} ||| EmployeeAddress: {empAddress} ||| "
                        f"EmployeeUserName: {empUserName}")
            else:
                print("No deliveries found. Please add data to the database and retry.")
        elif user_input == "2":

            DeliveryID = input("What is the DeliveryID of the Delivery you are Updating")
            EmployeeID = input("What is the EmployeeID of the person who will deliver the order? ")

            database.updateDeliveryDriver(DeliveryID, EmployeeID)
        else:
            print('Error: Please input 3 to go back! ')


# MAIN MENU FUNCTION
if __name__ == "__main__":
    # <-------- Main, program starts here.
    database.create_tables()

    while (user_input := input(menu_prompt)) != "4":
        if user_input == "1":
            inventory_menu()
        elif user_input == "2":
            employee_menu()
        elif user_input == "3":
            order_menu()
        else:
            print("Invalid Input. Try Again")