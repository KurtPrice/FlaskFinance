from flask import Flask, request, flash, url_for, render_template
from blueprints import login_blueprint

app = Flask(__name__)
site_name = "Finance Site"


def index():
    print("WTF")
    return render_template('index.html',
                           name=site_name)


if __name__ == '__main__':
    app.session_cookie_name = site_name
    app.register_blueprint(login_blueprint.login_bp)
    app.run()
