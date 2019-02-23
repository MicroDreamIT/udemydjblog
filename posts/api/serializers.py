from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'category'
        ]


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'category'
        ]


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'created_at'
        ]
