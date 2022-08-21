from flask import Blueprint, flash, request, render_template, redirect, url_for, abort
from flask_login import login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length, Email
from passlib.hash import sha256_crypt
from urllib.parse import urlparse, urljoin

from models import User


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


bp = Blueprint('bp_auth', __name__, template_folder='templates')


# Login page
@bp.route('/login', methods=['GET', 'POST'])
def login():

    class LoginForm(FlaskForm):
        email = StringField('Email', validators=[InputRequired(), Length(max=255), Email()])
        password = StringField('Hasło', validators=[InputRequired()])

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)

        if user and sha256_crypt.verify(form.password.data, user.password):
            login_user(user)
            flash('Zalogowano')

            return redirect(url_for('bp_account.get', account_id=user.account_id, currency_name= 'pln'))
        else:
            flash('Nieprawidłowe dane logowania')
            return render_template('login.html', form=form)

    elif form.is_submitted():
        for field_name, errors in form.errors.items():
            for err in errors:
                flash(f"{form._fields[field_name].label.text}: {err}", 'error')

    return render_template('login.html', form=form)


# Logout
@bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('bp_home.get'))
