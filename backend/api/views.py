from django.forms.models import model_to_dict # 可以直接輸出模型的全部內容
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        data = serializer.data
        return Response(data)
    
    return Response({"invalid": "not good data"}, status=400)
    
    # 先把客戶端的資料做ProductSerializer的資料轉換，之後再把轉換完的資訊呼叫出來

    '''
    下面的方法，雖然已經轉成json檔格式，但是因為price是decimal所以還是會遇到不支援的error，
    所以最好的方式還是用JsonReponse回傳，這一可以省略很多步驟去處理Decimal格式不相容的問題
    json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={'content-type': 'application/json'})
    '''
