import secrets
import datetime

from flask import Flask, render_template
from flask_security import Security, SQLAlchemyUserDatastore, hash_password
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
security = Security()


def create_app():
    app = Flask(__name__)

    # Load config from file config.py
    app.config.from_pyfile('config.py')

    # Database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = (f"postgresql://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}"
                                             f"@{app.config['DB_HOST']}:{app.config['DB_PORT']}"
                                             f"/{app.config['DB_NAME']}")

    db.init_app(app)

    # Setup Flask-Security module
    from models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    # Register blueprints
    from views.home import bp as bp_home
    app.register_blueprint(bp_home)

    # from views.account import bp as bp_account
    # app.register_blueprint(bp_account)

    from views.transaction import bp as bp_transaction
    app.register_blueprint(bp_transaction)

    @app.before_first_request
    def db_init():
        from models import Account, Currency, SubAccount

        # --------------------------- phase one ------------------------------
        # account1 = Account(active=True, created_at=datetime.datetime.now())
        # account2 = Account(active=True, created_at=datetime.datetime.now())
        #
        # currency1 = Currency(name='zł', exchange_rate=1.0)
        # currency2 = Currency(name='eur', exchange_rate=4.68)
        #
        # db.session.add(account1)
        # db.session.add(account2)
        # db.session.add(currency1)
        # db.session.add(currency2)
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

        # if not user_datastore.find_role(role='User'):
        #     db.session.add(Role(name='User', description='Normal user'))
        #
        # if not user_datastore.find_user(email="test@test"):
        #     user_datastore.create_user(
        #         email="test@test",
        #         password=hash_password("test"),
        #         confirmed_at=datetime.datetime.now(),
        #         roles=['User'],
        #         account_id=1,
        #         name='test1'
        #     )
        # if not user_datastore.find_user(email="test2@test"):
        #     user_datastore.create_user(
        #         email="test2@test",
        #         password=hash_password("test"),
        #         confirmed_at=datetime.datetime.now(),
        #         roles=['User'],
        #         account_id=2,
        #         name='test2'
        #     )
        # db.session.commit()
        # --------------------------------------------------------------------

    return app