from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Scholarship(db.Model):
    name = db.Column(db.String(100), unique=True)
    amount = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), primary_key=True)

    def __init__(self, name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type

    def __repr__(self):
        return '<Name: %r Amount: %d Type: %r>' % ()


class Extracurriculars(db.Model):
    name = db.Column(db.String(100), unique=True)
    hours = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), primary_key=True)

    def __init__(self, name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type


class Contests(db.Model):
    name = db.Column(db.String(100), unique=True)
    amount = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), primary_key=True)
    subject = db.Column(db.String(80), primary_key=True)

    def __init__(self, name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type
        self.subject = subject














