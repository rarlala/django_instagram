from django.shortcuts import render, redirect

from posts.forms import PostCreateForm
from posts.models import Post, PostLike, PostImage, PostComment


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


def post_like(request, pk):
    """
    pk가 pk인 Post와 (변수명 post사용)
    request.user로 전달되는 User(변수명 user사용)에 대해

    1. PostLike(post=post, user=user)인 객체가 존재하는지 확인
        없다면 생성한다.
        이미 있다면, 삭제한다.
    2. 완료 후 posts:post-list로 redirect한다.

    URL : /posts/<pk>/like/
    """

    post = Post.objects.get(pk=pk)
    user = request.user
    print('post')
    print('user')

    post_like_qs = PostLike.objects.filter(post=post, user=user)

    if post_like_qs.exists():
        post_like_qs.delete()

    else:
        PostLike.objects.create(post=post, user=user)

    return redirect('posts:post-list')


def post_create(request):
    """
    URL: /posts/create/
    Template: /posts/post-create.html

    forms.PostCreateForm을 사용

    """
    if request.method == 'POST':
        """
        새 Post 생성
        user는 request.user
        전달받는 데이터 : image, text
            image는 request.FILES에 있음
            text는 request.POST에 있음
        Post를 생성
            request.user와 text를 사용
        PostImage를 생성
            post와 전달받은 image를 사용
        모든 생성이 완료되면 posts:post-list로 redirect
        """
        text = request.POST['text']
        images = request.FILES.getlist('image')

        post = Post.objects.create(
            author=request.user,
            content=text,
        )

        for image in images:
            post.postimage_set.create(image=image)

        return redirect('posts:post-list')
    else:
        form = PostCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'posts/post-create.html', context)


def comment_create(request, post_pk):
    # URL: /posts/<int:post_pk>/comments/create/
    # Template: 없음 (post_list.html 내에 Form을 구현)
    #  post-list.html 내부에서, 각 Post마다 자신에게 연결된 PostComment목록을 보여주도록 함
    #   보여주는 형식은
    #   <ul>
    #       <li><b>작성자명</b><span>내용</span>/li>
    #       <li><b>작성자명</b><span>내용</span>/li>
    #   </ul>
    # Form: post.forms.CommentCreateForm

    comment = request.POST['comment']

    post = Post.objects.get(pk=post_pk)

    PostComment.objects.create(post=post, author=request.user, content=comment)
    # post.postcomment_set.creata(post=post, author=request.user, content=comment)

    return redirect('posts:post-list')
