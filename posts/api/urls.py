from django.urls import path
from posts.api.views import IndexApi

urlpatterns = [
    path('', IndexApi.as_view(), name='indexApi')
]
