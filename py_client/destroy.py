import requests

product_id = input("請輸入你想刪除產品的ID：\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} 不是正確的產品ID')

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/destroy/"
    get_reponse = requests.delete(endpoint)
  
    print(get_reponse.status_code, get_reponse.status_code==204) # 印出回復狀態 200、404、500...