from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from models.user import User, Coupon
from flask_login import current_user

purchases_blueprint = Blueprint('purchases',
                            __name__,
                            template_folder='templates')


@purchases_blueprint.route('/<coupon_id>', methods=['GET'])
def create(coupon_id):
    coupon = Coupon.get_or_none(Coupon.id == coupon_id)
    user = User.get_or_none(current_user.id == User.id)
    if coupon and user:
        new_purchase = Purchase(user_id=user.id, coupon_id=coupon.id)
        new_purchase.save()


