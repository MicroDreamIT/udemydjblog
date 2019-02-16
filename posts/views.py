from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from posts.forms import PostForm
from posts.models import Post


# public method
def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            __post_save(form, request, 'blog has been created')  # sub method
        else:
            messages.error(request, 'please try again')
            return render(request, 'create.html', {'form': form})

    return render(request, 'create.html', {'form': PostForm})


def show(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'show.html', {'post': post})


def edit(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            __post_save(form, request, 'blog has been updated')  # sub method
        else:
            messages.error(request, 'Please try again')

    return render(request, 'edit.html', {'form': form, 'post': post})


def delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'successfully deleted')
    return redirect('posts:index')


# private methods
def __post_save(form, request, message):
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, message)
