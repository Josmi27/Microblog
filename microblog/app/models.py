# This file defines the initial schema (database structure) 
from datetime import datetime
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
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


'''
A model that represents posts:

                    posts
        id                  INTEGER
        body                VARCHAR (140)
        timestamp           DATETIME
        user_id             INTEGER
'''

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)