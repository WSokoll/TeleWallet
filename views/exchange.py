from datetime import datetime

from flask import Blueprint, render_template, abort, flash, redirect, url_for, jsonify
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, Regexp

from app import db
from models import SubAccount, Currency, CurrencyExchange

bp = Blueprint('bp_exchange', __name__, template_folder='templates')


@bp.route('/exchange/<account_id>', methods=['GET', 'POST'])
@login_required
def get_post(account_id=0):

    if account_id == 0:
        abort(404)

    sub_accounts = SubAccount.query.filter_by(account_id=account_id).all()
    currencies = []
    for sa in sub_accounts:
        currencies.append(Currency.query.filter_by(id=sa.currency_id).first())

    currency_names = [c.name for c in currencies]

    class ExchangeForm(FlaskForm):
        currency_from = SelectField('Waluta źródłowa:', validators=[InputRequired()], choices=currency_names)
        currency_to = SelectField('Waluta docelowa', validators=[InputRequired()], choices=currency_names)
        value_from = StringField('Wartość przed wymianą', validators=[InputRequired(), Regexp(r'^[0-9.]*$')])
        value_to = StringField('Wartość po wymianie', render_kw={'readonly': True}, validators=[Regexp(r'^[0-9.]*$')])

    form = ExchangeForm()

    if form.validate_on_submit():
        currency_from = Currency.query.filter_by(name=form.currency_from.data.lower()).first()
        currency_to = Currency.query.filter_by(name=form.currency_to.data.lower()).first()

        sub_account_from = SubAccount.query.filter_by(account_id=account_id, currency_id=currency_from.id).first()
        sub_account_to = SubAccount.query.filter_by(account_id=account_id, currency_id=currency_to.id).first()

        if float(form.value_from.data) > sub_account_from.balance:
            flash('Nie posiadasz wystarczających środków.')
            return render_template('currency_exchange.html', form=form, sub_accounts=sub_accounts, currencies=currencies)

        exchange = CurrencyExchange(user_id=current_user.id,
                                    currency_from=currency_from.id,
                                    currency_to=currency_to.id,
                                    value_old=float(form.value_from.data),
                                    value_new=float(form.value_to.data),
                                    exchange_date=datetime.now())

        sub_account_from.balance = sub_account_from.balance - float(form.value_from.data)
        sub_account_to.balance = sub_account_to.balance + float(form.value_to.data)

        db.session.add(exchange)
        db.session.commit()

        flash('Wymiana zakończona sukcesem.')
        return redirect(url_for('bp_account.get', account_id=account_id, currency_name='pln'))

    elif form.is_submitted():
        for field_name, errors in form.errors.items():
            for err in errors:
                flash(f"{form._fields[field_name].label.text}: {err}", 'error')

    return render_template('currency_exchange.html', form=form, sub_accounts=sub_accounts, currencies=currencies)


@bp.route('/exchange/<account_id>/<currency_name>/other')
@login_required
def rest_currencies(account_id=0, currency_name=''):
    if account_id == 0 or currency_name == '':
        abort(404)

    sub_accounts = SubAccount.query.filter_by(account_id=account_id).all()
    currencies = []
    for sa in sub_accounts:
        currencies.append(Currency.query.filter_by(id=sa.currency_id).first())

    return jsonify({'other': [c.name for c in currencies if c.name != currency_name]})


@bp.route('/exchange/<currency_from_name>/<currency_to_name>/<value_from>')
@login_required
def value_to(currency_from_name='pln', currency_to_name='pln', value_from=''):
    if value_from == '':
        abort(404)

    currency_from = Currency.query.filter_by(name=currency_from_name).first()
    currency_to = Currency.query.filter_by(name=currency_to_name).first()

    if not currency_from or not currency_to:
        abort(404)

    value_to = round(float(value_from) * currency_from.exchange_rate / currency_to.exchange_rate, 2)

    return jsonify({'value_to': value_to})
