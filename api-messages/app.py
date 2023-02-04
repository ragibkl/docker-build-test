from flask import Flask
from flask import render_template
from faker import Faker

app = Flask(__name__)


@app.route("/api/message")
def get_message():
    fake = Faker()
    msg = "This is a message from flask backend."
    return {"msg": fake.sentence()}
