from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify, make_response
from models.store import Coupon
from datetime import datetime
coupons_blueprint = Blueprint('coupons',
                            __name__,
                            template_folder='templates')

@coupons_blueprint.route('/<coupon_id>',methods=['GET'])
def show(coupon_id):
    coupon = Coupon.get_or_none(Coupon.id==coupon_id)

    if coupon:
        return jsonify({
            'id' : coupon.id,
            'store_id' : coupon.store_id,
            'name' : coupon.name,
            'deal' : coupon.value,
            'description' : coupon.description,
            'points' : coupon.cost,
            'expiration' : coupon.expiration,
        })
    else:
        return jsonify({'message' : 'coupon not found.'})


