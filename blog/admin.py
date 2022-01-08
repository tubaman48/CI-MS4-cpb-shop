""" Admin for Blog app"""

from django.contrib import admin
from .models import Blog, Post, Comment


class BlogAdmin(admin.ModelAdmin):
    """ BlogAdmin class model """
    list_display = (
        'title',
    )


class PostAdmin(admin.ModelAdmin):
    """ PostAdmin class model """
    list_display = (
        'title',
        'intro',
        'article',
        'image',
        'date_added',
        'author'
    )


class CommentAdmin(admin.ModelAdmin):
    """ CommentAdmin class model """
    list_display = (
        'name',
        'comment_desc',
        'date_added',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
