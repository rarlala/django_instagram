from django.urls import path

from . import views
from .views import post_create, comment_create

app_name = 'posts'

urlpatterns = [
    # /posts/
    path('', views.post_list, name='post-list'),
    # path('explore/tags/<str:tag>/', post_list_by_tag, name='post-list-by-tag'),

    # /posts/3/like/
    path('<int:pk>/like/', views.post_like, name='post-like'),

    path('create/', post_create, name="post-create"),
    path('<int:post_pk>/comments/create/', comment_create, name="comment-create"),
]
