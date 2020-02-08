from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from models.user import User
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')

@users_blueprint.route('/',methods=['GET'])
def get_all_users():
    return ''

@users_blueprint.route('/<user_id>', methods=['GET'])
def get_one_user():
    return ''

@users_blueprint.route('/',methods=['POST'])
def create_user():
    user = request.get_json()
    new_user = User(
        username=user['username'], 
        password=user['password'],
        email=user['email'], 
        )

    if new_user.save():
        return jsonify({
            'message' : 'new user created!',
            'status' : 'success',
            'user' : {
                'id' : new_user.id,
                'username' : new_user.username,
                'email' : new_user.email
                },
            })
    else:
        er_msg = []
        for error in new_user.errors:
            er_msg.append(error)
        return jsonify({'message' : er_msg})


@users_blueprint.route('/<user_id>',methods=['PUT'])
def update_user():
    return ''






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

    