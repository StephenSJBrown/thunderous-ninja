from models.base_model import db
from models.user import User, Purchase
from models.store import Store, Coupon

user_data = [
    {'username': 'calix','email':'calix@gmail.com','password':'Password123','contact':'123456'},
    {'username': 'daniel','email':'daniel@gmail.com','password':'Password123','contact':'123456'},
    {'username': 'hseng','email':'hseng@gmail.com','password':'Password123','contact':'123456'},
    {'username': 'stephen','email':'stephen@gmail.com','password':'Password123','contact':'123456'},
    {'username': 'dixon','email':'dixon@gmail.com','password':'Password123','contact':'123456'},
    {'username': 'ethan','email':'ethan@gmail.com','password':'Password123','contact':'123456'},
    {'username': 'liren','email':'liren@gmail.com','password':'Password123','contact':'123456'},
]

store_data = [
    {'name':'mcdonalds','password':'Password123','email':'mcdonalds@gmail.com','category':'food'},
    {'name':'kfc','password':'Password123','email':'kfc@gmail.com','category':'food'},
    {'name':'tealive','password':'Password123','email':'tealive@gmail.com','category':'food'},
    {'name':'uniqlo','password':'Password123','email':'uniqlo@gmail.com','category':'clothing'},
    {'name':'h&m','password':'Password123','email':'h&m@gmail.com','category':'clothing'},
    {'name':'airasia','password':'Password123','email':'airasia@gmail.com','category':'travel'},
    {'name':'malaysia-airline','password':'Password123','email':'malaysia-airline@gmail.com','category':'travel'},
    {'name':'trivago','password':'Password123','email':'trivago@gmail.com','category':'hotels'},
    {'name':'great-eastern','password':'Password123','email':'great-eastern@gmail.com','category':'insurance'},
    {'name':'aia','password':'Password123','email':'aia@gmail.com','category':'insurance'}
]

coupon_data = [
    {'store_id':1,'name':'McRabbit promo','value':25,'description':'delicious rabbit','cost':5000,'expiration':'1/1/2021'},
    {'store_id':1,'name':'McDaddy buy 2 free 1','value':33,'description':'Happy father\'s day','cost':5000,'expiration':'1/1/2021'},
    {'store_id':1,'name':'McDooDoo buy 1 free 1','value':50,'description':'doodoo nice','cost':10000,'expiration':'1/1/2021'},
    {'store_id':2,'name':'Run chicken RUN!','value':20,'description':'catch yo chicken','cost':8000,'expiration':'1/1/2021'},
    {'store_id':2,'name':'Cheeky nuggets','value':30,'description':'nuggets4life','cost':5000,'expiration':'1/1/2021'},
    {'store_id':3,'name':'Boba for life','value':15,'description':'Boba for life','cost':5000,'expiration':'1/1/2021'},
    {'store_id':4,'name':'comfy clothes','value':25,'description':'very comfy clothes','cost':5000,'expiration':'1/1/2021'},
    {'store_id':4,'name':'comfy pants','value':35,'description':'very comfy pants','cost':10000,'expiration':'1/1/2021'},
    {'store_id':5,'name':'not so comfy pants','value':75,'description':'very not comfy pants','cost':5000,'expiration':'1/1/2021'}
]

purchase_data = [
    {"user_id":1,"coupon_id":1,"status":"active"},
    {"user_id":1,"coupon_id":1,"status":"redeemed"},
    {"user_id":2,"coupon_id":1,"status":"expired"},
    {"user_id":4,"coupon_id":2,"status":"active"},
    {"user_id":7,"coupon_id":2,"status":"active"},
    {"user_id":5,"coupon_id":2,"status":"expired"}
]

def seed_users():
    try:
        for row in db.batch_commit(user_data, 100):
            User.create(**row)
    except:
        print('user problem')

    try:
        for row in db.batch_commit(store_data, 100):
            Store.create(**row)
    except:
        print('store problem')
    
    try:
        for row in db.batch_commit(coupon_data, 100):
            Coupon.create(**row)
    except:
        print('coupon problem')

    try:
        for row in db.batch_commit(purchase_data, 100):
            Purchase.create(**row)
    except:
        print('purchase problem')

    print('seed complete')