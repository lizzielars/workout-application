"""
 * FILENAME: [hww-app]
 * AUTHOR: [Team Workout App]
 * COURSE: [CMSC 495 7383]
 * PROFESSOR: [Jeff Sanford]
 * CREATEDATE: [04/16/2022]

"""
from flask import Flask

from controller import main_blueprint, auth_blueprint, workout_blueprint
from db import db
from model import user, exercise, cart_item


def create_app():
    """
    Function that creates flask app and initializes it
    """
    # Create app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(main_blueprint.app)

    app.register_blueprint(auth_blueprint.app)
    auth_blueprint.init_blueprint(app)

    app.register_blueprint(workout_blueprint.app)

    # Attach config file with secret
    app.config.from_pyfile("config/app.cfg", silent=True)

    # Init DB
    db.init_db(app)
    user.init_model(app)
    exercise.init_model(app)
    cart_item.init_model(app)

    return app


# run file with python3 cmd
if __name__ == "__main__":
    create_app()
