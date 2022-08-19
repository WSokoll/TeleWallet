from flask import Blueprint, render_template, abort
from flask_login import login_required

from models import SubAccount, Currency

bp = Blueprint('bp_account', __name__, template_folder='templates')


# Show account page
@bp.route('/account/<int:account_id>/<string:currency_name>', methods=['GET'], defaults={'currency_name': 'pln'})
@login_required
def get(account_id=0, currency_name='pln'):
    if account_id == 0:
        abort(404)

    currency = Currency.query.filter_by(name=currency_name).first()
    if not currency:
        abort(404)

    sub_account = SubAccount.query.filter_by(account_id=account_id, currency_id=currency.id).first()
    if not sub_account:
        abort(404)

    return render_template('account.html', currency=currency, sub_account=sub_account)


