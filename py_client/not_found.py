import requests

# 測試如果搜尋不到會如何。
endpoint = "http://127.0.0.1:8000/api/products/123123123/"
get_reponse = requests.get(endpoint)

print(get_reponse.json())
print(get_reponse.status_code) # 印出回復狀態 200、404、500...