import peewee as pw
from models.base_model import BaseModel

class Store(BaseModel):
    name = pw.CharField()
    password = pw.CharField()
    email = pw.CharField(unique=True)
    profile_image = pw.TextField(default="#")
    logo = pw.TextField(default="#")

class Coupon(BaseModel):
    store = pw.ForeignKeyField(Store, backref="coupons")
    name = pw.CharField()
    category = pw.CharField()
    value = pw.IntegerField()
    description = pw.CharField
    cost = pw.BigIntegerField()s