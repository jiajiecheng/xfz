from django import forms
from apps.forms import FormMixin


class LogiForm(forms.Form, FormMixin):
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(min_length=6, max_length=16, error_messages={
        "max_length": "密码做多不能超过16个字符",
        "min_length": "密码最小不能不能小于6位"
    })
    remember = forms.IntegerField(required=False)
