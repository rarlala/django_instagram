import os

from django.core.management import BaseCommand
from django.utils import timezone

from config.settings import MEDIA_ROOT
from posts.models import Post, PostComment, Tag


class Command(BaseCommand):
    help = 'Posts, Comments, Tags 개수 출력'

    def handle(self, *args, **options):

        print('''
            전체 Posts: {}개,
            전체 Comments: {}개,
            전체 Tags: {}개
        '''.format(Post.objects.all().count(), PostComment.objects.all().count(), Tag.objects.all().count()))