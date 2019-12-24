from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    """
    URL: /members/login/ (members.url 사용, config.urls에 include하여 사용)
        name: members:login (url namespace를 사용)

    POST 요청시, 예제를 보고 적절히 로그인 처리 한 후, index로 돌아갈 수 있도록 한다.
    """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print('username', username, 'password', password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('members:login')
    return render(request, 'members/login.html')