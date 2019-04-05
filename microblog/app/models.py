# This file defines the initial schema (database structure) 
from app import db

'''
A model that represents users:

                    users
        id                  INTEGER
        username            VARCHAR (64)
        email               VARCHAR (120)
        password_hash       VARCHAR (128)
'''

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)