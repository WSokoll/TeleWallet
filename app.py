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

    # Create a user to test with
    @app.before_first_request
    def create_user():
        if not user_datastore.find_user(email="test2@test"):
            user_datastore.create_user(
                email="test2@test",
                username='tes2t',
                password=hash_password("test2"),
                confirmed_at=datetime.now(),
                roles=['User'],
                account_id=1
            )
        db.session.commit()

    # Register blueprints
    from views.home import bp as bp_home
    app.register_blueprint(bp_home)

    from views.account import bp as bp_account
    app.register_blueprint(bp_account)

    from views.database_temp import bp as bp_database_temp
    app.register_blueprint(bp_database_temp)

    return app