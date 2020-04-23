import requests

#api-endpoint
URL = "http://127.0.0.1:5000/api/v1/resouces/books"

#parametri query
Params = {'id':1}

#invia richiesta
r = requests.get(url = URL, params = Params)

#estrazione dati
data = r.json()
print(data)