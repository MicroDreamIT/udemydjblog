from django.http import HttpResponse, Http404
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
            form = PostForm(request.POST, request.FILES or None)
            if form.is_valid():
                __post_save(form, request, 'blog has been created')  # sub method
            else:
                messages.error(request, 'please try again')
                return render(request, 'create.html', {'form': form})

    return render(request, 'create.html', {'form': PostForm})


def show(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'show.html', {'post': post})


def edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            __post_save(form, request, 'blog has been updated')  # sub method
        else:
            messages.error(request, 'Please try again')

    return render(request, 'edit.html', {'form': form, 'post': post})


def delete(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'successfully deleted')
    return redirect('posts:index')


# private methods
def __post_save(form, request, message):
    if request.user.is_authenticated:
        form.user = request.user
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, message)
    else:
        raise Http404
