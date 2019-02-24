from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView

from posts.api.serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer
from posts.models import Post


class CreateApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class IndexApi(ListAPIView):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer


class ShowApi(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class UpdateApi(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteApi(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
