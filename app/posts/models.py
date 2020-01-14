import re

from django.db import models
from members.models import User


class Post(models.Model):
    TAG_PATTERN = re.compile(r'#(\w+)')
    # 인스타그램의 포스트
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    content_html = models.TextField(blank=True)
    like_users = models.ManyToManyField(User, through='PostLike', related_name='like_posts_set',)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        'Tag', verbose_name='해시태그 목록', related_name="posts", blank=True,
    )

    def __str__(self):
        return f'author: {self.author}, content: {self.content}, like_users: {self.like_users}, created:{self.created}'


    def _save_html(self):
        """
        content 속성의 값을 사용해서 해시태그에 해당하는 문자열을 a태그로 바꾸어 줌
        :return: 해시태그가 a태그로 변환된 HTML
        """
        # 자신의 content_html에 #Python -> <a ~>로 변환된 문자열을 저장
        self.content_html = re.sub(
            self.TAG_PATTERN,
            r'<a href="/explore/tags/\g<1>">#\g<1></a>',
            self.content,
        )

    def _save_tags(self):
        """
        content에 포함된 해시태그 문자열 (ex. #Python)의 Tag를 만들고,
        자신의 tags Many-to-many field에 추가한다.
        :return:
        """
        # Post 객체가 저장될 때, content 값을 분석해서
        # 자신의 tags항목을 적절히 채워줌
        # ex) #Django #Python이 온 경우
        # post.tags.all() 시
        # name이 Django, Python인 Tag 2개 QuerySet이 리턴되어야 함

        # instance, created = Tag.objects.get_or_create(속성)
        # ManyToManyField.set

        tag_name_list = re.findall(self.TAG_PATTERN, self.content)

        # self.tags.clear()

        # for tag_name in tag_name_list:
        #     tag = Tag.objects.get_or_create(name=tag_name)[0]
        #     self.tags.add(tag)

        tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tag_name_list]
        self.tags.set(tags)

        # self.content = content_html
        # print("알고싶은 정보2", self.content)
        # self.save()

    def save(self, *args, **kwargs):
        self._save_html()
        super().save(*args, **kwargs)
        self._save_tags()

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