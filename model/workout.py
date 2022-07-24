from dataclasses import dataclass
from datetime import date

from db.db import db


@dataclass
class Workout(db.Model):
    workoutID: int = db.Column(db.Integer, primary_key=True, nullable=False)
    userID: int = db.Column(db.Integer, db.ForeignKey('user.userID'))
    difficulty: str = db.Column(db.Integer, nullable=False, default='Beginner')
    userRating: int = db.Column(db.Integer, nullable=True)
    isCompleted: bool = db.Column(db.Boolean, nullable=False, default=False)
    startDate: date = db.Column(db.Date, nullable=True)
    completionDate: date = db.Column(db.Date, nullable=True)

    cartItems = db.relationship('CartItem', lazy='dynamic')


def init_model(app):
    with app.app_context():
        db.create_all()
