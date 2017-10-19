from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from blueprints import login_blueprint

app = Flask(__name__)
site_name = "Finance Site"
cards_dict = {'CSR': 'Chase Sapphire Reserve', 'CF': 'Chase Freedom', 'CFU': 'Chase Freedom Unlimited',
              'BN': 'Barnes & Noble', 'BKL': 'Buckle', 'AZN': 'Amazon', 'CSP': 'Chase Sapphire Preferred'}


if __name__ == '__main__':
    Bootstrap(app)
    app.register_blueprint(login_blueprint.login_bp)

    app.config.update(
        DEBUG=True,
        SECRET_KEY="that's-a-spicyah-meatball",
        SESSION_COOKIE_NAME=site_name
    )

    lm = LoginManager()
    lm.init_app(app)

    app.run()
