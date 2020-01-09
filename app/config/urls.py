"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from members.views import signup_view

urlpatterns = [
    path('', signup_view, name='signup'),
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('posts/', include('posts.urls')),
]

urlpatterns += static(
    # prefix='/media/',
    # URL 앞부분이 /media/이면
    prefix=settings.MEDIA_URL,
    # document_root위체어서 나머지 path에 해당하는 파일을 리턴
    document_root=settings.MEDIA_ROOT,
)
