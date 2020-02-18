from rest_framework import serializers

from posts.models import Post


# List, Retrieve, Update, Create할 때 serializer가 필요
# Post일 때는, Postserializer , PostDetailSerializer, PostUpdateSerializer, PostCreateSerializer로 분리

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'pk',
            'content',
        )
