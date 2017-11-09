import json
from database import create_database
from flask import request, render_template, redirect
from forms.login import LoginForm
from forms.calculators import CardsForm
from Finance import site_name, cards_dict
import Finance


def index():
    form = LoginForm()
    return render_template('index.html',
                           name=site_name,
                           form=form)


def cards():
    form = CardsForm()
    json_cards = request.form.get('card_list')
    benefits = []
    # If credit cards have been collected
    if json_cards is not None:
        print("GETEM")
        card_list = json.loads(json_cards)
        reverse_card_dict = dict((v, k) for k, v in cards_dict.items())

        # Access the finance site database and the cards collection!
        finance_db = create_database("finance")
        card_col = finance_db['cards']

        # Retrieve the benefits and cards from the database as selected by the user.
        for card in card_list:
            card_abbr = reverse_card_dict[card.replace("&amp;", "&")]  # hotfix for B&N card.
            benefits.append(card_col.find_one({'card': card_abbr}))

    return render_template('cards.html',
                           name=site_name,
                           form=form,
                           benefits=benefits)
