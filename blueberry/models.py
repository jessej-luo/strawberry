from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

def reset():
    db.drop_all()
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email, password):
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User: {}>'.format(self.email)

class Scholarship(db.Model):
    name = db.Column(db.String(100), unique=True)
    amount = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), primary_key=True)

    def __init__(self, name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type

    def __repr__(self):
        return '<Name: {}, Amount: {}, Type: {}>'.format(self.name, self.amount, self.type)


class Extracurricular(db.Model):
    name = db.Column(db.String(100), unique=True)
    hours = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), primary_key=True)

    def __init__(self, name, hours, type):
        self.name = name
        self.hours = hours
        self.type = type

    def __repr__(self):
        return '<Name: {} Amount: {} Type: {}>'.format(self.name, self.hours, self.type)


class Contest(db.Model):
    name = db.Column(db.String(100), unique=True)
    amount = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), primary_key=True)
    subject = db.Column(db.String(80), primary_key=True)

    def __init__(self, name, amount, type, subject):
        self.name = name
        self.amount = amount
        self.type = type
        self.subject = subject

    def __repr__(self):
        return '<Name: {} Amount: {} Type: {} Subject: {}>'.format(self.name, self.amount, self.type, self.subject)














