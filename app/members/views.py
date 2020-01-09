from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm

# from members.models import User
User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('posts:post-list')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'members/login.html', context)


def signup_view(request):
    """
    config.views.index 삭제
    Template : index.html을 복사해서 /members/signup.html
    URL: /
    From: members.forms.SignupForm
    생성에 성공하면 로그인 처리 후 (위 login_view 참조) posts:post-list로 redirect 처리
    """

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.login(request, user)
            return redirect('posts:post-list')
    else:
        form = SignupForm()

    context = {
        'form': form
    }

    if request.user.is_authenticated:
        return redirect('posts:post-list')

    else:
        return render(request, 'members/signup.html', context)


def logout_view(request):
    """
    GET 요청으로 처리함
    요청에 있는 사용자를 logout처리
    django.contrib.logout함수를 사용한다.
    """
    logout(request)
    return redirect('members:login')
