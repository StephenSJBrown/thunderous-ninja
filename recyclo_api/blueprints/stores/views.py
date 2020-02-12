from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify, make_response
from models.store import Store
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
                'store-id' : store.id,
                'store-name' : store.name,
                'store-email' : store.email,
                'store-profile-image' : store.profile_image,
                'store-logo' : store.logo,
                'store-category' : store.category,
                'coupons' : [
                    {
                        'coupon-id' : coupon.id,
                        'coupon-name' : coupon.name,
                        'coupon-deal' : coupon.value,
                        'coupon-points' : coupon.cost,
                    } for coupon in store.coupons
                ]
            }
            result.append(store_data)
        return jsonify({'stores' : result})
    else:
        return jsonify({'message' : 'category not found'})


