from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify, make_response
from models.store import Store, Coupon

stores_blueprint = Blueprint('stores',
                            __name__,
                            template_folder='templates')

@stores_blueprint.route('/<category>',methods=['GET'])
def index(category):
    stores = Store.select().where(Store.category==category)
    result = []

    if stores:
        for store in stores:
            store_data = {
                'id' : store.id,
                'name' : store.name,
                'email' : store.email,
                'profile-image' : store.profile_image,
                'logo' : store.logo,
                'category' : store.category,
                'coupons' : [
                    {
                        'id' : coupon.id,
                        'name' : coupon.name,
                        'deal' : coupon.value,
                        'points' : coupon.cost,
                    } for coupon in store.coupons
                ]
            }
            result.append(store_data)
        return jsonify({'stores' : result})
    else:
        return jsonify({'message' : 'category not found'})

@stores_blueprint.route('/store/<store_name>',methods=['GET'])
def show(store_name):
    store = Store.get_or_none(Store.name==store_name)
    coupons = Coupon.select().where(Coupon.store_id==store.id)
    
    result = []

    if coupons:
        for coupon in coupons:
            coupon_data = {
                'id' : coupon.id,
                'store_id' : coupon.store_id,
                'name' : coupon.name,
                'deal' : coupon.value,
                'description' : coupon.description,
                'points' : coupon.cost,
                'expiration' : coupon.expiration,
                #npm install momentjs/use moment().format(MM .....) at React, to pull specific date format.
            }
            result.append(coupon_data)
        return jsonify({'coupons' : result}), 200
    else:
        return jsonify({'message' : 'store not available.'}), 418


