import requests

endpoint = "http://127.0.0.1:8000/api/products/"
get_reponse = requests.get(endpoint)

print(get_reponse.json())
print(get_reponse.status_code) # 印出回復狀態 200、404、500...