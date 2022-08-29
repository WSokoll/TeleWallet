from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION

from app import db


class RolesUsers(db.Model):
    __tablename__ = 'RolesUsers'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('User.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('Role.id'))


class Role(db.Model):
    __tablename__ = 'Role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer())
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    confirmed_at = db.Column(db.DateTime())
    account_id = db.Column(db.Integer(), db.ForeignKey('Account.id'))
    roles = db.relationship('Role', secondary='RolesUsers', backref=db.backref('users', lazy='dynamic'))


class Account(db.Model):
    __tablename__ = 'Account'
    id = db.Column(db.Integer(), primary_key=True)
    active = db.Column(db.Boolean(), nullable=False, default=False)
    created_at = db.Column(db.DateTime())


class Currency(db.Model):
    __tablename__ = 'Currency'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    exchange_rate = db.Column(DOUBLE_PRECISION, nullable=False)


class SubAccount(db.Model):
    __tablename__ = 'SubAccount'
    id = db.Column(db.Integer(), primary_key=True)
    balance = db.Column(DOUBLE_PRECISION)
    account_id = db.Column(db.Integer(), db.ForeignKey('Account.id'), nullable=False)
    currency_id = db.Column(db.Integer(), db.ForeignKey('Currency.id'), nullable=False)


class InternalTransaction(db.Model):
    __tablename__ = 'InternalTransaction'
    id = db.Column(db.Integer(), primary_key=True)
    transaction_from = db.Column(db.Integer(), db.ForeignKey('User.id'), nullable=False)
    transaction_to = db.Column(db.Integer(), db.ForeignKey('User.id'), nullable=False)
    currency_id = db.Column(db.Integer(), db.ForeignKey('Currency.id'), nullable=False)
    value = db.Column(DOUBLE_PRECISION, nullable=False)
    transaction_date = db.Column(db.DateTime(), nullable=False)
    name = db.Column(db.String(255))


class ExternalTransaction(db.Model):
    __tablename__ = 'ExternalTransaction'
    id = db.Column(db.Integer(), primary_key=True)
    transaction_from = db.Column(db.String(500))
    transaction_to = db.Column(db.Integer(), db.ForeignKey('User.id'), nullable=False)
    currency_id = db.Column(db.Integer(), db.ForeignKey('Currency.id'), nullable=False)
    value = db.Column(DOUBLE_PRECISION, nullable=False)
    transaction_date = db.Column(db.DateTime(), nullable=False)
    name = db.Column(db.String(255))

    # TODO: dodać pole confirmed (wyszukiwana i sprawdzana tranzakcja po przyciśnięciu powrotu do stronki)


class CurrencyExchange(db.Model):
    __tablename__ = 'CurrencyExchange'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('User.id'), nullable=False)
    currency_from = db.Column(db.Integer(), db.ForeignKey('Currency.id'), nullable=False)
    currency_to = db.Column(db.Integer(), db.ForeignKey('Currency.id'), nullable=False)
    value_old = db.Column(DOUBLE_PRECISION, nullable=False)
    value_new = db.Column(DOUBLE_PRECISION, nullable=False)
    exchange_date = db.Column(db.DateTime(), nullable=False)
