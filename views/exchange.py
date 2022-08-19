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

    # TODO:  walidator dostępnej kwoty...(jakoś we froncie? z wykożystaniem sub_accounts i currencies)
    # TODO: dynamicznie zmieniające sie pole value_to w zależności od wpisanej kwoty value_from

    sub_accounts = SubAccount.query.filter_by(account_id=account_id).all()
    currencies = []
    for sa in sub_accounts:
        currencies.append(Currency.query.filter_by(id=sa.currency_id).first())

    currency_names = [c.name for c in currencies]

    class ExchangeForm(FlaskForm):
        currency_from = SelectField('Z', validators=[InputRequired()], choices=currency_names)
        currency_to = SelectField('Na', validators=[InputRequired()], choices=currency_names)
        value_from = StringField('Wartość przed', validators=[InputRequired(), Regexp(r'^[0-9.]*$')])
        value_to = StringField('Wartość po', render_kw={'readonly': True}, validators=[Regexp(r'^[0-9.]*$')])

    form = ExchangeForm()
    form.value_from.data = '0.0'
    form.value_to.data = '0.0'

    if form.validate_on_submit():
        currency_from = Currency.query.filter_by(name=form.currency_from.data).first()
        currency_to = Currency.query.filter_by(name=form.currency_to.data).first()

        sub_account_from = SubAccount.query.filter_by(account_id=account_id, currency_id=currency_from.id)
        sub_account_to = SubAccount.query.filter_by(account_id=account_id, currency_id=currency_to.id)

        value_to = float(form.value_from.data) * currency_from.exchange_rate * currency_to.exchange_rate

        # will it work (current_user.id)????
        exchange = CurrencyExchange(user_id=current_user.id,
                                    currency_from=currency_from.id,
                                    currency_to=currency_to.id,
                                    value_old=float(form.value_from.data),
                                    value_new=value_to)

        with db.session.begin():
            sub_account_from.balance = sub_account_from.balance - float(form.value_from.data)
            sub_account_to.balance = sub_account_to.balance + value_to

            db.session.add(exchange)

        flash('Wymiana zakończona sukcesem.')
        return redirect(url_for('bp_account.get', account_id=account_id, currency_name='pl'))

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
