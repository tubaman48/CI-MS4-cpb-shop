""" Review Admin """

from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """ ReviewAdmin class """
    list_display = (
        'username',
        'title',
        'body',
        'firstcreated',
        'lastedited',
    )


admin.site.register(Review, ReviewAdmin)
