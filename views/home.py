from flask import Blueprint, render_template
from models import Roles
from app import db

bp = Blueprint('bp_home', __name__, template_folder='templates')


# Show home page
@bp.route('/home', methods=['GET'])
@bp.route('/', methods=['GET'])
def home_get():

    role = Roles()
    role.RoleName = 'normal'
    role.RoleDescription = 'normal user'

    db.session.add(role)
    db.session.commit()

    return render_template('home.html')