from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(label="请输入用户账号", max_length=100)
    password = forms.CharField(label="请输入账号密码", widget=forms.PasswordInput)
    captcha = CaptchaField(label="验证码")
    remember_me = forms.BooleanField(label="记住我", required=False)
