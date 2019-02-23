from django.urls import path
from posts.api.views import IndexApi, ShowApi, UpdateApi, DeleteApi, CreateApi

urlpatterns = [
    path('', IndexApi.as_view(), name='indexApi'),
    path('create/', CreateApi.as_view(), name='createApi'),
    path('<str:slug>/', ShowApi.as_view(), name='showApi'),
    path('<str:slug>/edit/', UpdateApi.as_view(), name='updateApi'),
    path('<str:slug>/delete/', DeleteApi.as_view(), name='deleteApi'),
]
