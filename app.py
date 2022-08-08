import secrets
from datetime import datetime

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

    from views.account import bp as bp_account
    app.register_blueprint(bp_account)

    from views.transaction import bp as bp_transaction
    app.register_blueprint(bp_transaction)

    return app