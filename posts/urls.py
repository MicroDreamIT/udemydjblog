from django.urls import path
from .views import (index, edit, delete, show, create)

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', show, name='show'),
    path('create/', create, name='create'),
    path('<int:id>/edit/', edit, name='edit'),
    path('<int:id>/delete/', delete, name='delete'),
]