from flask import Blueprint, flash, request, render_template, redirect, url_for
from flask_login import login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length, Email
from passlib.hash import sha256_crypt

from models import User

bp = Blueprint('bp_auth', __name__, template_folder='templates')

# next


# Login page
@bp.route('/login', methods=['GET', 'POST'])
def login():

    class LoginForm(FlaskForm):
        email = StringField('Email', validators=[InputRequired(), Length(max=255), Email()])
        password = StringField('Hasło', validators=[InputRequired()])

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and sha256_crypt.verify(form.password.data, user.password):
            login_user(user)
            flash('Zalogowano')

            return redirect(url_for('bp_account.get', account_id=user.account_id))
        else:
            flash('Nieprawidłowe dane logowania')
            return render_template('login.html', form=form)

        # next = request.args.get('next')
        # if not is_safe_url(next):
        #     return flask.abort(400)

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
