from django.urls import path

from posts import apis

urlpatterns = [
    path('', apis.PostListCreateAPIView.as_view()),
]