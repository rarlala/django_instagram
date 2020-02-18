from django.urls import path

from .. import views

app_name = 'members'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('naver-login/', views.naver_login, name='naver-login'),
]