import requests
from getpass import getpass # 可以讓在終端機打字時不會顯示打出的東西，但是在有些環境不支援這項函式

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username = input("What is your username？\n")
pwd = getpass("What is your password？\n")

auth_reponse = requests.post(auth_endpoint, json={"username": username, "password": pwd})

print(auth_reponse.json())
print(auth_reponse.status_code) 


if auth_reponse.status_code == 200:
    # CreateListView類別可以新增產品也可以列出產品
    Token = auth_reponse.json()["token"]
    headers = {
        "Authorization": f"Bearer {Token}"
    }

    endpoint = "http://127.0.0.1:8000/api/products/"
    get_reponse = requests.get(endpoint, headers=headers)

    print(get_reponse.json())
    print(get_reponse.status_code) # 印出回復狀態 200、404、500...