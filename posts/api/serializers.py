from rest_framework.serializers import ModelSerializer, SerializerMethodField

from posts.models import Post, Category
from comments.api.serializers import CommentSerializer
from comments.models import Comment


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
    user = SerializerMethodField()
    category = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'user',
            'description',
            'created_at',
            'user',
            'category'
        ]

    def get_user(self, obj):
        return obj.user.username

    def get_category(self, obj):
        return obj.category.name


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

