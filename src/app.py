from flask import Flask, jsonify, request

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

# GET /books
@app.route("/books")
def get_books():
    return jsonify({"books" : books})

# POST /books
# {
#     "name" : "F",
#     "price" : 6,
#     "isbn" : 6987
# }

@app.route("/books", methods=["POST",])
def add_book():
    return jsonify(request.get_json())

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