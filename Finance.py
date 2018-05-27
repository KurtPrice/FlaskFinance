from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from blueprints import login_blueprint
from database import create_database

app = Flask(__name__)
site_name = "Finance Site"
card_col = create_database("finance")
card_col = card_col["cards"]
card_list = card_col.find()
cards_dict = {post["card"]: post["full_name"] for post in card_list}


if __name__ == '__main__':
    Bootstrap(app)
    app.register_blueprint(login_blueprint.login_bp)

    app.jinja_env.auto_reload = True
    app.config.update(
        DEBUG=True,
        SECRET_KEY="that's-a-spicyah-meatball",
        SESSION_COOKIE_NAME=site_name,
        TEMPLATES_AUTO_RELOAD=True
    )

    lm = LoginManager()
    lm.init_app(app)

    app.run()
