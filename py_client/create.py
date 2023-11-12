import requests
from getpass import getpass # 可以讓在終端機打字時不會顯示打出的東西，但是在有些環境不支援這項函式

# CreateListView類別可以新增產品也可以列出產品


endpoint = "http://127.0.0.1:8000/api/products/"
headers = {
    "Authorization": "Bearer 615c4d785ac440f54cc97c6a3b6eedb350909fe3"
}
data = {
    "title": "Hello world!!!!",
    "price": 1000
}

get_reponse = requests.post(endpoint, json=data, headers=headers)

print(get_reponse.json())
print(get_reponse.status_code) # 印出回復狀態 200、404、500...