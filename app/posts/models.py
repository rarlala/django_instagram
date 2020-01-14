from django.db import models
from members.models import User


class Post(models.Model):
    # 인스타그램의 포스트
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    like_users = models.ManyToManyField(User, through='PostLike', related_name='like_posts_set',)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', verbose_name='해시태그 목록', related_name="posts", )

    def __str__(self):
        return f'author: {self.author}, content: {self.content}, like_users: {self.like_users}, created:{self.created}'


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/image')


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class PostLike(models.Model):
    """
    사용자가 좋아요 누른 Post 정보를 저장
    Many-to-many 필드를 중간모델을 거쳐 사용
    언제 생성되었는지 Extra field로 저장
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    """
    Many-to-many에서 필드는 Post에 클래스에 작성
    HashTag의 Tag를 담당
    Post입장에서 post.tags.all()로 연결된 전체 Tag를 불러올 수 있어야 함
    Tag 입장에서 tag.posts.all()로 연결된 전체 Post를 불러올 수 있어야 함

    Django admin에서 결과를 볼 수 있도록 admin.py에 적절히 내용 기록
    중계모델(Intermediate model)을 사용할 필요 없음
    """
    name = models.CharField('', max_length=100)

    def __str__(self):
        return self.name