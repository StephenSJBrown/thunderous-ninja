from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from models.user import User, Purchase
from models.store import Coupon
from flask_login import current_user
import random
import string

purchases_blueprint = Blueprint('purchases',
                            __name__,
                            template_folder='templates')


@purchases_blueprint.route('/create/<coupon_id>', methods=['POST'])
def create(coupon_id):
    buy = request.get_json()
    coupon = Coupon.get_or_none(Coupon.id == coupon_id)
    user = User.get_or_none(User.id == buy['user_id'])

    def randomStringDigits(stringLength=4):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

    if coupon and user:
        if user.points > coupon.cost:
            qrstring = randomStringDigits(4)+'-'+randomStringDigits(4)+'-'+randomStringDigits(4)+'-'+randomStringDigits(4)
            new_purchase = Purchase(user_id=user.id, coupon_id=coupon.id, qr_string=qrstring)
            new_purchase.save()
            User.update(points=user.points - coupon.cost).where(User.id == user.id).execute()
            # add cost column to Purchase?
            return jsonify({
                'message' : 'purchase success',
                'date' : new_purchase.created_at,
                'id' : new_purchase.id,
                'qr_string' : new_purchase.qr_string,
                'user' :{
                    'id' : user.id,
                    'username' : user.username,
                    'email' : user.email,
                    'contact' : user.contact,
                    'points_total' : user.points
                },
                'coupon' : {
                    'id' : coupon.id,
                    'name' : coupon.name,
                    'store' : coupon.store.name,
                    'value' : coupon.value
                }
            }), 200
        else:
            return jsonify({'message' : 'user can\'t afford it.'}), 418
    else:
        return jsonify({'message' : 'user/coupon not found'}), 418


@purchases_blueprint.route('/index/<user_id>', methods=['GET'])
def index(user_id):
    user = User.get_or_none(User.id == user_id)
    if user:
        purchases = user.purchases
        return jsonify([{
            'date' : purchase.created_at,
            'id' : purchase.id,
            'status' : purchase.status,
            'qr_string' :purchase.qr_string,
            'coupon' : {
                'id' : purchase.coupon.id,
                'name' : purchase.coupon.name,
                'value' : purchase.coupon.value,
                'description' : purchase.coupon.description,
                'cost' : purchase.coupon.cost,
                'expiration' : purchase.coupon.expiration,
                'store' : {
                    'id' : purchase.coupon.store.id,
                    'name' : purchase.coupon.store.name,
                    'logo' : purchase.coupon.store.logo
                }
            }
        } for purchase in purchases
        ]), 200
    else:
        return jsonify({'message' : 'user unavailable'}), 418


@purchases_blueprint.route('/show/<purchase_id>', methods=['GET'])
def show(purchase_id):
    purchase = Purchase.get_or_none(Purchase.id == purchase_id)
    if purchase:
        return jsonify({
            'date' : purchase.created_at,
            'id' : purchase.id,
            'user_id' : purchase.user_id,
            'coupon_id' : purchase.coupon_id,
            'status' : purchase.status,
            'qr_string' : purchase.qr_string
        }), 200
    else:
        return jsonify({'message' : 'no record for such purchase'}), 418



#when user redeems coupon, update status to 'redeemed'
@purchases_blueprint.route('/update/<purchase_id>',methods=['POST'])
def update(purchase_id):
    purchase = Purchase.get_or_none(Purchase.id == purchase_id)
    get_status = request.get_json()
    user = get_status['user_id']
    # status = get_status['status']
    get_user = User.get_or_none(User.id == user)
    get_coupon = Coupon.get_or_none(Coupon.id == purchase.coupon_id)

    # if not redeem , return not active
    # if status != 'redeemed':
    #     return jsonify({'message' : 'status must only be \'redeemed\''})

    if purchase and get_user.id == purchase.user_id:
        if purchase.status == 'active':
            Purchase.update(status='redeemed').where(Purchase.id == purchase_id).execute()
            purchase = Purchase.get_or_none(Purchase.id == purchase_id)
            
            return jsonify({
                'message' : 'coupon updated',
                'id' : purchase.id,
                'qr_string' : purchase.qr_string,
                'status' : purchase.status, 
                'user' : {
                    'id' : get_user.id,
                    'username' : get_user.username,
                    'email' : get_user.email,
                    'contact' : get_user.contact,
                },
                'coupon' :{
                    'id' : get_coupon.id,
                    'name' : get_coupon.name,
                    'description' : get_coupon.description
                }
            }), 200
        else:
            return jsonify({'message' : 'this coupon is not active'}), 418
    else:
        return jsonify({'message' : 'no record of such purchase'}), 418


