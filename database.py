import _sqlite3

CREATE_INVENTORY = ''' CREATE TABLE IF NOT EXISTS Inventory(
ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
ItemName TEXT, 
ItemCategory TEXT,
ItemCost FLOAT,
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
connection = _sqlite3.connect('Hardware.db')


def create_tables():
    with connection:
        connection.execute(CREATE_MANUFACTURER)
        connection.execute(CREATE_INVENTORY)
        connection.execute(CREATE_ORDER_TABLE)
        connection.execute(CREATE_EMPLOYEES_TABLE)
        connection.execute(CREATE_DELIVERY)
