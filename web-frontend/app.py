from flask import Flask
from flask import render_template

from api import message_api

app = Flask(__name__)


@app.route("/")
def home():
    response = message_api.get_message()
    return render_template("home.html", msg=response["msg"])
