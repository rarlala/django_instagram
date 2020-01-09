from django import forms
from django.contrib.auth import login
from django.http import HttpResponse, request
from django.shortcuts import redirect

from members.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'아이디'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호'
            }
        )
    )

class SignupForm(forms.Form):
    email = forms.CharField(max_length=30)
    username = forms.CharField(max_length=10)
    name = forms.CharField(max_length=10)
    password = forms.CharField(max_length=20)

    def save(self, email, username, name, password):
        """
        Form으로 전달받은 데이터를 사용해서 새로운 User를 생성하고 리턴
        username과 email 검증 로직도 이 안에 넣기
        """
        if User.objects.filter(username=username).exists():
            return HttpResponse('이미 사용중인 username/email 입니다')
        if User.objects.filter(email=email).exists():
            return HttpResponse('이미 사용중인 username/email 입니다')

        return User.objects.create_user(
            email=email,
            username=username,
            name=name,
            password=password
        )
