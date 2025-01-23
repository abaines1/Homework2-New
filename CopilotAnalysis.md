import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute(CREATE_MANUFACTURER)
            self.connection.execute(CREATE_INVENTORY)
            self.connection.execute(CREATE_ORDER_TABLE)
            self.connection.execute(CREATE_ORDER_ITEMS)
            self.connection.execute(CREATE_EMPLOYEES_TABLE)
            self.connection.execute(CREATE_DELIVERY_TABLE)

    def add_employee(self, EmpFirstName, EmpLastName, EmpPhone, EmpUserName):
        with self.connection:
            self.connection.execute(ADD_EMPLOYEE, (EmpFirstName, EmpLastName, EmpPhone, EmpUserName))

    def username_exists(self, EmpUserName):
        cursor = self.connection.cursor()
        cursor.execute(USERNAME_EXISTS, (EmpUserName,))
        return cursor.fetchone() is not None

    def create_order(self, DateOrdered, EmployeeUserName):
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(CREATE_ORDER, (DateOrdered, EmployeeUserName))
                return cursor.lastrowid
        except Exception as e:
            print(f"Transaction failed: {e}")
            self.connection.rollback()
            return None

    def add_items_to_order(self, order_id, ItemID, ItemQuantity):
        with self.connection:
            self.connection.execute(ADD_ITEM_TO_ORDER, (order_id, ItemID, ItemQuantity))

# filepath: /Users/austinbaines/VisualCodeStudio/Homework2-New/main.py
import re
from database import Database

db = Database('Hardware.db')

def create_order():
    try:
        DateOrdered = input("What is the date of the order? (mm-dd-yyyy) ")
        if not re.match(r'\d{2}-\d{2}-\d{4}', DateOrdered):
            print("Invalid date format. Please use mm-dd-yyyy")
            return
        
        EmployeeUserName = input("What is the username of the employee who is creating the order? ")
        if db.username_exists(EmployeeUserName):
            order_id = db.create_order(DateOrdered, EmployeeUserName)
            if order_id is None:
                print("Failed to create order")
                return
        else:
            print("Employee does not exist")
            return
        
        while (user_input := input("Would you like to add items to the order? (y/n) ")) != "n":
            ItemID = input("What is the ID of the item? ")
            ItemQuantity = int(input("How many of the item are you adding? "))
            db.add_items_to_order(order_id, ItemID, ItemQuantity)

    except Exception as e:
        print(f"Error: {e}")

def employee_menu():
    employee_menu = """ --- Employee Menu ---
    1) View Employees
    2) Add Employee
    3) Remove Employee
    4) Go Back
    """
    print(employee_menu)
    # Add logic to handle employee menu options

# Example usage
create_order()