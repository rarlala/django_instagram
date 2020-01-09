from django import forms
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from django.http import HttpResponse, request
from django.shortcuts import redirect

from members.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디'
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

    def clean(self):
        # Form.clean에서는 cleaned_data에 접근 가능
        # cleaned_data에는 이 Form이 가진 모든 Field들에서 리턴된 데이터가 key: value로 들어있음
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError('username또는 password가 올바르지 않습니다.')
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)

# class SignupForm(forms.Form):
#     email = forms.CharField(max_length=30)
#     username = forms.CharField(max_length=10)
#     name = forms.CharField(max_length=10)
#     password = forms.CharField(max_length=20)
#
#     def save(self, email, username, name, password):
#         """
#         Form으로 전달받은 데이터를 사용해서 새로운 User를 생성하고 리턴
#         username과 email 검증 로직도 이 안에 넣기
#         """
#         if User.objects.filter(username=username).exists():
#             return HttpResponse('이미 사용중인 username/email 입니다')
#         if User.objects.filter(email=email).exists():
#             return HttpResponse('이미 사용중인 username/email 입니다')
#
#         return User.objects.create_user(
#             email=email,
#             username=username,
#             name=name,
#             password=password
#         )
