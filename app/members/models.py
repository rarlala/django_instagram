from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # img_profile = models.ImageField('프로필 이미지', blank=True, upload_to="users/")
    name = models.CharField('이름', max_length=100)
