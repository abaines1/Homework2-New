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

REMOVE_EMPLOYEE = ''' DELETE FROM Employees WHERE EmployeeID = (?); '''
REMOVE_ITEM = ''' DELETE FROM Inventory 
WHERE ItemID = (?);
'''

UPDATE_ITEM_STOCK = ''' UPDATE Inventory 
SET ItemQuantity = ? 
WHERE ItemID = ?
'''

VIEW_INVENTORY = ''' SELECT * FROM Inventory;
'''
VIEW_IN_STOCK = ''' SELECT * FROM Inventory 
WHERE ItemQuantity > 0
'''
VIEW_OUT_STOCK = ''' SELECT * FROM Inventory 
WHERE ItemQuantity = 0
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
