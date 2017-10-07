from flask import render_template, redirect, url_for
from forms.login import LoginForm
from views.view import index
from Finance import site_name


def login():
    """
    retrieves username and password from POST
    :return:
    """
    form = LoginForm()
    print(form.username)
    print(form.password)
    if form.validate_on_submit():
        return render_template('profile.html', name=site_name)
    return redirect(url_for(index))
