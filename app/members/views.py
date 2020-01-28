import urllib

from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from config.settings import json_data
from .forms import LoginForm, SignupForm
import requests

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

    login_base_url = 'https://nid.naver.com/oauth2.0/authorize'
    login_params = {
        'response_type': 'code',
        'client_id': json_data['client_id'],
        'redirect_uri': 'http://localhost:8000/members/naver-login/',
        'state': 'RANDOM_STATE',
    }
    login_url = '{base}?{params}'.format(
        base=login_base_url,
        params='&'.join([f'{key}={value}' for key, value in login_params.items()])
    )

    print(login_url)

    context = {
        'form': form,
        'login_url': login_url
    }
    return render(request, 'members/login.html', context)


def naver_login(request):
    # GET parameter로 전달된 code 값을 사용해서
    # 네이버 API의 PHP 샘플코드를 보고
    # token_url을 생성
    # print(token_url)
    # print(request.GET)
    # return
    code = request.GET['code']
    if not code:
        return HttpResponse('code가 전달되지 않았습니다')

    print('code입니다', code)

    token_base_url = 'https://nid.naver.com/oauth2.0/token'
    token_params = {
        'grant_type': 'authorization_code',
        'client_id': json_data['client_id'],
        'client_secret': json_data['client_secret'],
        'redirect_uri': 'http://localhost:8000/members/naver-login/',
        'code': code,
        'state': request.GET['state'],
    }

    token_url = '{base}?{params}'.format(
        base=token_base_url,
        params='&'.join([f'{key}={value}' for key, value in token_params.items()])
    )

    print('token_url입니다.', token_url)

    # token URL에
    # GET요청을 보내고, 그 요청의 response를 받아와서
    # response가 가진 text를 출력해보기 -> HttpResponse로 보여주기
    # Hint: Python requests 라이브러리
    response = requests.get(token_url)
    access_token = response.json()['access_token']
    print('access_token입니다',access_token)

    # print(response.text)
    # print(response.status_code)

    # token = access_token
    # header = "Bearer " + token  # Bearer 다음에 공백 추가
    # url = "https://openapi.naver.com/v1/nid/me"
    # request = urllib.request.Request(url)
    # request.add_header("Authorization", header)
    # response = urllib.request.urlopen(request)
    # rescode = response.getcode()
    # if (rescode == 200):
    #     response_body = response.read()
    #     print(response_body.decode('utf-8'))
    # else:
    #     print("Error Code:" + rescode)

    # return HttpResponse(response_body.decode('utf-8'))

    me_url = "https://openapi.naver.com/v1/nid/me"
    me_headers = {
        'Authorization' : f'Bearer {access_token}',
    }
    me_response = requests.get(me_url, headers=me_headers)
    me_response_data = me_response.json()
    print(me_response_data)

    unique_id = me_response_data['response']['id']
    print(unique_id)

    # n_{unique_id}의 username을 갖는 새로운 User를 생성
    # 생성한 유저를 login 시킴
    # posts:post-list로 이동시킴

    naver_username = f'n_{unique_id}'
    if not User.objects.filter(username=naver_username).exists():
        user = User.objects.create_user(username=naver_username)
    else:
        user = User.objects.get(username=naver_username)
    login(request, user)
    return redirect('posts:post-list')


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
