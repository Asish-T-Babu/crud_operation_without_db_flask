from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

books = [
    {"id": 1, "title": "Book 1", "author": "Authour 1"},
    {"id": 2, "title": "Book 2", "author": "Authour 2"},
    {"id": 3, "title": "Book 3", "author": "Authour 3"}
]

@app.route('/books', methods = ['GET'])
def get_books():
    return books

@app.route('/books/<int:book_id>', methods= ['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return {'error': "book not found"}

@app.route('/books', methods= ['POST'])
def create_book():
    new_book = {'id': len(books)+1, 'title': request.form.get('title'), 'author': request.form.get('author')}
    books.append(new_book)
    return new_book

@app.route('/books/<int:book_id>', methods= ['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.form.get('title')
            book['author'] = request.form.get('author')
            return book
    return {'error': 'Book not found'}

@app.route('/books/<int:book_id>', methods= ['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {'data': 'Book Deleted Successfully'}
    return {'error': "book not found"}

# Run the flask app
if __name__ == "__main__":
    app.run(debug= True)
