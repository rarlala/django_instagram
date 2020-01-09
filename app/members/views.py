from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm

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
    Template : index.html을 그대로 사용
        action만 이쪽으로
    URL: /members/signup/
    User에 name 필드를 추가
        email, username, name, password
        를 전달받아 새로운 User를 생성한다.
        생성 시, User.objects.create_user() 메서드를 사용한다.

    이미 존재하는 username또는 email을 입력한 경우, "이미 사용중인 username/email 입니다" 라는 메시지를 HttpResponse로 돌려준다.

    생성에 성공하면 로그인 처리 후 (위 login_view 참조) posts:post-list로 redirect 처리
    """

    email = request.POST['email']
    username = request.POST['username']
    name = request.POST['name']
    password = request.POST['password']

    if User.objects.filter(username=username).exists():
        return HttpResponse('이미 사용중인 username/email 입니다')
    if User.objects.filter(email=email).exists():
        return HttpResponse('이미 사용중인 username/email 입니다')

    user = User.objects.create_user(email=email, username=username, name=name, password=password)

    login(request, user)
    return redirect('posts:post-list')


def logout_view(request):
    """
    GET 요청으로 처리함
    요청에 있는 사용자를 logout처리
    django.contrib.logout함수를 사용한다.
    """
    logout(request)
    return redirect('members:login')
