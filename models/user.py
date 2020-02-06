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
    user = pw.ForeignKeyField(User, backref='deposits', on_delete='CASCADE')
    centre = pw.ForeignKeyField(User, backref='deposits', on_delete='CASCADE')
    weight = pw.IntegerField()

class Purchase(BaseModel):
    user = pw.ForeignKeyField(User, backref='purchases', on_delete='CASCADE')
    coupon = pw.ForeignKeyField(User, backref='purchases', on_delete='CASCADE')
    status = pw.CharField(default='active')


