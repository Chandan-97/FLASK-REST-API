from flask import Flask, jsonify, request, Response, json

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

def validBookObject(bookObject):
    if "name" in bookObject and "price" in bookObject and "isbn" in bookObject:
        return True
    return False

@app.route("/books", methods=["POST",])
def add_book():
    request_data = request.get_json()
    if(validBookObject(request_data)):
        new_book = {
            "name" : request_data["name"],
            "price" : request_data["price"],
            "isbn" : request_data["isbn"]
        }
        books.insert(0, new_book)
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "/books/" + str(new_book["isbn"])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error" : "Invalid book object passed in request",
            "helpString" : "Data passed in similar to this {'name' : 'Book45', 'price' : 23, 'isbn' : 534}"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application/json')
        return response

@app.route("/books/<int:isbn>")
def get_books_by_isbn(isbn):
    for book in books:
        if(book["isbn"] == isbn):
            return_value = {
                "name" : book["name"],
                "price" : book["price"]
            }
    return jsonify(return_value)

# PUT
# {
#     "name" : 'The Odyssey',
#     "price" : 0.9
# }
@app.route("/books/<int:isbn>", methods=["PUT"])
def replace_book(isbn):
    request_data = request.get_json()
    new_book = {
        "name" : request_data["name"],
        "isbn" : isbn,
        "price" : request_data["price"]
    }

    i = 0
    for book in books:
        currentIsbn = book['isbn']
        if currentIsbn == isbn:
            books[i] = new_book
        i+=1
    
    response = Response("", status=204)
    return response

app.run(port=5000)