from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from comments.forms import CommentForm
from comments.models import Comment
from posts.forms import PostForm
from posts.models import Post


# public method
def category(request, name):
    return render(request,
                  'index.html',
                  {
                      'posts': Post.objects.filter(category__name=name.replace('-', ' '))
                  })


def index(request):
    query = request.GET.get('q')
    posts = Post.objects
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(description__icontains=query)).distinct()
    else:
        posts = Post.objects

    posts = posts.order_by('-created_at')
    return render(request,
                  'index.html',
                  {'posts': posts})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            __post_save(form, request, 'blog has been created')  # sub method
        else:
            messages.error(request, 'please try again')
            return render(request, 'create.html', {'form': form})

    return render(request,
                  'create.html',
                  {'form': PostForm})


def show(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments
    initial_data = {
        'content_type': post.get_content_type,
        'object_id': post.id
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)

    if comment_form.is_valid():
        # print(comment_form.cleaned_data, '\n', comment_form)
        c_type = comment_form.cleaned_data.get('content_type')
        object_id = comment_form.cleaned_data.get('object_id')
        content_data = comment_form.cleaned_data.get('comments')
        content_type = ContentType.objects.get(model=c_type)
        parent_qs = __check_and_return_parent(request.POST.get('parent_id'))

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=object_id,
            comments=content_data,
            parent=parent_qs if parent_qs.id else None
        )

    return render(request, 'show.html',
                  {
                      'post': post,
                      'comments': comments,
                      'comment_form': comment_form
                  })


def edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            __post_save(form, request, 'blog has been updated')  # sub method
        else:
            messages.error(request, 'Please try again')

    return render(request, 'edit.html',
                  {
                      'form': form,
                      'post': post
                  })


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


def __check_and_return_parent(param):
    try:
        parent_id = int(param)
    except:
        parent_id = None

    if parent_id:
        parent_qs = get_object_or_404(Comment, id=parent_id)
    else:
        parent_qs = None

    return parent_qs
