from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from models.user import User, Purchase
from models.store import Coupon
from flask_login import current_user

purchases_blueprint = Blueprint('purchases',
                            __name__,
                            template_folder='templates')


@purchases_blueprint.route('/', methods=['POST'])
def create():
    buy = request.get_json()

    coupon = Coupon.get_or_none(Coupon.id == buy['coupon_id'])
    if coupon:
        user = User.get_or_none(User.id == buy['user_id'])
        if user:
            new_purchase = Purchase(user_id=user.id, coupon_id=coupon.id)
            new_purchase.save()
            # User.update(points=user.points - new_purchase.points).where(User.id == user.id).execute()
            # add cost column to Purchase?
            return jsonify({
                'message' : 'purchase success',
                'date' : new_purchase.created_at,
                'id' : new_purchase.id,
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
                    'store' : store.name,
                    'value' : coupon.value
                }
            }) 
        else:
            return jsonify({'message' : 'user not found'})
    else:
        return jsonify({'message' : 'coupon not found'})


@purchases_blueprint.route('/show/<user_id>', methods=['GET'])
def show(user_id):
    purchases = Purchase.get_or_none(Purchase.user_id == user_id)

    if purchases:
        return jsonify([{
            'id' : purchase.id,
            'coupon_id' : purchase.coupon.id,
            'status' : purchase.status
        } for purchase in purchases
    ]), 200

    else:
        return jsonify({'message' : 'user unavailable'}), 418

# @purchases_blueprint.route('/')
# def update():
#     #when user redeems coupon, update status to 'redeemed'


