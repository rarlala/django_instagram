from rest_framework import serializers

from members.serializers import UserSerializer
from posts.models import Post, PostImage


# List, Retrieve, Update, Create할 때 serializer가 필요
# Post일 때는, Postserializer , PostDetailSerializer, PostUpdateSerializer, PostCreateSerializer로 분리

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'content',
            'postimage_set',
        )


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'content',
        )

    def to_representation(self, instance):
        return PostSerializer(instance).data
