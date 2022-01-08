""" Models for Blog app """

from django.db import models


class Blog(models.Model):
    """ Blog class model """
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='')

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    """ Post class model """
    blog = models.ForeignKey(
        Blog, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='')
    author = models.CharField(max_length=255)
    intro = models.TextField()
    article = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    """ Comment class model """
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    comment_desc = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s - %s' % (self.post.title, self.name, self.date_added)
