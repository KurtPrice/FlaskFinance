from flask_wtf import FlaskForm
from Finance import cards_dict
from wtforms import SelectField
from wtforms.validators import DataRequired


class CardsForm(FlaskForm):
    # Must package into tuples of two to prevent unpacking errors
    cards_list = cards_dict.items()

    cards_selector = SelectField('cards selects', choices=cards_list, validators=[DataRequired])
