# 封装请求码
from django.http import JsonResponse


class HttpCode(object):
    ok = 200
    params_error = 400
    un_auth = 401
    method_error = 405
    server_error = 500


# 封装返回的json数据
def result(code=HttpCode.ok, message="", data=None, **kwargs):
    json_data = {
        "code": code,
        "message": message,
        "data": data
    }
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_data.update(kwargs)
    return JsonResponse(json_data)


def ok(message="", data=None):
    return result(message=message, data=data)


# 参数错误
def params_error(message="", data=None):
    return result(code=HttpCode.params_error, message=message, data=data)


# 没有授权
def un_auth(message="", data=None):
    return result(code=HttpCode.un_auth, message=message, data=data)


def method_error(message="", data=None):
    return result(code=HttpCode.method_error, message=message, data=data)


def server_error(message="", data=None):
    return result(code=HttpCode.server_error, message=message, data=data)
