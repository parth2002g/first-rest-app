import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = []

@app.route('/get_books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/put_books', methods=['POST'])
def put_books():
    new_books = json.loads(request.data)
    print(new_books)
    books.append(new_books)
    return jsonify(books)

app.run()