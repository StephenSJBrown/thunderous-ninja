# thunderous ninja
`To install seed file:`
`pip install -r requirements.txt`
`createdb <'your-db-name>`
`python migrate.py`
`flask seed`


This is a great app.

The Models are as follows:

User:
    ID
    Username
    Password
    Email
    Name
    Points
    profile_photo

Store:
    ID
    Name
    Password
    Email
    profile_photo
    logo 

Coupon:
    ID
    Name
    Category
    Expiry Date
    Value
    Description
    Cost
    Store

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
    Status
