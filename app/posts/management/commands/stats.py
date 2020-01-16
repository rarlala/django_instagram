import os

from django.core.management import BaseCommand
from django.utils import timezone

from config.settings import MEDIA_ROOT
from posts.models import Post, PostComment, Tag


class Command(BaseCommand):
    help = 'Posts, Comments, Tags 개수 출력'

    def handle(self, *args, **options):
        now = timezone.now()
        # instagram/.media/now.txt
        # 파일이 이미 있다면 다음줄에 기록
        # 파일이 없다면 파일을 생성하고 기록

        with open(os.path.join(MEDIA_ROOT, 'now.txt'), 'at') as f:
            time_str = f'Now: + {timezone.localtime(now).strftime("%Y-%m-%d %H:%M:%S")}\n'
            f.write(time_str)