import flask
from flask import request, jsonify

#Il web server
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di web API.</p>"

#I dati
books = [
    {'id': 0,
     'title': 'Il nome della rosa',
     'author': 'Umberto Eco',
     'year_published': '1980'},
     {'id': 1,
     'title': 'Il problema dei tre corpi',
     'author': 'Liu Cixin',
     'year_published': '2008'},
     {'id': 2,
     'title': 'Fondazione',
     'author': 'Isacc Asimov',
     'year_published': '1951'}
]

#Una prima URL per la API
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#Ricerca per ID
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    print(request.args)
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

app.run()