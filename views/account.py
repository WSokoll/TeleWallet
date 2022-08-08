from flask import Blueprint, render_template
from app import db
from models import SubAccount, Currency

bp = Blueprint('bp_account', __name__, template_folder='templates')


#login required ....
# Show account page
@bp.route('/account/<account_id>/<string:currency_name>', methods=['GET'])
def get(account_id=0, currency_name='pl'):

    # 404...
    # if id == 0:
    #     return

    # check if sub-account exists
    currency = Currency.query.get_or_404(name=currency_name)
    sub_account = SubAccount.query.get_or_404(account_id=account_id, currency_id=currency.id)

    return render_template('account.html', currency=currency, sub_account=sub_account)


