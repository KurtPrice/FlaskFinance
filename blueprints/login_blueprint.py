from flask import Blueprint
from views import view, login

login_bp = Blueprint('login',
                     __name__,
                     static_folder='../static',
                     template_folder='../templates')

# Register users to view methods --Kurtpr
login_bp.add_url_rule('/', 'index', view.index)
login_bp.add_url_rule('/login', 'login', login.login, methods=['GET', 'POST'])
login_bp.add_url_rule('/cards', 'cards', view.cards, methods=['GET', 'POST'])
login_bp.add_url_rule('/benefits', 'benefits', view.cards, methods=['GET', 'POST'])
login_bp.add_url_rule('/logout', 'logout', login.logout, methods=['POST'])
