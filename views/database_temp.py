from flask import Blueprint, redirect
from app import db
from models import Role, Account, User, RolesUsers, Currency, SubAccount

bp = Blueprint('bp_database_temp', __name__, template_folder='templates')


@bp.route('/database_temp', methods=['GET'])
def home_get():
    #
    # account = Account(active=True)
    # currency = Currency(name='zł', exchange_rate=1)
    # subAccount = SubAccount(balance=100.50, account_id=4, currency_id=4)
    # #
    # db.session.add(account)
    # db.session.add(currency)
    #
    # db.session.commit()

    # db.session.add(subAccount)
    #
    # db.session.commit()

    return redirect('home.html')