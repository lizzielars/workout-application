from dataclasses import dataclass

from db.db import db


@dataclass
class CartItem(db.Model):
    cartItemID: int = db.Column(db.Integer, primary_key=True)
    workoutID: int = db.Column(db.Integer, db.ForeignKey('workout.workoutID'), nullable=False)
    exerciseID: int = db.Column(db.Integer, nullable=False)
    muscleGroup: str = db.Column(db.String, nullable=False)
    exerciseName: str = db.Column(db.String, nullable=False)


def init_model(app):
    with app.app_context():
        db.create_all()
