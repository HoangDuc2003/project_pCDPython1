from typing import Any
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class RegisterForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    resetPassword = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_Password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            resetPassword = self.cleaned_data['reset_password']
            if password == resetPassword and password:
                return password
        raise forms.ValidationError('Mật khẩu không hợp lệ')
    def clean_Password(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Tên tài khoản có ký tự đặc biệt')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản tồn tại")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],email= self.cleaned_data['email'],password=self.cleaned_data['password'])