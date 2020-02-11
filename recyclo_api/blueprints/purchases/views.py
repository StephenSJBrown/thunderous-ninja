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
        user = User.get_or_none(current_user.id == buy['user_id'])
        if coupon and user:
            new_purchase = Purchase(user_id=user.id, coupon_id=coupon.id)
            new_purchase.save()
            return jsonify({'message' : 'purchase success'}) 
        else:
            return jsonify({'message' : 'user not found'})
    else:
        return jsonify({'message' : 'coupon not found'})



