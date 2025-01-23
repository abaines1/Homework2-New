sequenceDiagram
    participant User
    participant MainApp
    participant Database

    User->>MainApp: Start create_order()
    MainApp->>User: Prompt for DateOrdered
    User->>MainApp: Enter DateOrdered
    MainApp->>MainApp: Validate DateOrdered
    MainApp->>User: Prompt for EmployeeUserName
    User->>MainApp: Enter EmployeeUserName
    MainApp->>Database: Check username_exists(EmployeeUserName)
    Database-->>MainApp: Return True/False

    alt Employee exists
        MainApp->>Database: create_order(DateOrdered, EmployeeUserName)
        Database-->>MainApp: Return orderID
        MainApp->>User: Prompt to add items (Y/N)
        User->>MainApp: Enter Y
        loop Add items
            MainApp->>User: Prompt for ItemID
            User->>MainApp: Enter ItemID
            MainApp->>User: Prompt for ItemQuantity
            User->>MainApp: Enter ItemQuantity
            MainApp->>Database: add_items_to_order(orderID, ItemID, ItemQuantity)
            MainApp->>User: Prompt to add more items (Y/N)
            User->>MainApp: Enter Y/N
        end
    else Employee does not exist
        MainApp->>User: Print "Employee does not exist"
    end