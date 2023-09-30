from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST
from .forms import LogiForm
from utils import restful


@require_POST
def login_view(request):
    form = LogiForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get("telephone")
        password = form.cleaned_data.get("password")
        remember = form.cleaned_data.get("remember")
        user = authenticate(request, username=telephone, password=password)
        print(user)
        if user:
            # 判断用户是否可用
            if user.is_active:
                login(request, user)
                if remember:
                    # session 过期时间为Django默认,两个星期
                    request.session.set_expiry(None)
                else:
                    # 浏览器关闭session过期
                    request.session.set_expiry(0)
                return restful.ok(data={"username": user.username})
            else:
                return restful.un_auth(message="您的账号已经被冻结")
        else:
            return restful.params_error(message="手机号或者密码错误")
    else:
        errors = form.get_errors()
        return restful.params_error(message=errors)
