from flask import Flask, render_template
from flask_restful import Api

genaibox = Flask(__name__)
api = Api(genaibox, prefix='/api')

@genaibox.route("/")
def index():
    return render_template("index.html")