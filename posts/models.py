from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from comments.models import Comment


class Category(models.Model):
    name = models.CharField(max_length=191, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=191)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=0, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=0, on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def comments(self):
        obj = self
        qs = Comment.objects.filter_by_model(obj)
        return qs

    @property
    def get_content_type(self):
        obj = self
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return content_type

    def __str__(self):
        return self.title


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" % (slug, Post.objects.last().id + 1)
    instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Post)
