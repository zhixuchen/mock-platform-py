import datetime
import json

import requests
from django.http import HttpResponse

from mock import models


# Create your views here.

def entrance(request, par):
    uri = request.path
    if "callback" in uri:
        response = callback.mock_callback(request)
    else:
        if "/favicon.ico"in uri:
            method_result="页面正常请求不做处理"
            response=HttpResponse(method_result, content_type="application/json,charset=utf-8")
        else:
            response = method.mock_method(request)
    return response


class callback:
    def mock_callback(request):
        method = request.method
        url = request.build_absolute_uri()
        businessno = request.GET.get("businessno")
        platform = request.GET.get("platform")
        env = request.GET.get("env")
        try:
            mock_callback = callback.getcallback(request)
            callback_id = mock_callback.id
            callback_name = mock_callback.name
            callback_body = mock_callback.request_body
            callback_pragram = mock_callback.pragram
            callback_body = callback_body.replace('{{' + callback_pragram + '}}', businessno)
            callback_uri = mock_callback.request_uri
            callback_url = "http://" + env + "-" + platform + "-docker-" + env + ".beta.saasyc.com" + callback_uri
            post_enable = True
        except:
            callback_id = 0
            callback_name = "未找到对应的mock回调"
            callback_url = url
            callback_body = ''
            post_enable = False
        log_id = Log.set_log("callback", callback_id, callback_name, callback_url, callback_body, method, "")
        if post_enable:
            method_result = callback.callback_post(callback_url, callback_body)
        else:
            method_result = {"url": url, "method": method, "body": '未找到对应的mock回调'}
        Log.updata_log(log_id, method_result)
        return HttpResponse(json.dumps(method_result, ensure_ascii=False),
                            content_type="application/json,charset=utf-8")

    def getcallback(request):
        project = request.GET.get("project")
        status = request.GET.get("status")
        try:
            project_id = models.Project.objects.get(project=project).id
            callback = models.Callback.objects.get(project_id=project_id, status=status)
        except:
            print("未找到对应的mock回调")
        return callback

    def callback_post(callback_url, callback_body):
        post_data = callback_body.encode('utf-8')
        response = requests.post(callback_url, data=post_data, )
        content = response.content
        return json.loads(content)


class method:
    def mock_method(request):
        method = request.method
        url = request.build_absolute_uri()
        body = str(request.body, 'utf-8')
        if len(body) != 0:
            body = json.loads(body)
        try:
            mock_method = method.getmethod(url, body)
            method_id = mock_method["method_id"]
            method_name = mock_method["method_name"]
        except:
            method_id=0
            method_name="未找到对应mock请求的方法"
        log_id = Log.set_log("request", method_id, method_name, url, body, method, "")
        if method_id != 0:
            method_result = method.getmethod_result(method_id, body)
        else:
            method_result = json.dumps({"url": url, "method": method, "body": body}, ensure_ascii=False)
        Log.updata_log(log_id, method_result)
        return HttpResponse(method_result, content_type="application/json,charset=utf-8")

    def getmethod(url, body):
        method_list = models.Method.objects.all().values_list('id', 'uri', 'route', 'project_id', 'name')
        for method in method_list:
            if method[1] in url:
                if method[2] == None:
                    method_id = method[0]
                    method_name = method[4]
                    break
                else:
                    project_id = method[3]
                    rule_py = str(models.Project.objects.get(id=project_id))
                    rule = exec_code().ex(rule_py, body)
                    if rule == method[2]:
                        method_id = method[0]
                        method_name = method[4]
                        break
            else:
                method_id = 0
                method_name = '未找到相应的mock请求'
        getmethod = {"method_id": method_id, "method_name": method_name}
        return getmethod

    def getmethod_result(id, body):
        method_list = models.Method.objects.all().values_list('id', 'pragram', 'result', 'name')
        for method in method_list:
            if method[0] == id:
                method_pragram = method[1]
                method_result = method[2]
                break
        if method_pragram != None:
            replace_pragram = method.getreplace(method_pragram, body)
            method_result = method_result.replace("{{" + method_pragram + "}}", str(replace_pragram))
        return method_result

    def getreplace(method_pragram, body):
        code = str(models.Function.objects.get(function_name='get' + method_pragram))
        exec = exec_code()
        replace_pragram = exec.ex(code, body)
        return replace_pragram


class Log:
    def set_log(type, method_id, name, request_url, request_body, request_method, response):
        creat_time = datetime.datetime.now()
        log_id = models.Log.objects.create(type=type, method_id=method_id, name=name, request_url=request_url,
                                           request_body=request_body, request_method=request_method, response=response,
                                           creat_time=creat_time).id
        return log_id

    def updata_log(log_id, response):
        models.Log.objects.filter(id=log_id).update(response=response)


class exec_code(object):
    def __init__(self):
        self.__globals__ = {}
        self.__locals__ = self.__globals__

    def ex(self, code, body):
        self.__globals__.setdefault('body', body)

        exec(code, self.__globals__, self.__locals__)
        return self.__globals__['replace_pragram']
