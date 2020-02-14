import peewee as pw
from models.base_model import BaseModel

class Store(BaseModel):
    name = pw.CharField(unique=True)
    password = pw.CharField()
    email = pw.CharField(unique=True)
    logo = pw.TextField(default="#")
    category = pw.CharField()

class Coupon(BaseModel):
    store = pw.ForeignKeyField(Store, backref="coupons")
    name = pw.CharField()
    value = pw.IntegerField()
    description = pw.CharField()
    cost = pw.IntegerField()
    expiration = pw.DateField()
    coupon_image = pw.TextField(default="#")