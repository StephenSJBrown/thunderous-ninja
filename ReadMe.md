This is a great app.

The Models are as follows:

User:
    ID
    Username
    Password
    Email
    Name
    Points

Store:
    ID
    Name
    Password
    Email

Coupon:
    ID
    Name
    Expiry Date
    Value
    Description
    Cost
    
Centre:
    ID
    Name
    Location

Deposit:
    ID
    |FK| User
    |FK| Centre
    Weight

Purchase:
    ID
    |FK| User
    |FK| Coupon
