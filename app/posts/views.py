from django.shortcuts import render, redirect

from posts.models import Post


def post_list(request):
    """
    1. 로그인 완료 후 이 페이지로 이동하도록 함
    2. index에 접근할 때 로그인이 되어있다면, 이 페이지로 이동하도록 함
        로그인 되어있는지 확인:
            User.is_authenticated가 True인지 체크

    URL :       /post/ (posts.urls를 사용, config.urls에서 include)
    Template : templates/posts/post-list.html
                <h1>Post List</h1>

    'posts'라는 키로 모든 Post QuerySet을 전달
    순서는 pk의 역순
    그리고 전달받은 QuerySet을 순회하며 적절히 Post내용을 출력
    """

    posts = Post.objects.order_by('-pk')

    context = {
        'posts': posts,
    }

    return render(request, 'posts/post-list.html', context)