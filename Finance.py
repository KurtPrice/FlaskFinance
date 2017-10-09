from flask import Flask
from flask_bootstrap import Bootstrap
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

    app.run()
