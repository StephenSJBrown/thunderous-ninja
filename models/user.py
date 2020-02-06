import peewee as pw
import datetime
from models.base_model import BaseModel

class User(BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True)
    password = pw.CharField()
    contact = pw.IntegerField()
    points = pw.IntegerField()
    profile_image = pw.TextField(default="#")
    background_image = pw.TextField(default="#")


class Deposit(BaseModel):
    user
    centre
    weight

class Purchase(BaseModel):
    user
    coupon
    status


