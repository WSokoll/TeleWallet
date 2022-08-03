from flask import Blueprint, redirect
from app import db
from models import Role, Account, User, RolesUsers, Currency, SubAccount

bp = Blueprint('bp_database_temp', __name__, template_folder='templates')


@bp.route('/database_temp', methods=['GET'])
def database_temp():

    return redirect('home.html')