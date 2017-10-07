from flask import Blueprint
import Finance

login_bp = Blueprint('login',
                     __name__,
                     static_folder='../static',
                     template_folder='../templates')

# Register users to view methods --Kurtpr
login_bp.add_url_rule('/', 'index', Finance.index)
