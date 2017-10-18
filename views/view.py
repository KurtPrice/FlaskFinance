import json
from flask import request, flash, url_for, render_template
from forms.login import LoginForm
from forms.calculators import CardsForm
from Finance import site_name


def index():
    form = LoginForm()
    return render_template('index.html',
                           name=site_name,
                           form=form)


def cards():
    form = CardsForm()
    json_cards = request.args.get('card_list')
    if json_cards is not None:
        card_list = json.loads(json_cards)

    return render_template('cards.html',
                           name=site_name,
                           form=form)
