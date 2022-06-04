from flask import Blueprint, render_template


bp = Blueprint('bp_account', __name__, template_folder='templates')


#login required ....
# Show account page
@bp.route('/account', methods=['GET'])
def account_get():
    return render_template('account.html')


