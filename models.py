import datetime

from sqlalchemy import ForeignKey

from app import db


class Roles(db.Model):
    __tablename__ = 'Roles'
    RoleId = db.Column(db.Integer(), primary_key=True)
    RoleName = db.Column(db.String(80), unique=True)
    RoleDescription = db.Column(db.String(255))


class Accounts(db.Model):
    __tablename__ = 'Accounts'
    AccountId = db.Column(db.Integer(), primary_key=True)
    AccountActive = db.Column(db.Boolean(), nullable=False)
    AccountCreatedDate = db.Column(db.DateTime())


class Users(db.Model):
    __tablename__ = 'Users'
    UserId = db.Column(db.Integer(), primary_key=True)
    UserName = db.Column(db.String(255))
    UserSurname = db.Column(db.String(255))
    UserLogin = db.Column(db.String(255), unique=True, nullable=False)
    UserPassword = db.Column(db.String(255), nullable=False)
    UserEmail = db.Column(db.String(255), nullable=False)
    AccountId = db.Column(db.Integer(), ForeignKey("Accounts.AccountId"), nullable=False, unique=True)
    RoleId = db.Column(db.Integer(), ForeignKey("Roles.RoleId"), nullable=False)