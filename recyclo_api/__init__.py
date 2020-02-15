from app import app
from flask import render_template
from recyclo_api.blueprints.users.views import users_blueprint
from recyclo_api.blueprints.sessions.views import sessions_blueprint
from recyclo_api.blueprints.deposits.views import deposits_blueprint
from recyclo_api.blueprints.purchases.views import purchases_blueprint
from recyclo_api.blueprints.stores.views import stores_blueprint
from recyclo_api.blueprints.coupons.views import coupons_blueprint
from recyclo_api.blueprints.centres.views import centres_blueprint


from flask_assets import Environment, Bundle
from .util.assets import bundles
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/api/users")
app.register_blueprint(sessions_blueprint, url_prefix="/api")
app.register_blueprint(deposits_blueprint, url_prefix="/api/deposits")
app.register_blueprint(purchases_blueprint, url_prefix="/api/purchases")
app.register_blueprint(stores_blueprint, url_prefix="/api/stores")
app.register_blueprint(coupons_blueprint, url_prefix="/api/coupons")
app.register_blueprint(centres_blueprint, url_prefix="/api/centres")



@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def home():
    return render_template('home.html')