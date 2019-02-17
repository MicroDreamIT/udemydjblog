from django.db import models
from django.db.models.signals import pre_save

# Create your models here.
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=191)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" % (slug, Post.objects.last().id + 1)
    instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Post)
