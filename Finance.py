from flask import Flask
from flask_bootstrap import Bootstrap
from blueprints import login_blueprint

app = Flask(__name__)
site_name = "Finance Site"


if __name__ == '__main__':
    Bootstrap(app)
    app.session_cookie_name = site_name
    app.secret_key = "SDGLKJGTHKLS*%(@#$J(SGS*(&GSJK(*GJSLKJT(*W646549845646546549874"
    app.register_blueprint(login_blueprint.login_bp)
    app.config['DEBUG'] = True
    app.config['WTF_CSRF_ENABLED'] = True
    app.run()
