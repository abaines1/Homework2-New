# Homework2-New
SQLite Version - Inventory System - 12/18/2023

## Introduction



### Tasks: 

- Store the following information: 

    - Items
  
        - Item Name
        - Item Category
        - Cost of Item
        - Quantity in stock

            - Flag if Out of Stock
    
    - Manufacturer

        - Address of Manufacturer
        - What day is delivery? (Day Example: Monday, Tuesday, Wednesday,  etc.)

    - Delivery Person

        - Name
        - Phone Number

- User Actions

    - Insert New Items *
    - Remove Items *
    - Search Item by Name or Category *

        - Retrieve number of item in stock
  
            - If item is out of stock, return next possible delivery date *
      - If no items matching search term handle this *
      - Update stock amount !!!---!!! *
      - View sold out items *
      - View last delivery person for specific item *
      - Update delivery person for an item (sign in when updating stock?) ***

### Database Schema

    Items: 
        - ItemID(PK)
        - ItemName
        - ItemCategory
        - ManufacturerID(FK)
        - ItemCost
        - ItemQuantity
    
    Manufacturer: 
        - ManufacturerID(PK)
        - ManufacturerName
        - ManufacturerAddress
        - DayOfDelivery

    Delivery:
        - DeliveryID(PK)
        - OrderID(FK)
        - EmployeeID(FK)
        - Status
        - ExpectedDelivery

    Orders: 
        - OrderID(PK)
        - ManufacturerID(FK)
        - DateOrdered

    Employees: 
        - EmployeeID(PK)
        - EmployeeFirstName
        - EmployeeLastName
        - EmployeePhoneNumber
        - EmployeeUserName



### Menu Design 

Welcome to AB Hardware!
What would you like to do?

1) Inventory
   2) View Full Inventory (In and Out of Stock Items)
   3) View In Stock Inventory
   4) View Out of Stock Inventory
5) Search (By Name or Category)
   6) Return stock and other info
   6) Flag if Out of Stock
   7) Who will deliver the item and when? 
8) Update Inventory
   9) Add Items
   10) Remove items
   11) Username of Employee
12) Employee Accounts
    13) Add Employee
    14) Remove Employee
    15) View Employees
16) Exit 


### Software Design Processes

1) Build Menu
2) 
