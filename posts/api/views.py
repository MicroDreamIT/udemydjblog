from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from posts.api.serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer
from posts.models import Post


class CreateApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class IndexApi(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ShowApi(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class UpdateApi(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'slug'


class DeleteApi(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
