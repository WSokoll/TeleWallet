from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Length, Regexp

from models import Currency, SubAccount, InternalTransaction

bp = Blueprint('bp_transaction', __name__, template_folder='templates')


# Show internal transaction page
@bp.route('/transaction/internal/<account_id>/<string:currency_name>', methods=['GET'])
def get_internal_transaction(account_id=0, currency_name='pl'):

    # 404...
    # if id == 0:
    #     return

    # NAPISAĆ WALIDATOR SPRAWDZAJĄCY CZY KTOŚ WPISANĄ KWOTĄ DYSPONUJE... + kwestia czy druga osoba istnieje i ma subkonto w danej walucie
    class InternalTransactionForm(FlaskForm):
        username_from = StringField('Od', validators=[InputRequired(), Length(max=255)], render_kw={'readonly': True})
        username_to = StringField('Do', validators=[InputRequired(), Length(max=255)])
        title = StringField('Tytuł', validators=[Length(max=255)])
        value = TextAreaField('Kwota przelewu', validators=[InputRequired(), Regexp(r'^[0-9,.]*$')])

    currency = Currency.query.get_or_404(name=currency_name)
    sub_account = SubAccount.query.get_or_404(account_id=id, currency_id=currency.id)

    form = InternalTransactionForm

    if form.validate_on_submit():
        transaction = InternalTransaction()

    return render_template('internal_transaction.html', currency=currency, sub_account=sub_account, form=form)