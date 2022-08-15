from flask import Blueprint, render_template, abort
from flask_login import login_required

from models import SubAccount, Currency

bp = Blueprint('bp_account', __name__, template_folder='templates')


# Show account page
@bp.route('/account/<account_id>/<string:currency_name>', methods=['GET'])
@login_required
def get(account_id=0, currency_name='pl'):
    if account_id == 0:
        abort(404)

    # check if sub-account exists (jakiś try except od sqlalchemy)
    currency = Currency.query.filter_by(name=currency_name).first()
    sub_account = SubAccount.query.filter_by(account_id=account_id, currency_id=currency.id)

    return render_template('account.html', currency=currency, sub_account=sub_account)


