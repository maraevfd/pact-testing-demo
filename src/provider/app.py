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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)