from django.urls import path

from posts import apis
from posts.views import comment_list

urlpatterns = [
    path('', apis.PostListCreateAPIView.as_view()),
    path('<int:pk>/images/',apis.PostImageCreateAPIView.as_view()),
    path('<int:post_pk>/comments/',apis.PostCommentListCreateAPIView.as_view()),
]