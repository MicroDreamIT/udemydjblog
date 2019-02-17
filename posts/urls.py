from django.urls import path
from .views import (index, edit, delete, show, create)

app_name = 'posts'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('<str:slug>/', show, name='show'),
    path('<str:slug>/edit/', edit, name='edit'),
    path('<str:slug>/delete/', delete, name='delete'),
]
