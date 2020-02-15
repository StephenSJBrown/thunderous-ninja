from models.base_model import db
from models.user import User, Purchase, Deposit
from models.store import Store, Coupon
from models.centre import Centre


user_data = [
    {'username': 'calix','email':'calix@gmail.com','password':'Password123','contact':'123456','points':600},
    {'username': 'daniel','email':'daniel@gmail.com','password':'Password123','contact':'123456','points':100},
    {'username': 'hseng','email':'hseng@gmail.com','password':'Password123','contact':'123456','points':100000},
    {'username': 'stephen','email':'stephen@gmail.com','password':'Password123','contact':'123456','points':37000},
    {'username': 'dixon','email':'dixon@gmail.com','password':'Password123','contact':'123456','points':0},
    {'username': 'ethan','email':'ethan@gmail.com','password':'Password123','contact':'123456','points':0},
    {'username': 'liren','email':'liren@gmail.com','password':'Password123','contact':'123456','points':0}
]

store_data = [
    {'name':'mcdonalds','password':'Password123','email':'mcdonalds@gmail.com','category':'food',
    'logo':'https://miro.medium.com/max/2000/1*sszpZOih_xJV_lZsDbog-Q.png'},
    {'name':'kfc','password':'Password123','email':'kfc@gmail.com','category':'food',
    'logo':'https://upload.wikimedia.org/wikipedia/sco/thumb/b/bf/KFC_logo.svg/1200px-KFC_logo.svg.png'},
    {'name':'tealive','password':'Password123','email':'tealive@gmail.com','category':'food',
    'logo':'https://vectorlogo4u.com/wp-content/uploads/2019/10/Tealive-logo-vector-720x340.png'},
    {'name':'uniqlo','password':'Password123','email':'uniqlo@gmail.com','category':'clothing',
    'logo':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/UNIQLO_logo.svg/1200px-UNIQLO_logo.svg.png'},
    {'name':'h&m','password':'Password123','email':'h&m@gmail.com','category':'clothing',
    'logo':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/H%26M-Logo.svg/1200px-H%26M-Logo.svg.png'},
    {'name':'airasia','password':'Password123','email':'airasia@gmail.com','category':'travel',
    'logo':'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/AirAsia_New_Logo.svg/1024px-AirAsia_New_Logo.svg.png'},
    {'name':'malaysia-airline','password':'Password123','email':'malaysia-airline@gmail.com','category':'travel',
    'logo':'https://lh3.googleusercontent.com/proxy/CDPla9z81tfwvSlF2uD65aTkdMVT4jZnVEOxto67YFK9ku9p3dLia7tByZ2i2vu1Z1yjxeMP6yRPncJYHlDSjz98qf0v0ncNrmgJ43EiXURtHogL3M_nMZMionUK7EL82Pd7mQ4L'},
    {'name':'trivago','password':'Password123','email':'trivago@gmail.com','category':'hotels',
    'logo':'https://pluspng.com/img-png/trivago-logo-png--640.png'},
    {'name':'great-eastern','password':'Password123','email':'great-eastern@gmail.com','category':'insurance',
    'logo':'https://logoeps.com/wp-content/uploads/2012/10/great-eastern-logo-vector.png'},
    {'name':'aia','password':'Password123','email':'aia@gmail.com','category':'insurance',
    'logo':'https://seeklogo.com/images/A/aia-logo-618BFE8E96-seeklogo.com.png'},
    {'name':'genting','password':'Password123','email':'genting@gmail.com','category':'experience',
    'logo':'https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/102011/resortworld_0.png?itok=PpciQM7Z'}
]

coupon_data = [
    {'store_id':1,'name':'McRabbit promo','value':25,'description':'delicious rabbit','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://images2.minutemediacdn.com/image/upload/c_crop,h_1414,w_2102,x_0,y_0/v1554351612/shape/mentalfloss/557234-istock-480927021.jpg?itok=BhBBCMJr'},
    {'store_id':1,'name':'McDaddy buy 2 free 1','value':33,'description':'Happy father\'s day','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://images.theconversation.com/files/127128/original/image-20160617-11112-1e7k2u0.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=926&fit=clip'},
    {'store_id':1,'name':'McDooDoo buy 1 free 1','value':50,'description':'doodoo nice','cost':10000,'expiration':'1/1/2021',
    'coupon_image':'https://2.bp.blogspot.com/-9rTRy8leOYM/TzRgJaqMAFI/AAAAAAAAGeE/eWl_VR-zyNI/s1600/doo+doo+cookies.jpg'},
    {'store_id':2,'name':'Run chicken RUN!','value':20,'description':'catch yo chicken','cost':8000,'expiration':'1/1/2021',
    'coupon_image':'https://i.ytimg.com/vi/-INJ2xwNLJI/maxresdefault.jpg'},
    {'store_id':2,'name':'Cheeky nuggets','value':30,'description':'nuggets4life','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://www.syioknya.com/custom/picture/13761/syioknya1_5daf2d0b8c553.jpg'},
    {'store_id':3,'name':'Boba for life','value':15,'description':'Boba for life','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://d3avoj45mekucs.cloudfront.net/rojakdaily/media/nur-afiqah/dr%20hartini%20for%20chowkit/main3.jpg?ext=.jpg'},
    {'store_id':4,'name':'comfy clothes','value':25,'description':'very comfy clothes','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://image.uniqlo.com/is/image/UNIQLO/eu-pc-150928-stores-detail-be-belgian-store.jpg'},
    {'store_id':4,'name':'comfy pants','value':35,'description':'very comfy pants','cost':10000,'expiration':'1/1/2021',
    'coupon_image':'https://www.uniqlo.com/my/img/140915_ourstory_01.jpg'},
    {'store_id':5,'name':'not so comfy pants','value':75,'description':'very not comfy pants','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://images.businessoffashion.com/site/uploads/2018/02/shutterstock_1029515539.jpg?auto=format%2Ccompress&crop=top&fit=crop&h=275&w=494'},
    {'store_id':6,'name':'fly! you fools~','value':25,'description':'fly while you can.','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://www.traveldailymedia.com/assets/2019/09/A321XLR-AirAsia--e1567567856589.jpg'},
    {'store_id':7,'name':'world class flying!','value':35,'description':'WOOOOORLD class!','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://d3avoj45mekucs.cloudfront.net/rojakdaily/media/marcus-images/power%20rangers/malaysia-airlines-satellite-flight-tracking.png?ext=.png'},
    {'store_id':8,'name':'Hotel?','value':25,'description':'TRIVAGO!','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://imgcy.trivago.com/c_limit,d_dummy.jpeg,f_auto,h_1300,q_auto,w_2000/itemimages/35/40/35404_v5.jpeg'},
    {'store_id':9,'name':'Have you insured yourself from Corona Virus?','value':25,'description':'too late! haha!','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://i.imgflip.com/1od0i5.jpg'},
    {'store_id':10,'name':'great eastern won\'t insure you from the Corona Virus?','value':25,'description':'neither do we! haha!','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://imgflip.com/s/meme/Laughing-Men-In-Suits.jpg'},
    {'store_id':11,'name':'get rich today!','value':25,'description':'Get rich quick from our casino services','cost':5000,'expiration':'1/1/2021',
    'coupon_image':'https://www.sarcasm.co/wp-content/uploads/2019/07/rich-guy.jpg'},
    
]

purchase_data = [
    {"user_id":1,"coupon_id":1,"status":"active","qr_string":"MbSR-b9Po-lOqg-oBHO"},
    {"user_id":1,"coupon_id":1,"status":"redeemed","qr_string":"q171-DdNs-vZpJ-zmgz"},
    {"user_id":2,"coupon_id":1,"status":"expired","qr_string":"cQvn-oVB6-1TUf-yKF3"},
    {"user_id":4,"coupon_id":2,"status":"active","qr_string":"MnEx-u0m2-twnk-KUK8"},
    {"user_id":7,"coupon_id":2,"status":"active","qr_string":"To9S-PPIU-Ge0s-2KfC"},
    {"user_id":5,"coupon_id":2,"status":"expired","qr_string":"i4HH-GEOE-JRHx-QzE7"}
]

centre_data = [
    {"name":"IPC Recycling & Buy-Back Centre","place_id":"ChIJ6eTsxytPzDERW07hq6W8cBA"},
    {"name":"Tzu Chi Kayu Ara Recycle Center","place_id":"ChIJddVFuspOzDERNJ8jbM4Dunk"},
    {"name":"Tzu Chi Recycling Point","place_id":"ChIJa3VfKVFJzDER1oZDn3umsgk"}
]

deposit_data = [
    {"user_id":1,"centre_id":1,"weight":2,"points":200},
    {"user_id":1,"centre_id":1,"weight":4,"points":400},
    {"user_id":4,"centre_id":2,"weight":60,"points":6000},
    {"user_id":4,"centre_id":3,"weight":40,"points":4000},
    {"user_id":4,"centre_id":2,"weight":80,"points":8000},
    {"user_id":4,"centre_id":3,"weight":50,"points":5000},
    {"user_id":4,"centre_id":3,"weight":50,"points":5000},
    {"user_id":4,"centre_id":2,"weight":90,"points":9000},
    {"user_id":2,"centre_id":3,"weight":1,"points":100},
    {"user_id":3,"centre_id":1,"weight":1000,"points":100000},
]

def seed_users():
    for row in db.batch_commit(user_data, 100):
        User.create(**row)

    for row in db.batch_commit(store_data, 100):
        Store.create(**row)
    
    for row in db.batch_commit(coupon_data, 100):
        Coupon.create(**row)

    for row in db.batch_commit(purchase_data, 100):
        Purchase.create(**row)

    for row in db.batch_commit(centre_data, 100):
        Centre.create(**row)

    for row in db.batch_commit(deposit_data, 100):
        Deposit.create(**row)

    # try:
    #     for row in db.batch_commit(deposit_data, 100):
    #         Centre.create(**row)
    # except:
    #     print('centre problem')

    print('seed complete')