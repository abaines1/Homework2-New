# Homework2-New
SQLite Version - Inventory System - 12/18/2023

## Introduction

*** 
*** Add Item + Manufacturer = 1 Trans
*** Add Order + Add Delivery = 1 Trans

*** Employee ***

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


### TODO

1) When there is no inventory at first time of DB file creation, it should return by saying "Inventory Database Empty. Please add data to the database and retry." **** AS OF 6/11/2024 at 1250pm completed ***
2) What is the ORDER_ITEMS table?
3) View Employees under the Employee Tab
4) One big Inventory Menu with sub menus? (Not being able to view inventory before adding things doesnt make sense)
5) If there are no deliveries, return (Currently no deliveries)
6) If there are no orders, return (currently no orders)
7) When adding an item to inventory, if the price is 13.99, the database can only accept an int (change to float)
8) Price Not in the Print() when viewing inventory && seperator between Price, Quantity, and ManID in View Inventory
9) Seperator between ManAddress and DayOfDelivery in View Manufacturers
10) When creating orders, it says after inputing ManuID (***why manu id isnt this the company's employee?***)
11) when going back iin Search menu it needs to be go back on 3 not 4
12) When changing quantity of items in stock, maybe when prompting show how many items are currently in stock in the system? 

Potential: When opening the database for the first time (with no inventory or anything) maybe a seperate menu should prompt information to be created before the database can even be viewed
Potential: Admin vs User? (admin can create employees, etc)
