from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework import permissions

from posts.api.serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer
from posts.models import Post
from posts.api.permissions import IsOwnerOrReadOnly


class CreateApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

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
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteApi(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
