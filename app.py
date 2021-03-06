import os
import click
import config
from flask import Flask
from models.base_model import db
from models.user import User
from flask_login import LoginManager

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'recyclo_api')

app = Flask('RECYCLO', root_path=web_dir)
app.config['JSON_SORT_KEYS'] = False

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc

@click.command()
def seed():
    from seed import seed_users
    seed_users()

app.cli.add_command(seed)