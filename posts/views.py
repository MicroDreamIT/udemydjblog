from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from posts.forms import PostForm
from posts.models import Post


def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'blog has been created')
        else:
            messages.error(request, 'please try again')
            return render(request, 'create.html', {'form': form})

    return render(request, 'create.html', {'form': PostForm})


# Create your views here.
def show(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'show.html', {'post': post})


# Create your views here.
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'blog has been updated')
        else:
            messages.error(request, 'Please try again')

    return render(request, 'edit.html', {'form': form, 'post': post})


# Create your views here.
def delete(request, id):
    return HttpResponse('delete')
