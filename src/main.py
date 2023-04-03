

import flask
from flask import render_template
from pathlib import Path


app = flask.Flask(__name__)



@app.route("/")
def hello():
    return "Hello World!"

@app.route("page1")
def page1():
    return render_template(str(Path(__file__).parent.parent / "pages/index.html"))


