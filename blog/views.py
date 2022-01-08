""" Import post model to add/edit and display posts """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CommentForm
from .forms import PostForm


def blog(request):
    """ Blog page to display all available posts """

    posts = Post.objects.all()
    post_count = len(posts)
    template = 'blog/blog.html'
    context = {
        'posts': posts,
        'post_count': post_count
    }
    return render(request, template, context)


def post_detail(request, slug):
    """ Display each Post in detail along with its comments """
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Only our CPB Shop Admin has access to this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added a post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Failed to add blog post. Check if form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """ Edit an existing Post """
    if not request.user.is_superuser:
        messages.error(request, 'Only our CPB Shop Admin has access to this.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Failed to update blog post. Check if form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Only our CPB Shop Admin has access to this.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'post deleted!')
    return redirect(reverse('post_detail'))
