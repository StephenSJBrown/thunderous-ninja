import peewee as pw
import datetime
from models.base_model import BaseModel

class Store(BaseModel):
    name = pw.CharField()
    password = pw.CharField()
    email = pw.CharField(unique=True)
    profile_image = pw.TextField(default="#")
    logo = pw.TextField(default="#")

class Coupon(BaseModel):
    store = pw.ForeignKeyField(Store, backref="")
    name
    category
    value
    description
    cost