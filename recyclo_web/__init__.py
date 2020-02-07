from app import app
from flask import render_template
from recyclo_web.blueprints.users.views import users_blueprint
<<<<<<< HEAD
from recyclo_web.blueprints.sessions.views import sessions_blueprint
=======
from recyclo_web.blueprints.deposits.views import deposits_blueprint
>>>>>>> 0a5e0456b76a5f43e098b0c8645bf1a4ae0c730a
from flask_assets import Environment, Bundle
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")
<<<<<<< HEAD
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")
=======
app.register_blueprint(deposits_blueprint, url_prefix="/deposits")
>>>>>>> 0a5e0456b76a5f43e098b0c8645bf1a4ae0c730a

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def home():
    return render_template('home.html')