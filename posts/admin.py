from django.contrib import admin
from posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_editable = ['title']
    search_fields = ['title', 'description']
    list_display_links = ['id']
