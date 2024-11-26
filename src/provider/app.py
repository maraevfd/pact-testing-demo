from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
books = [{"id": 1, "title": "1984", "author": "George Orwell"}]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books #just for mock usage
    book_to_delete = next((book for book in books if book["id"] == book_id), None)

    if book_to_delete is None:
        return jsonify({"error": "Book not found"}), 404

    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": f"Book with ID {book_id} has been deleted"}), 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)