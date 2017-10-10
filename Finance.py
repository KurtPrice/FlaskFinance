from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from blueprints import login_blueprint

app = Flask(__name__)
site_name = "Finance Site"


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
