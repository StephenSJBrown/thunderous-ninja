from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from models.user import User, Deposit
from models.centre import Centre
from flask_login import current_user, login_manager

deposits_blueprint = Blueprint('deposits',
                            __name__,
                            template_folder='templates')


@deposits_blueprint.route('/create', methods=['POST'])
def create():
    centre = request.form.get('centre')
    print(centre) # None
    centre = Centre.get_by_id(centre)
    user = request.form.get('user')
    user = User.get_by_id(user)
    weight = request.form.get('weight')
    points = weight*100


    new_deposit = Deposit(user=user, centre=centre, weight=weight, points=points)
    new_deposit.save()

    user.update(points=User.points + points) 
    
    return jsonify({'centre':centre.name,
                   'weight':new_deposit.weight,
                   'points':points})

@deposits_blueprint.route('/show/<id>')
def show(id):
    user = User.get_by_id(id)

    # user = User.get_by_id(1)
    deposits = user.deposits


    return jsonify([{
                'date':deposit.created_at,
                'centre':deposit.centre.id,
                'weight':deposit.weight,
                'points':deposit.points} for deposit in deposits
    ]), 200

    # else:
    #     return jsonify([{
    #             'date':deposit.created_at,
    #             'centre':deposit.centre.id,
    #             'weight':deposit.weight,
    #             'points':deposit.points} for deposit in deposits
    #     ]), 418
