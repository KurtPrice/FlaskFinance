from flask_wtf import FlaskForm
from wtforms import SelectField, FormField, FieldList, TextField
from wtforms.validators import DataRequired


class CardsForm(FlaskForm):
    # Must package into tuples of two to prevent unpacking errors
    cards_list = [('CSR', 'Chase Sapphire Reserved'), ('CF', 'Chase Freedom'), ('CFU', 'Chase Freedom Unlimited'),
                  ('BN', 'Barnes & Noble'), ('BKL', 'Buckle'), ('AZN', 'Amazon')]

    cards_selector = SelectField('cards selects', choices=cards_list, validators=[DataRequired])
