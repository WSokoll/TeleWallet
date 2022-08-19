import secrets
import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from passlib.hash import sha256_crypt

login_manager = LoginManager()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Load config from file config.py
    app.config.from_pyfile('config.py')

    # Database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = (f"postgresql://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}"
                                             f"@{app.config['DB_HOST']}:{app.config['DB_PORT']}"
                                             f"/{app.config['DB_NAME']}")

    db.init_app(app)

    # init flask login
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=int(user_id)).first()

    # Register blueprints
    from views.home import bp as bp_home
    app.register_blueprint(bp_home)

    from views.account import bp as bp_account
    app.register_blueprint(bp_account)

    from views.transaction import bp as bp_transaction
    app.register_blueprint(bp_transaction)

    from views.exchange import bp as bp_exchange
    app.register_blueprint(bp_exchange)

    from views.auth import bp as bp_auth
    app.register_blueprint(bp_auth)

    # TEST DATA
    # @app.before_first_request
    # def create_test_data():
        # from models import Account, Currency, SubAccount

        # --------------------------- phase one ------------------------------
        # account1 = Account(active=True, created_at=datetime.datetime.now())
        # account2 = Account(active=True, created_at=datetime.datetime.now())
        #
        # currency1 = Currency(name='pln', exchange_rate=1.0)
        # currency2 = Currency(name='eur', exchange_rate=4.68)
        # currency3 = Currency(name='usd', exchange_rate=4.61)
        #
        # db.session.add(account1)
        # db.session.add(account2)
        # db.session.add(currency1)
        # db.session.add(currency2)
        # db.session.add(currency3)
        # db.session.commit()
        # --------------------------------------------------------------------

        # --------------------------- phase two ------------------------------
        # sub_account1 = SubAccount(balance=100.1, account_id=1, currency_id=1)
        # sub_account2 = SubAccount(balance=1000.2, account_id=1, currency_id=2)
        # sub_account3 = SubAccount(balance=2000.0, account_id=2, currency_id=1)
        # sub_account4 = SubAccount(balance=300.44, account_id=2, currency_id=2)
        #
        # db.session.add(sub_account1)
        # db.session.add(sub_account2)
        # db.session.add(sub_account3)
        # db.session.add(sub_account4)
        #
        # user1 = User(email="test1@test.com",
        #              password=sha256_crypt.encrypt("test1"),
        #              confirmed_at=datetime.datetime.now(),
        #              account_id=1,
        #              name='Adam Nowak',
        #              fs_uniquifier=123)
        #
        # user2 = User(email="test2@test.com",
        #              password=sha256_crypt.encrypt("test2"),
        #              confirmed_at=datetime.datetime.now(),
        #              account_id=2,
        #              name='Marek Kowalski',
        #              fs_uniquifier=321)
        #
        # db.session.add(user1)
        # db.session.add(user2)
        #
        # db.session.commit()
        # --------------------------------------------------------------------

    return app