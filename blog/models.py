""" Models for Blog app """

from django.db import models


class Blog(models.Model):
    """ Blog class model """

    class Meta:
        """ Meta class for Blog model """
        verbose_name_plural = 'Blogs'

    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        """ Short blog info def """
        return self.body[:100]

    def pub_date_pretty(self):
        """ Formatted publish date def """
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return str(self.title)
