""" Custom Storages for AWS S3 bucket """

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ StaticStorage class """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ MediaStorage class """
    location = settings.MEDIAFILES_LOCATION
