from django.db import models


class Post(models.Model):
    # 인스타그램의 포스트
    author =
    content =
    like_users = 'PostLike를 통한 Many-to-many구현'
    created =
    pass

class PostImage(models.Model):
    # 각 포스트의 사진
    pass

class PostComment(models.Model):
    # 각 포스트의 댓글
    pass

class PostLike(models.Model):
    pass