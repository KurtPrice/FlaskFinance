import json
from database import create_database
from flask import request, render_template, redirect
from forms.login import LoginForm
from forms.calculators import CardsForm
from Finance import site_name, cards_dict


def index():
    form = LoginForm()
    return render_template('index.html',
                           name=site_name,
                           form=form)


def benefits_page():
    form = LoginForm()
    json_cards = request.form.get('card_list')
    benefits = []
    benefit_categories = {}
    card_count = 0
    # if credit cards have been collected
    if json_cards is not None:
        cards_list = json.loads(json_cards)
        reverse_card_dict = dict((v, k) for k, v in cards_dict.items())

        # Access the finance site database and the cards collection!
        finance_db = create_database("finance")
        card_col = finance_db['cards']

        # Retrieve the benefits and cards from the database as selected by the user.
        card_count = len(cards_list)
        for card in cards_list:
            card_abbr = reverse_card_dict[card.replace("&amp;", "&")]  # hotfix for B&N card.
            benefits.append(card_col.find_one({'card': card_abbr}))
        for benefit in benefits:
            categories = benefit['benefits'].keys()
            for category in categories:
                if benefit_categories.get(category, 0) == 0:
                    benefit_categories[category] = 1
                else:
                    benefit_categories[category] += 1

    return render_template('benefits.html',
                           name=site_name,
                           form=form,
                           benefits=benefit_categories.keys(),
                           counts=benefit_categories,
                           total=card_count)


def cards_page():
    form = LoginForm()
    card_form = CardsForm()

    return render_template('cards.html',
                           name=site_name,
                           form=form,
                           card_form=card_form)
