from flask import Blueprint, render_template, abort
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, Regexp

from models import SubAccount, Currency

bp = Blueprint('bp_exchange', __name__, template_folder='templates')


@bp.route('/exchange/<account_id>', methods=['GET', 'POST'])
def get(account_id=0):

    if account_id == 0:
        abort(404)

    # dynamiczne pole select (jak wybrana jedna waluta, to w drugim do wyboru inne, poza tą wybraną)
    # walidator dostępnej kwoty...
    # dynamicznie zmieniające sie pole value_to w zależności od wpisanej kwoty value_from

    sub_accounts = SubAccount.query.filter_by(account_id=account_id).all()
    currencies = []
    for sa in sub_accounts:
        currencies.append(Currency.query.filter_by(id=sa.currency_id).first())

    currency_names = [c.name for c in currencies]

    class ExchangeForm(FlaskForm):
        currency_from = SelectField('Z', validators=[InputRequired()], choices=currency_names)
        currency_to = SelectField('Na', validators=[InputRequired()], choices=currency_names)
        value_from = StringField('Wartość przed', validators=[InputRequired()])
        value_to = StringField('Wartość po', render_kw={'readonly': True}, validators=[Regexp(r'^[0-9.]*$')])

    form = ExchangeForm()
    form.value_from.data = '0.0'
    form.value_to.data = '0.0'

    if form.validate_on_submit():
        pass
    elif form.is_submitted():
        pass

    return render_template('currency_exchange.html', form=form)


def rest_currencies():
    pass
