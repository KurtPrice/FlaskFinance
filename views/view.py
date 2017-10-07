from flask import request, flash, url_for, render_template
from Finance import site_name


def index():
    return render_template('index.html',
                           name=site_name)