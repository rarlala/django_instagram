from django.urls import path

from members.views import login_view, signup_view, logout_view, naver_login

app_name = 'members'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('naver-login/', naver_login, name='naver-login'),
]