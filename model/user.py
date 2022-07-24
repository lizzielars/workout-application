from dataclasses import dataclass

from flask_bcrypt import Bcrypt
from flask_login import UserMixin

from db.db import db


@dataclass
class User(db.Model, UserMixin):
    userID: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(25), unique=True, nullable=False)
    email: str = db.Column(db.String(50), unique=True, nullable=False)
    password: str = db.Column(db.String(25), nullable=False)
    exerciseTime: int = db.Column(db.Integer, default=30, nullable=False)
    exerciseSets: int = db.Column(db.Integer, default=3, nullable=False)
    exerciseRest: int = db.Column(db.Integer, default=60, nullable=False)

    workouts = db.relationship('Workout', lazy='dynamic')

    def get_id(self):
        return self.userID

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"


def init_model(app):
    with app.app_context():
        db.create_all()
        gen_hash = Bcrypt().generate_password_hash
        hashed_password = gen_hash('admin').decode("utf-8")
        db.session.add(User(username='admin', email='admin@admin.com', password=hashed_password))
        db.session.commit()
