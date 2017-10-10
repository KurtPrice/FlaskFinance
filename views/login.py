from flask import render_template, redirect, url_for, request
from flask_login import login_manager, logout_user
from forms.login import LoginForm
from Finance import site_name


def login():
    """
    retrieves username and password from POST
    :return:
    """
    form = LoginForm(request.form)
    print(form.username.data)
    print(form.password.data)
    if form.validate_on_submit():
        return render_template('profile.html', name=site_name, form=form)
    return render_template('index.html', name=site_name, form=form)


def logout():
    pass