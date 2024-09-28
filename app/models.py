from flask_sqlalchemy import SQLAlchemy
from app import db


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    narrative = db.Column(db.Text, nullable=False)

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'))
    story = db.relationship('Story', backref=db.backref('choices', lazy=True))
    text = db.Column(db.String(200), nullable=False)