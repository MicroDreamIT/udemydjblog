from rest_framework.serializers import ModelSerializer, SerializerMethodField

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
    user = SerializerMethodField()

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
