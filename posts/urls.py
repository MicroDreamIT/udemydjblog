from django.urls import path, include
from .views import index, edit, delete, show

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('<id>', show, name='show'),
    path('<id>/edit', edit, name='edit'),
    path('<id>/', delete, name='delete'),
]