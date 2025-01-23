import _sqlite3

CREATE_INVENTORY = ''' CREATE TABLE IF NOT EXISTS Inventory(
ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
ItemName TEXT, 
ItemCategory TEXT,
ItemCost FLOAT,
ItemQuantity INTEGER, 
ManufacturerID INTEGER,
FOREIGN KEY (ManufacturerID) REFERENCES Manufacturer(ManufacturerID)
);

'''
CREATE_MANUFACTURER = ''' CREATE TABLE IF NOT EXISTS Manufacturer(
ManufacturerID INTEGER PRIMARY KEY AUTOINCREMENT,
ManufacturerName TEXT,
ManufacturerAddress TEXT,
DayOfDelivery TEXT
);
'''

CREATE_DELIVERY_TABLE = ''' CREATE TABLE IF NOT EXISTS Delivery(
DeliveryID INTEGER PRIMARY KEY AUTOINCREMENT,
OrderID INTEGER,
EmployeeID INTEGER,
ManufacturerID INTEGER,
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
FOREIGN KEY (ManufacturerID) REFERENCES Manufacturer(ManufacturerID)
);
'''

CREATE_ORDER_TABLE = ''' CREATE TABLE IF NOT EXISTS Orders(
OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
DateOrdered REAL,
EmployeeUserName TEXT,
FOREIGN KEY (EmployeeUserName) REFERENCES Employees(EmployeeUserName)
);
'''

CREATE_EMPLOYEES_TABLE = ''' CREATE TABLE IF NOT EXISTS Employees(
EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
EmployeeFirstName TEXT,
EmployeeLastName TEXT,
EmployeePhone INTEGER,
EmployeeUserName TEXT
);
'''

CREATE_ORDER_ITEMS = ''' CREATE TABLE IF NOT EXISTS Order_Items(
OrderID INTEGER,
ItemID INTEGER,
Quantity INTEGER,
PRIMARY KEY (OrderID, ItemID),
FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
FOREIGN KEY (ItemID) REFERENCES Inventory(ItemID)
);'''

INSERT_NEW_ITEM = ''' INSERT INTO Inventory (ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID)
VALUES (?, ?, ?, ?, ?); '''
ADD_EMPLOYEE = ''' INSERT INTO Employees (EmployeeFirstName, EmployeeLastName, EmployeePhone, EmployeeUserName)
VALUES (?, ?, ?, ?);
'''
ADD_MANUFACTURER = ''' INSERT INTO Manufacturer (ManufacturerName, ManufacturerAddress, DayOfDelivery) VALUES (?, ?, ?)
'''
CREATE_ORDER = ''' INSERT INTO Orders (DateOrdered, EmployeeUserName) VALUES (?,?)
'''

ADD_ITEM_TO_ORDER = '''
INSERT INTO Order_Items (OrderID, ItemID, Quantity) VALUES (?,?,?)
'''

CREATE_DELIVERY = ''' INSERT INTO Delivery (OrderID, ManufacturerID) VALUES (?,?)'''

REMOVE_ORDER = ''' DELETE FROM Orders WHERE OrderID = (?)'''
REMOVE_EMPLOYEE = ''' DELETE FROM Employees WHERE EmployeeID = (?); '''
REMOVE_ITEM = ''' DELETE FROM Inventory 
WHERE ItemID = (?);
'''
REMOVE_MANUFACTURER = ''' DELETE FROM Manufacturer WHERE ManufacturerID = (?);
'''

UPDATE_ITEM_STOCK = ''' UPDATE Inventory 
SET ItemQuantity = ? 
WHERE ItemID = ?
'''
UPDATE_DELIVERY_EMP = ''' UPDATE Delivery
SET EmployeeID = ?
WHERE DeliveryID = ?
'''

FETCH_ORDER_ITEMS = ''' SELECT * 
FROM Order_Items 
WHERE OrderID = (?)
'''

VIEW_INVENTORY = ''' SELECT I.ItemName, I.ItemCategory, I.ItemCost, I.ItemQuantity, I.ManufacturerID, 
M.ManufacturerName, M.ManufacturerAddress, M.DayOfDelivery
FROM Inventory AS I
JOIN Manufacturer as M
ON I.ManufacturerID = M.ManufacturerID
'''

VIEW_INVENTORY_BY_CATEOGRY = '''
SELECT * 
FROM Inventory
WHERE ItemCategory = ?
'''

VIEW_IN_STOCK = ''' SELECT * FROM Inventory 
WHERE ItemQuantity > 0
'''
VIEW_OUT_STOCK = ''' SELECT * FROM Inventory 
WHERE ItemQuantity = 0
'''
VIEW_MANUFACTURERS = ''' SELECT * FROM Manufacturer
'''
VIEW_ORDERS = ''' SELECT * FROM Orders '''

VIEW_DELIVERIES = ''' SELECT * FROM Delivery AS D
JOIN Employees AS E
ON D.EmployeeID = E.EmployeeID'''

EMP_DELIVERY_INFO = ''' Select * 
FROM Delivery AS D
JOIN Employees AS E
ON D.EmployeeID = E.EmployeeID
WHERE DeliveryID = ?
'''

SEARCH_MENU_NAME = ''' SELECT *
FROM Inventory
WHERE ItemName = (?)
'''

SEARCH_BY_CATEGORY = ''' SELECT *
FROM Inventory 
WHERE ItemCategory = (?)
'''

NEXT_DELIVERY = ''' SELECT DayOfDelivery
FROM Manufacturer AS M
JOIN Inventory AS I
ON 	I.ManufacturerID = M.ManufacturerID
WHERE M.ManufacturerID = (?)
'''

MANUFACTURER_EXISTS = '''
SELECT ManufacturerID, ManufacturerAddress, DayOfDelivery 
FROM Manufacturer 
WHERE ManufacturerName = ?
'''

MANUFACTURER_EXISTS_2 = '''
SELECT ManufacturerID
FROM Manufacturer
WHERE ManufacturerID = ?
'''

USERNAME_EXISTS = '''
SELECT EmployeeUserName
FROM Employees
WHERE EmployeeUserName = ?
'''

EMPLOYEE_CHECK = ''' SELECT COUNT(*) AS EMP
FROM Employees
'''

VIEW_EMPLOYEES = ''' SELECT * FROM Employees
'''

connection = _sqlite3.connect('Hardware.db')


def create_tables():
    with connection:
        connection.execute(CREATE_MANUFACTURER)
        connection.execute(CREATE_INVENTORY)
        connection.execute(CREATE_ORDER_TABLE)
        connection.execute(CREATE_ORDER_ITEMS)
        connection.execute(CREATE_EMPLOYEES_TABLE)
        connection.execute(CREATE_DELIVERY_TABLE)


def add_item_with_manufacturer(ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerName):
    try:
        with connection:
            # Check if the manufacturer exists
            manufacturer_check = connection.execute(MANUFACTURER_EXISTS,
                                                    (ManufacturerName,))
            manufacturer_details = manufacturer_check.fetchone()
            print(manufacturer_details)

            if not manufacturer_details:
                cursor = connection.cursor()
                # If the manufacturer doesn't exist, prompt for additional details
                ManufacturerAddress = input("Enter manufacturer address: ")
                DayOfDelivery = input("Enter day of delivery: ")
                # Add the manufacturer
                cursor.execute(ADD_MANUFACTURER, (ManufacturerName, ManufacturerAddress, DayOfDelivery))
                # Retrieve the newly added ManufacturerID
                manufacturer_id = cursor.lastrowid
                print(manufacturer_id)
            else:
                # Use existing manufacturer details
                manufacturer_id, existing_address, existing_delivery_day = manufacturer_details

            # Add the item to the inventory
            connection.execute(INSERT_NEW_ITEM, (ItemName, ItemCategory, ItemCost, ItemQuantity, manufacturer_id))
            # Other related operations

    except Exception as e:
        print(f"Transaction failed: {e}")
        connection.rollback()


def add_employee(EmpFirstName, EmpLastName, EmpPhone, EmpUserName):
    with connection:
        connection.execute(ADD_EMPLOYEE, (EmpFirstName, EmpLastName, EmpPhone, EmpUserName))

def username_exists(EmpUserName):
    cursor = connection.cursor()
    cursor.execute(USERNAME_EXISTS, (EmpUserName,))

    return cursor.fetchall()

def create_order(DateOrdered, EmployeeUserName):
    try:
        cursor = connection.cursor()
        cursor.execute(CREATE_ORDER, (DateOrdered, EmployeeUserName))

        print("Order Created Successfully! Please proceed to adding items!")
        return cursor.lastrowid

    except Exception as e:
        print(f"Transaction failed: {e}")
        connection.rollback()

def add_items_to_order(OrderID, ItemID, Quantity):
    with connection:
        connection.execute(ADD_ITEM_TO_ORDER, (OrderID, ItemID, Quantity))
        print("Item added to order successfully!")

def view_inventory_categories():
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT ItemCategory FROM Inventory')

    return cursor.fetchall()

def view_inventory_by_category(ItemCategory):
    cursor = connection.cursor()
    cursor.execute(VIEW_INVENTORY_BY_CATEOGRY, (ItemCategory,))

    return cursor.fetchall()

def remove_order(removeID):
    try:
        with connection:
            connection.execute(REMOVE_ORDER, removeID)

    except Exception as e:
        print(f"Transaction failed: {e}")
        connection.rollback()


def remove_item(ItemID):
    with connection:
        connection.execute(REMOVE_ITEM, ItemID)


def remove_employee(EmployeeID):
    with connection:
        connection.execute(REMOVE_EMPLOYEE, EmployeeID)


def updateItemStock(quantity, _id):
    with connection:
        connection.execute(UPDATE_ITEM_STOCK, (quantity, _id))


def updateDeliveryDriver(DeliveryID, EmployeeID):
    with connection:
        connection.execute(UPDATE_DELIVERY_EMP, (DeliveryID, EmployeeID,))


def viewInventory():
    cursor = connection.cursor()
    cursor.execute(VIEW_INVENTORY)

    return cursor.fetchall()


def viewInStock():
    cursor = connection.cursor()
    cursor.execute(VIEW_IN_STOCK)

    return cursor.fetchall()


def viewOutOfStock():
    cursor = connection.cursor()
    cursor.execute(VIEW_OUT_STOCK)

    return cursor.fetchall()


def viewManufacturers():
    cursor = connection.cursor()
    cursor.execute(VIEW_MANUFACTURERS)

    return cursor.fetchall()

def manufacturer_exists(ManufacturerID):
    cursor = connection.cursor()
    cursor.execute(MANUFACTURER_EXISTS_2, (ManufacturerID,))

    return cursor.fetchall()

def viewOrders():
    cursor = connection.cursor()
    cursor.execute(VIEW_ORDERS)

    return cursor.fetchall()

def viewSpecificOrder(orderID):
    cursor = connection.cursor()
    cursor.execute(FETCH_ORDER_ITEMS, (orderID,))

    return cursor.fetchall()

def viewDeliveries():
    cursor = connection.cursor()
    cursor.execute(VIEW_DELIVERIES, )

    return cursor.fetchall()

def viewEmployees():
    cursor = connection.cursor()
    cursor.execute(VIEW_EMPLOYEES)
    
    return cursor.fetchall()

def removeManufacturer(removeId):
    with connection:
        connection.execute(REMOVE_MANUFACTURER, removeId)


def searchByName(ItemName):
    cursor = connection.cursor()
    cursor.execute(SEARCH_MENU_NAME, (ItemName,))

    return cursor.fetchall()


def searchByCategory(ItemCategory):
    cursor = connection.cursor()
    cursor.execute(SEARCH_BY_CATEGORY, (ItemCategory,))

    return cursor.fetchall()


def getNextDeliveryDate(ManufacturerID):
    cursor = connection.cursor()
    cursor.execute(NEXT_DELIVERY, (ManufacturerID,))

    return cursor.fetchone()


def empDeliveryInfo(DeliveryID):
    cursor = connection.cursor()
    cursor.execute(EMP_DELIVERY_INFO, (DeliveryID,))

    return cursor.fetchall()
