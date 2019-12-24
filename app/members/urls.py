from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from config.views import index
from members.views import login_view

app_name = 'members'

urlpatterns = [
    path('login/', login_view, name='login'),
]