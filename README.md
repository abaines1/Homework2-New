# Homework2-New

- SQLite Version - Inventory System - 12/18/2023

## Introduction

---

**_ Add Item + Manufacturer = 1 Trans
_** Add Order + Add Delivery = 1 Trans

**_ Employee _**

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
    - What day is delivery? (Day Example: Monday, Tuesday, Wednesday, etc.)

  - Delivery Person

    - Name
    - Phone Number

- User Actions

  - Insert New Items \*
  - Remove Items \*
  - Search Item by Name or Category \*

    - Retrieve number of item in stock

      - If item is out of stock, return next possible delivery date \*

    - If no items matching search term handle this \*
    - Update stock amount !!!---!!! \*
    - View sold out items \*
    - View last delivery person for specific item \*
    - Update delivery person for an item (sign in when updating stock?) \*\*\*

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

1. Inventory 2) View Full Inventory (In and Out of Stock Items) 3) View In Stock Inventory 4) View Out of Stock Inventory
2. Search (By Name or Category) 6) Return stock and other info 6) Flag if Out of Stock 7) Who will deliver the item and when?
3. Update Inventory 9) Add Items 10) Remove items 11) Username of Employee
4. Employee Accounts 13) Add Employee 14) Remove Employee 15) View Employees
5. Exit

### Software Design Processes

1. Build Menu
2.

### TODO

- [ ] 2. What is the ORDER_ITEMS table?
- [ ] 4. One big Inventory Menu with sub menus? (Not being able to view inventory before adding things doesnt make sense)

  **_ NEW MENU _**

  1. Inventory
     1. View Inventory
        Which store inventory report do you need?
        1. Total Inventory
        2. In Stock Inventory
        3. Out of Stock Inventory
        4. Go Back
     2. Update Inventory
        1. Add New Item
        2. Remove Item
        3. Update Quantity
        4. Go Back
     3. Search Inventory
        Do you want to search by name or category?
        1. Name
           1. What is the name of the item you want to search for?
                1. Return error if no item is found
        2. Category
           1. What is the category of the item you want to search for?
                1. {print known item categories}
                2. Return error if no categories exist or the one searched is not found
        3. Go Back
     4. Manufacturer Information
        1. View All Manufacturers 
        2. Add New Manufacturer
        3. Update Manufacturer
        4. Delete Manufacturer
        5. Go Back
     5. Go back
  1. Employee Menu
        1. View Employees
        2. Create New Employee
        3. Delete Employee
  3. Orders
        1. View Orders
        2. Create New Order
        3. Delete Order
        4. Go Back
  4. Sign off

- [ ] 10. Updates to Order Menu functionality
  - [ ] a. If there are no employees it prints that there are none to assign to. After this we should prompt to add an employee
  - [ ] b. **_why manu id isnt this the company's employee?_**
  - [ ] c. When asked to input the date - should we assume that the order was placed on todays date?
  - [ ] d. If there are no orders - when choosing delete - it should say that there are no orders found and to please add data to the database

- [ ] 11. When going back in Search menu it needs to be go back on 3 not 4 \*\*\*\*
- [ ] 12. When changing quantity of items in stock, maybe when prompting show how many items are currently in stock in the system? \*\*\*\*
- [ ] 13. Print Inventory showing the items ^^^ and maybe say "Item Deleted" if successful \*\*\*\*
- [ ] 14. Update Quantity of an Item \*\*\*\*
  - [ ] a. When selecting you are then prompted with a delete querey when it should be asking what you want to update
  - [ ] b. When asking about ID of what you are updating, after selecting, print the items details to insure the item selected is the correct option
  - [ ] c. If no item exists, alert the user (inventory is empty or item id selected does not exist)

#### Ideas:

- Potential: When opening the database for the first time (with no inventory or anything) maybe a seperate menu should prompt information to be created before the database can even be viewed
- Potential: Admin vs User? (admin can create employees, etc)
- Potential: Editing menu spacing layouts

#### Finished Tasks:

1. When there is no inventory at first time of DB file creation, it should return by saying "Inventory Database Empty. Please add data to the database and retry." **_ AS OF 6/11/2024 at 1250pm completed _**
2. View Employees under the Employee Tab **_ AS OF 6/15/2024 at 1106AM completed _**
3. If there are no deliveries, return (Currently no deliveries) **_ AS OF 1/16/2025 - COMPLETED _**
4. If there are no orders, return (currently no orders) **_ AS OF 1/16/2025 - COMPLETED _**
5. When adding an item to inventory, if the price is 13.99, the database can only accept an int (change to float) **_ AS OF 1/16/2025 - COMPLETED _**
6. Price Not in the Print() when viewing inventory && seperator between Price, Quantity, and ManID in View Inventory **_ AS OF 1/16/2025 - COMPLETED _**
7. Seperator between ManAddress and DayOfDelivery in View Manufacturers **_ AS OF 1/17/2025 - COMPLETED _**
   +- There are two different functions of Viewing Manufactures **_ DONE _**
   +- One is located in the menu and the other is a separate function called listManufacturers **_ DONE _**
