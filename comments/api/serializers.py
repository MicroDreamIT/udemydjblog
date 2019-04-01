from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField

    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'parent',
            'content',
            'created_at'
        ]

    def get_reply_count(self, obj):
        if obj.parent:
            return obj.children.count()
