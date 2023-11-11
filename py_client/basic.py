import requests

endpoint = "http://127.0.0.1:8000/api/"

get_reponse = requests.post(endpoint, json={"title": "Hello world", "price": "123" })

# print(get_reponse.text) # 印出所獲取的內容
# print(get_reponse.headers)
print(get_reponse.json())
print(get_reponse.status_code) # 印出回復狀態 200、404、500...