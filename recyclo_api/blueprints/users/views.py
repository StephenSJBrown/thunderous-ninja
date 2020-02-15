from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify, make_response
from models.user import User
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')

@users_blueprint.route('/',methods=['GET'])
def index():
    users = User.select()
    result = []

    for user in users:
        user_data = {
            'id' : user.id,
            'username' : user.username,
            'email' : user.email
        }
        result.append(user_data)
    return jsonify({'users' : result}), 200


@users_blueprint.route('/id', methods=['GET'])
def show(username):
    user = User.get_or_none(User.id == id)

    if user:
        return jsonify({
            'id' : user.id,
            'username' : user.username,
            'email' : user.email,
            'contact' : user.contact,
            'points' : user.points,
            'profile_image' : user.profile_image,
            'background_image' : user.background_image
#image in static/images, but no idea how to link this.
            }), 200
    else:
        return jsonify({'message' : 'user not found'}), 418


@users_blueprint.route('/',methods=['POST'])
def create():
    user = request.get_json()
    if not user['password'] == user['cfm_pwd']:
        return jsonify({'message' : 'password confirmation does not match'}), 418

    new_user = User(
        username=user['username'], 
        password=user['password'],
        email=user['email'], 
        )
    if new_user.save():
        return jsonify({
            'message' : 'new user created!',
            'status' : 'success',
            'new_user' : {
                'id' : new_user.id,
                'username' : new_user.username,
                'email' : new_user.email
                },
            }), 200
    else:
        er_msg = []
        for error in new_user.errors:
            er_msg.append(error)
        return jsonify({'message' : er_msg}), 418


@users_blueprint.route('/<user_id>',methods=['PUT'])
@login_required
def update(user_id):
    user = User.get_by_id(user_id)

    if not current_user == user:
        return jsonify({'message' : 'unauthorized access'}), 418

    update = request.get_json()

    if update['username'] != '':
        user.username = update['username']
        user.password = None
    if update['email'] != '':
        user.email = update['email']
        user.password = None
    if update['contact'] != '':
        user.contact = update['contact']
        user.password = None
    if update['password'] != '':
        user.password = update['password']
    if user.save():
        return jsonify({
            'message' : 'successfully updated profile',
            'status' : 'success',
            'updated_user' : {
                'id' : user.id,
                'username' : user.username,
                'email' : user.email,
                'contact' : user.contact,
                'profile_image' : user.profile_image,
                },
            }), 200
    else:
        er_msg = []
        for error in user.errors:
            er_msg.append(error)
        return jsonify({'message' : er_msg}), 418

# @users_blueprint.route('/<user_id>/points',methods=['GET'])
# @login_required
# def view_points(user_id):
#     user = User.get_by_id(user_id)

#     if user:
#         if not current_user == user:
#             return jsonify({'message' : 'unauthorized access'})
    
#         return jsonify({'points' : user.points})
#     else:
#         return make_response({'message' : 'user unavailable'})


# @users_blueprint.route('/signup', methods=['GET'])
# def new():
#     return render_template('users/new.html')

# @users_blueprint.route('/', methods=['POST'])
# def create():
#     username = request.form.get('username')
#     email = request.form.get('email')
#     password = request.form.get('password')
#     pwd_cfm = request.form.get('pwd_cfm')

#     if password == pwd_cfm:
#         user = User(username=username, 
#                     email=email, 
#                     password=password)
#         if user.save():
#             flash(f'Welcome {user.username}, thanks for signing up!','alert alert-success')
#             return redirect(url_for('home'))
#         else:
#             for error in user.errors:
#                 flash(error,'alert alert-danger')
#             return render_template('users/new.html')
#     else:
#         flash('Password confirmation does not match.','alert alert-danger')
#         return render_template('users/new.html')
    
# @users_blueprint.route('/<username>', methods=['GET'])
# def show(username):
#     user = User.get_or_none(User.username == username)
#     if user:
#         if current_user.is_authenticated:
#             return render_template('users/show.html',user=user)
#         else:
#             flash('Login required.','alert alert-danger')
#             return render_template('sessions/new.html')
#     else:
#         return render_template('404.html')


# @users_blueprint.route('/edit/<id>',methods=['GET'])
# def edit(id):
#     user = User.get_or_none(User.id == current_user.id)
#     if user:
#         if current_user.is_authenticated:
#             return render_template('users/edit.html')
#         else:
#             flash('Unauthorized to edit','alert alert-danger')
#             return render_template(url_for('users.show',username=current_user.username))
#     else:
#         return render_template('404.html')
        

# @users_blueprint.route('/update/<id>',methods=['POST'])
# def update(id):
#     user = User.get_by_id(id)
#     username = request.form.get('username')
#     email = request.form.get('email')
#     contact = request.form.get('contact')
#     password = request.form.get('password')

#     if username != '':
#         user.username = username
#         user.password = None
#     if email != '':
#         user.email = email
#         user.password = None
#     if contact != '':
#         user.contact = contact
#         user.password = None
#     if password != '':
#         user.password = password
#     if user.save():
#         flash('Profile updated successfully!','alert alert-success')
#         return redirect(url_for('users.show',username=current_user.username))
#     else:
#         for error in user.errors:
#             flash(error,'alert alert-danger')
#         return redirect(url_for('home'))

    