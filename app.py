from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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

    # Register blueprints
    from views.home import bp as bp_home
    app.register_blueprint(bp_home)

    from views.account import bp as bp_account
    app.register_blueprint(bp_account)

    return app