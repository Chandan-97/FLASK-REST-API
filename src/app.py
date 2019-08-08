from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        "name" : "Book1",
        "price" : 3,
        "isbn" : 908,
    },
    {
        "name" : "Book2",
        "price" : 4,
        "isbn" : 89,
    }
]

@app.route("/books")
def get_books():
    return jsonify({"books" : books})

@app.route("/books/<int:isbn>")
def get_books_by_isbn(isbn):
    for book in books:
        if(book["isbn"] == isbn):
            return_value = {
                "name" : book["name"],
                "price" : book["price"]
            }
    return jsonify(return_value)

app.run(port=5000)