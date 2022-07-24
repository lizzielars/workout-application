from flask import Blueprint, render_template

app = Blueprint('main', __name__)


@app.route("/")
def home():
    """
    A function that is called when the route "/" is activated.
    :return: returns a home page template
    """

    return render_template("home.html")
