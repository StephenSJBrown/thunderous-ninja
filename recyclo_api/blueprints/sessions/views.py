from flask import Blueprint, render_template, redirect, request, url_for, flash, session, jsonify, make_response
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

sessions_blueprint = Blueprint('sessions',
                                __name__,
                                template_folder='templates')


@sessions_blueprint.route('/login', methods=['POST'])
def login():
    login = request.get_json()
    user = User.get_or_none(User.username == login['username'])
    if user != None:
        result = check_password_hash(user.password, login['password'])
        if result == True:
            login_user(user)
            return jsonify({
                'message' : 'logged in succesful',
                'status' : 'success',
                'user' : {
                    'id' : user.id,
                    'username' : user.username,
                    'email' : user.email
                    }
                })
        else:
            return jsonify({
                'message' : 'incorrect password',
                'status' : 'failed'
                })
    else:
        return jsonify({'message' : 'incorrect username and password'})


@sessions_blueprint.route('/logout')
def logout():
    logout_user()
    print('message : logout succesful')
    return render_template('home.html')






# @sessions_blueprint.route('/login', methods=['GET'])
# def new():
#     return render_template('sessions/new.html')

# @sessions_blueprint.route('/', methods=['POST'])
# def create():
#     username = request.form.get('username')
#     user = User.get_or_none(User.username == username)

#     if user != None:
#         password = request.form.get('password')
#         result = check_password_hash(user.password, password)
#         if result == True:
#             login_user(user)
#             flash(f'Welcome {username}!','alert alert-success')
#             return redirect(url_for('home'))
#         else:
#             flash('Credentials do not match our records.','alert alert-danger')
#             return render_template('sessions/new.html')
#     else:
#         flash('Credentials do not match our records.','alert alert-danger')
#         return render_template('sessions/new.html')

# @sessions_blueprint.route('/logout')
# def destroy():
#     logout_user()
#     flash('succesfully logged out','alert alert-success')
#     return redirect(url_for('sessions.new'))