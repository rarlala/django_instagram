from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializer, PostCreateSerializer


class PostListCreateAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostImageCreateAPIView(APIView):
    def post(self, request, pk):
        # 여러장의 이미지를 받아서
        # 특정 pk에 해당하는 Post에 연결되는 PostImage를 생성
        # /posts/1/images/
        post = Post.objects.get(pk=pk)
        for image in request.data.getlist('image'):
            post.postimage_set.create(image=image)

        serializer = PostCreateSerializer(post)
        return Response(serializer.data)