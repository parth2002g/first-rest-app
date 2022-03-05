import flask
from flask import request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import json
# Import for Migrations
from flask_migrate import Migrate, migrate

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [{'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany'}]

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(40), unique=False, nullable=False)
    author_name = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"Book : {self.book_name}, Author: {self.author_name}"


@app.route('/get_books', methods=['GET'])
def get_books():
    # TODO fetch from datqbase
    return jsonify(books)

@app.route('/put_books', methods=['POST'])
def put_books():
    # TODO
    new_books = json.loads(request.data)
    print(new_books)
    books.append(new_books)
    return jsonify(books)

@app.route('/putting_in_database', methods=['POST'])
def creating_database():
        for i in range(len(books)):
            title = books[i]['title'];
            author = books[i]['author'];
            if title != '' and author != '':
                p = Profile(book_name=title, author_name=author)
                db.session.add(p)
                db.session.commit()
        return redirect('/put_books')

@app.route('/reverse_integer', methods=['GET'])
def reverse_integer():
    """
    URL: http://127.0.0.1:5000/reverse_integer?integer=567892
    """
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

if __name__ == '__main__':
    app.run()