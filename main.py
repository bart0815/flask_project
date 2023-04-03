

import flask
from flask import render_template
from pathlib import Path


app = flask.Flask(__name__)



@app.route("/")
def hello():
    return render_template("base.html")


@app.route("/page1")
def page1():
    return render_template("index.html")


