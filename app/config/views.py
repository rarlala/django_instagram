from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return redirect('posts:post-list')

    else:
        return render(request, 'index.html')

# base.html 추가
# 상단에 {% load static %}
# 정적파일 불러올 때 {% static '경로'%}로 불러옴
# index.html과 login.html이 base.html을 extends하도록 함