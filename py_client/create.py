import requests

# CreateListView類別可以新增產品也可以列出產品
endpoint = "http://127.0.0.1:8000/api/products/"
data = {
    "title": "This field is done.",    

}
get_reponse = requests.post(endpoint, json=data)

print(get_reponse.json())
print(get_reponse.status_code) # 印出回復狀態 200、404、500...