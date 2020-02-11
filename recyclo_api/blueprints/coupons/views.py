from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify, make_response
from models.store import Coupon
from datetime import datetime
coupons_blueprint = Blueprint('coupons',
                            __name__,
                            template_folder='templates')

@coupons_blueprint.route('/<store_id>/index',methods=['GET'])
def index(store_id):
    coupons = Coupon.select().where(Coupon.store_id==store_id)
    result = []

    if coupons:
        for coupon in coupons:
            coupon_data = {
                'coupon-id' : coupon.id,
                'coupon-store_id' : coupon.store_id,
                'coupon-name' : coupon.name,
                'coupon-deal' : coupon.value,
                'coupon-description' : coupon.description,
                'coupon-points' : coupon.cost,
                'coupon-expiration' : coupon.expiration,
                #npm install momentjs/use moment().format(MM .....) at React, to pull specific date format.
            }
            result.append(coupon_data)
        return jsonify({'coupons' : result})
    else:
        return jsonify({'message' : 'category not available.'})

@coupons_blueprint.route('/<coupon_id>',methods=['GET'])
def show(coupon_id):
    coupon = Coupon.get_or_none(Coupon.id == coupon_id)

    if coupon:
        return jsonify({
            'coupon-id' : coupon.id,
            'coupon-store_id' : coupon.store_id,
            'coupon-name' : coupon.name,
            'coupon-deal' : coupon.value,
            'coupon-description' : coupon.description,
            'coupon-points' : coupon.cost,
            'coupon-expiration' : coupon.expiration,
        })
    else:
        return jsonify({'message' : 'coupon not found.'})


