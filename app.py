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

@app.route('/reverse_integer', methods=['GET'])
def reverse_integer():
    x = int(request.args.get("integer"))
    if x <= 0:
        a = -1 * int(str(x * -1)[::-1])
    if x > 0:
        a = int(str(x)[::-1])
    mina = -2 ** 31
    maxa = 2 ** 31 - 1
    if a not in range(mina, maxa):
        return str(0)
    else:
        return str(a)

app.run()