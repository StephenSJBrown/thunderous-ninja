import peewee as pw
import re
import datetime
from models.base_model import BaseModel
from models.store import Coupon
from models.centre import Centre
from werkzeug import generate_password_hash
from flask_login import UserMixin


class User(UserMixin ,BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True)
    password = pw.CharField()
    contact = pw.IntegerField(null=True)
    points = pw.IntegerField(default=0)
    profile_image = pw.TextField(default="#")
    background_image = pw.TextField(default="#")


    def validate(self):
        duplicate_username = User.get_or_none(User.username == self.username)
        duplicate_email = User.get_or_none(User.email == self.email)
        password_regex = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

        if self.id == None:
            if duplicate_username:
                self.errors.append(f'{self.username} is unvailable!')
            if duplicate_email:
                self.errors.append(f'{self.email} has already been registered1')
            if re.search(password_regex, self.password) == None:
                self.errors.append('Password must have minimum eight characters, at least one letter and one number!1')
            # if self.password != self.cfm_password:
            #     self.errors.append('Password does not match with password confirmation.')
            else:
                self.password = generate_password_hash(self.password)
        else:
            if self.password == None:
            # to handle edit email and name
                if duplicate_email and self.id != duplicate_email.id:
                    self.errors.append(f'{self.email} has already been registered2')
                else:
                    self.password = User.get_by_id(self.id).password 
            
            # to handle edit password
            else:
                # if self.password != User.password:
                if re.search(password_regex, self.password) == None:
                    self.errors.append('Password must have minimum eight characters, at least one letter and one number!2')
                else:
                    self.password = generate_password_hash(self.password)



class Deposit(BaseModel):
    user = pw.ForeignKeyField(User, backref='deposits', on_delete='CASCADE')
    centre = pw.ForeignKeyField(Centre, backref='deposits', on_delete='CASCADE')
    weight = pw.IntegerField()
    points = pw.IntegerField()

class Purchase(BaseModel):
    user = pw.ForeignKeyField(User, backref='purchases', on_delete='CASCADE')
    coupon = pw.ForeignKeyField(Coupon, backref='purchases', on_delete='CASCADE')
    status = pw.CharField(default='active')




