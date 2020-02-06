from flask import Blueprint, render_template, redirect, request, url_for, flash
from models.user import User

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')

@users_blueprint.route('/signup', methods=['GET'])
def new():
    return render_template('users/new.html')

@users_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    pwd_cfm = request.form.get('pwd_cfm')

    if password == pwd_cfm:
        user = User(username=username, 
                    email=email, 
                    password=password)
        if user.save():
            flash(f'Welcome {user.username}, thanks for signing up!','alert alert-success')
            return redirect(url_for('home'))
        else:
            for error in user.errors:
                flash(error,'alert alert-danger')
            return render_template('users/new.html')
    else:
        flash('Password confirmation does not match.','alert alert-danger')
        return render_template('users/new.html')
    
