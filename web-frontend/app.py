from flask import Flask
from flask import render_template

from api import messages

app = Flask(__name__)


@app.route("/")
def home():
    response = messages.get_message()
    return render_template("home.html", msg=response["msg"])
