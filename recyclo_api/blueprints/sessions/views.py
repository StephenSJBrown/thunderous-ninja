from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

sessions_blueprint = Blueprint('sessions',
                                __name__,
                                template_folder='templates')

@sessions_blueprint.route('/login', methods=['GET'])
def new():
    return render_template('sessions/new.html')

@sessions_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    user = User.get_or_none(User.username == username)

    if user != None:
        password = request.form.get('password')
        result = check_password_hash(user.password, password)
        if result == True:
            login_user(user)
            flash(f'Welcome {username}!','alert alert-success')
            return redirect(url_for('home'))
        else:
            flash('Credentials do not match our records.','alert alert-danger')
            return render_template('sessions/new.html')
    else:
        flash('Credentials do not match our records.','alert alert-danger')
        return render_template('sessions/new.html')

@sessions_blueprint.route('/logout')
def destroy():
    logout_user()
    flash('succesfully logged out','alert alert-success')
    return redirect(url_for('sessions.new'))