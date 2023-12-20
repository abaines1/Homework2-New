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

CREATE_DELIVERY = ''' CREATE TABLE IF NOT EXISTS Delivery(
DeliveryID INTEGER PRIMARY KEY AUTOINCREMENT,
OrderID INTEGER,
EmployeeID INTEGER,
ExpectedDelivery REAL,
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
'''

CREATE_ORDER_TABLE = ''' CREATE TABLE IF NOT EXISTS Orders(
OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
DateOrdered REAL,
ManufacturerID INTEGER,
FOREIGN KEY (ManufacturerID) REFERENCES Manufacturer(ManufacturerID)
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

INSERT_NEW_ITEM = ''' INSERT INTO Inventory (ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID)
VALUES (?, ?, ?, ?, ?);
'''
ADD_EMPLOYEE = ''' INSERT INTO Employees (EmployeeFirstName, EmployeeLastName, EmployeePhone, EmployeeUserName)
VALUES (?, ?, ?, ?);
'''
ADD_MANUFACTURER = ''' INSERT INTO Manufacturer (ManufacturerName, ManufacturerAddress, DayOfDelivery) VALUES (?, ?, ?)
'''

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

VIEW_INVENTORY = ''' SELECT I.ItemName, I.ItemCategory, I.ItemCost, I.ItemQuantity, I.ManufacturerID, 
M.ManufacturerName, M.ManufacturerAddress, M.DayOfDelivery
FROM Inventory AS I
JOIN Manufacturer as M
ON I.ManufacturerID = M.ManufacturerID
'''
VIEW_IN_STOCK = ''' SELECT * FROM Inventory 
WHERE ItemQuantity > 0
'''
VIEW_OUT_STOCK = ''' SELECT * FROM Inventory 
WHERE ItemQuantity = 0
'''
VIEW_MANUFACTURERS = ''' SELECT * FROM Manufacturer;
'''

SEARCH_MENU_NAME = ''' SELECT *
FROM Inventory
WHERE ItemName = (?)
'''

SEARCH_BY_CATEGORY = ''' SELECT *
FROM Inventory 
WHERE ItemCategory = (?)
'''

connection = _sqlite3.connect('Hardware.db')


def create_tables():
    with connection:
        connection.execute(CREATE_MANUFACTURER)
        connection.execute(CREATE_INVENTORY)
        connection.execute(CREATE_ORDER_TABLE)
        connection.execute(CREATE_EMPLOYEES_TABLE)
        connection.execute(CREATE_DELIVERY)


def add_item(ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID):
    with connection:
        connection.execute(INSERT_NEW_ITEM, (ItemName, ItemCategory, ItemCost, ItemQuantity, ManufacturerID))


def add_employee(EmpFirstName, EmpLastName, EmpPhone, EmpUserName):
    with connection:
        connection.execute(ADD_EMPLOYEE, (EmpFirstName, EmpLastName, EmpPhone, EmpUserName))


def add_manufacture(ManufacturerName, ManufacturerAddress, DayOfDelivery):
    with connection:
        connection.execute(ADD_MANUFACTURER, (ManufacturerName, ManufacturerAddress, DayOfDelivery))


def remove_item(ItemID):
    with connection:
        connection.execute(REMOVE_ITEM, ItemID)


def remove_employee(EmployeeID):
    with connection:
        connection.execute(REMOVE_EMPLOYEE, EmployeeID)


def updateItemStock(quantity, _id):
    with connection:
        connection.execute(UPDATE_ITEM_STOCK, (quantity, _id))


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


def removeManufacturer(removeId):
    with connection:
        connection.execute(REMOVE_MANUFACTURER, removeId)


def searchByName(ItemName):
    cursor = connection.cursor()
    cursor.execute(SEARCH_MENU_NAME, (ItemName,))

    return cursor.fetchall()


def searchByCategory(ItemCategory):
    cursor = connection.cursor()
    cursor.execute(SEARCH_BY_CATEGORY, (ItemCategory, ))

    return cursor.fetchall()
