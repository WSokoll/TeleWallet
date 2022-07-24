import datetime
from app import db


class Roles(db.Model):
    __tablename__ = 'Roles'
    RoleId = db.Column(db.Integer(), primary_key=True)
    RoleName = db.Column(db.String(80), unique=True)
    RoleDescription = db.Column(db.String(255))
