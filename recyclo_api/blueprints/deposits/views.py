from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from models.user import User, Deposit
from models.centre import Centre
from flask_login import login_manager

deposits_blueprint = Blueprint('deposits',
                            __name__,
                            template_folder='templates')

#records transaction of trash between user and centre, also updates user's points
@deposits_blueprint.route('/create/<centre_id>', methods=['POST'])
def create(centre_id):
    auth = request.get_json()
    centre = Centre.get_or_none(Centre.id == centre_id)
    if centre:
        user = User.get_or_none(User.id == auth['user_id'])
        if user:
            record_user = Deposit(
                user_id=user.id,
                centre_id=centre.id
            )
            record_user.save()
        
            return jsonify({
                'message' : 'entry created',
                'date' : record_user.created_at,
                'id' : record_user.id,
                'weight' : record_user.weight,
                'points_awarded' : record_user.points,
                'user' : {
                    'id' : user.id,
                    'username' : user.username,
                    'email' : user.email,
                    'contact' : user.contact,
                    'points_total' : user.points
                },
                'centre' : {
                    'id' : centre.id,
                    'name' : centre.name,
                    'location' : centre.location
                }
                })

        else:
            return jsonify({'message' : 'user not found'})
    else:
        return jsonify({'message' : 'centre not found'})


#gets weight from rashberryPi and updates the latest entry of the centre.
@deposits_blueprint.route('/update/<centre_id>', methods=['POST'])
def update(centre_id):
    get_weight = request.get_json()
    weight = get_weight['weight']
    points = get_weight['weight'] * 100
    deposit = Deposit.select().order_by(Deposit.id.desc()).where(Deposit.centre_id == centre_id).get()

    if deposit.weight == 0.00:
        Deposit.update(weight=weight,points=points).where(Deposit.id == deposit.id).execute()
        deposit = Deposit.get_by_id(deposit)

        user = User.get_or_none(deposit.user_id == User.id)
        User.update(points=user.points+deposit.points).where(User.id == user.id).execute()
        user = User.get_by_id(user)
        return jsonify({
            'message':'weight recorded.',
            'id' : deposit.id,
            'weight' : weight,
            'points' : points,
            'user' : {
                'id' : user.id,
                'username' : user.username,
                'email' : user.email,
                'contact' : user.contact,
                'points_total' : user.points
            }
            })
    else:
        return jsonify({'message' : 'can\'t record weight, this user already recorded a weight.'})


#shows all deposits based on user
@deposits_blueprint.route('/index/<user_id>', methods=['GET'])
def index(user_id):
    user = User.get_or_none(User.id == user_id)

    if user:
        deposits = user.deposits
        return jsonify([{
            'date':deposit.created_at,
            'id' : deposit.id,
            'centre_id':deposit.centre.id,
            'weight':deposit.weight,
            'points':deposit.points
            } for deposit in deposits
    ]), 200

    else:
        return jsonify([{'message' : 'user not found'}]), 418


@deposits_blueprint.route('/<deposit_id>', methods=['GET'])
def show(deposit_id):
    deposit = Deposit.get_or_none(Deposit.id == deposit_id)

    if deposit:
        return jsonify({
            'date' : deposit.created_at,
            'id' : deposit.id,
            'user_id' : deposit.user_id,
            'centre_id':deposit.centre_id,
            'weight':deposit.weight,
            'points':deposit.points
        })
    else:
        return jsonify({'message' : 'deposit unavailable'})