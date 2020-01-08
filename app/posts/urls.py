from django.urls import path

from . import views
from .views import post_create, comment_create

app_name = 'posts'

urlpatterns = [
    # /posts/
    path('', views.post_list, name='post-list'),

    # /posts/3/like/
    path('<int:pk>/like/', views.post_like, name='post-like'),

    path('create/', post_create, name="post-create"),
    path('<int:post_pk>/comments/create/', comment_create, name="comment-create"),
]
