""" Admin for Blog app"""

from django.contrib import admin
from .models import Blog


admin.site.register(Blog)
