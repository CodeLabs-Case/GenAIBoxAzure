from flask import Flask, render_template

genaibox = Flask(__name__)

@genaibox.route("/")
def index():
    return render_template("index.html")