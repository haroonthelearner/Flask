from flask import Flask, jsonify
from marshmallow import Schema, fields

app = Flask(__name__)

class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()

books_data = [
    {"title": "Book 1", "author": "Author A"},
    {"title": "Book 2", "author": "Author B"},
]

@app.route('/books', methods=['GET'])
def get_books():
    schema = BookSchema(many=True)
    result = schema.dump(books_data)
    return result  # Flask will automatically convert this to a JSON response

if __name__ == '__main__':
    app.run(debug=True)
