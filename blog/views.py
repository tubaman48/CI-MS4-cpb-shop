""" blog views """

from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    """ A view to show a summary of blogs """
    blogs = Blog.objects
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    """ A view to show individual blog details """
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blogdetail})
