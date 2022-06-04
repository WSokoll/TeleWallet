from flask import Flask, render_template


app = Flask(__name__)

# Register blueprints
from views.home import bp as bp_home
app.register_blueprint(bp_home)

from views.account import bp as bp_account
app.register_blueprint(bp_account)

if __name__ == '__main__':
    app.run()
