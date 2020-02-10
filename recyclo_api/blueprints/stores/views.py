from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify, make_response
from models.store import Store
stores_blueprint = Blueprint('stores',
                            __name__,
                            template_folder='templates')

@stores_blueprint.route('/<category>',methods=['GET'])
def index(category):
    stores = Store.select().where(Store.category==category)
    result = []

    for store in stores:
        store_data = {
            'store-id' : store.id,
            'store-name' : store.name,
            'store-email' : store.email,
            'store-profile-image' : store.profile_image,
            'store-logo' : store.logo,
            'store-category' : store.category
        }
        result.append(store_data)
    return jsonify({'stores' : result})



