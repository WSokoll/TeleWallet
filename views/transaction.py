from datetime import datetime

from flask import Blueprint, render_template, abort, redirect, url_for, flash
from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import InputRequired, Length, Regexp

from app import db
from models import Currency, SubAccount, InternalTransaction, User
from validators import ValueVSOwnedValidator, UserExistsValidator

bp = Blueprint('bp_transaction', __name__, template_folder='templates')

# TODO: transactions (database)


# Internal transaction page
@bp.route('/transaction/internal/<account_id>/<string:currency_name>', methods=['GET', 'POST'])
@login_required
def get_post_internal(account_id=0, currency_name='pl'):
    currencies = Currency.query.order_by(Currency.name).all()

    if account_id == 0 or currency_name not in [c.name for c in currencies]:
        abort(404)

    class InternalTransactionForm(FlaskForm):
        username_from = StringField('Nadawca', validators=[InputRequired(), Length(max=255)], render_kw={'readonly': True})
        username_to = StringField('Odbiorca', validators=[InputRequired(), Length(max=255), UserExistsValidator()], render_kw={'placeholder': 'Imię Nazwisko'})
        title = StringField('Tytuł przelewu', validators=[Length(max=255)])
        value = StringField('Kwota przelewu', validators=[InputRequired(), ValueVSOwnedValidator()])
        owned_value = HiddenField()

    currency = Currency.query.filter_by(name=currency_name).first()
    sub_account_from = SubAccount.query.filter_by(account_id=account_id, currency_id=currency.id).first()
    user_from = User.query.filter_by(account_id=account_id).first()

    form = InternalTransactionForm()
    form.username_from.data = user_from.name
    form.owned_value.data = str(sub_account_from.balance)

    if form.validate_on_submit():

        user_to = User.query.filter_by(name=form.username_to.data).first()
        sub_accounts_to = SubAccount.query.filter_by(account_id=user_to.account_id).all()

        # check if user has sub-account in given currency
        if currency.id in [sa.currency_id for sa in sub_accounts_to]:
            sub_account_to = SubAccount.query.filter_by(account_id=user_to.account_id, currency_id=currency.id).first()
            value_to = float(form.value.data)
        else:
            sub_account_to = SubAccount.query.filter_by(account_id=user_to.account_id, currency_id=1).first()
            value_to = float(form.value.data) * currency.exchange_rate

        transaction = InternalTransaction(transaction_from=user_from.id,
                                          transaction_to=user_to.id,
                                          currency_id=currency.id,
                                          value=float(form.value.data),
                                          transaction_date=datetime.now(),
                                          name=form.title.data)

        sub_account_from.balance = float(sub_account_from.balance) - float(form.value.data)
        sub_account_to.balance = float(sub_account_to.balance) + value_to

        db.session.add(transaction)
        db.session.commit()

        flash('Tranzakcja zakończona sukcesem.')
        return redirect(url_for('bp_account.get', account_id=account_id, currency_name=currency_name))

    elif form.is_submitted():
        for field_name, errors in form.errors.items():
            for err in errors:
                flash(f"{form._fields[field_name].label.text}: {err}", 'error')

    return render_template('internal_transaction.html', currency=currency, sub_account=sub_account_from, form=form)
