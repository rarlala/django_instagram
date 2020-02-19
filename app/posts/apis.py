from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post, PostComment
from posts.serializers import PostSerializer, PostCreateSerializer, PostImageCreateSerializer, PostCommentSerializer, \
    PostCommentCreateSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# class PostListCreateAPIView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             instance = serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostImageCreateAPIView(APIView):
    def post(self, request, pk):
        # 여러장의 이미지를 받아서
        # 특정 pk에 해당하는 Post에 연결되는 PostImage를 생성
        # /posts/1/images/
        post = Post.objects.get(pk=pk)
        for image in request.data.getlist('image'):
            data = {'image' : image}
            serializer = PostImageCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save(post=post)

        serializer = PostSerializer(post)
        return Response(serializer.data)

class PostCommentListCreateAPIView(APIView):
    # URL: /api/posts/1/comment

    def get(self, request, post_pk):
        # post_pk에 해당하는 Post에 연결된 PostComment 전체 가져오기
        post = get_object_or_404(Post, pk=post_pk)
        comments = post.postcomment_set.all()

        serializer = PostCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_pk):
        # post_pk에 해당하는 Post에 연결되는 PostComment 생성하기
        # content : request.data
        # author : request.user
        # post: URL params
        post = get_object_or_404(Post, pk=post_pk)
        serializer = PostCommentCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post=post, author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)