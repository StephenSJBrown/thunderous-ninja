from app import app
from flask import render_template
from recyclo_api.blueprints.users.views import users_blueprint
from recyclo_api.blueprints.sessions.views import sessions_blueprint
from recyclo_api.blueprints.deposits.views import deposits_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")
app.register_blueprint(deposits_blueprint, url_prefix="/deposits")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def home():
    return render_template('home.html')