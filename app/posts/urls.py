from django.urls import path

from posts.views import post_list

app_name = 'posts'

urlpatterns = [
    path('', post_list, name='postList')
]