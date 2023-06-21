from flask import Flask, render_template
from flask import request
from flask_restful import Api

genaibox = Flask(__name__)
api = Api(genaibox, prefix='/api')

@genaibox.route("/")
def index():
    return render_template("index.html")


@genaibox.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']

    # Make the API call using the user input
    # ...

    # Process the API response
    # ...

    return 'API call successful!'