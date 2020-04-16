from django.views.decorators.csrf import csrf_exempt
from mock.templatetags.function import *


# Create your views here.
@csrf_exempt
def entrance(request, par):
    uri = request.path
    if "/callback" == uri:
        response = callback.mock_callback(request)
    elif "/getparameter" == uri:
        key = request.GET.get('key')
        parameter=request.GET.get('parameter')
        value=mock_parameter.getparameter(key,parameter)
        method_result=json.dumps({key:value}, ensure_ascii=False)
        response = HttpResponse(method_result, content_type="application/json,charset=utf-8")
    elif "/encryption"==uri:
        method=request.GET.get('method')
        key = request.GET.get('key')
        data=request.GET.get('data')
        value=mock_parameter.getencryption(method,key,data)
        method_result = json.dumps({method: value}, ensure_ascii=False)
        response = HttpResponse(method_result, content_type="application/json,charset=utf-8")
    else:
        if "/favicon.ico" in uri:
            method_result = "页面正常请求不做处理"
            response = HttpResponse(method_result, content_type="application/json,charset=utf-8")
        else:
            response = Method.mock_method(request)
    return response




