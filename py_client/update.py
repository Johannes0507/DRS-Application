import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update/"

data = {
    "title": "Hello worl.",
    "price": 0
}

get_reponse = requests.delete(endpoint, json=data)
print(get_reponse.json())
print(get_reponse.status_code) # 印出回復狀態 200、404、500...