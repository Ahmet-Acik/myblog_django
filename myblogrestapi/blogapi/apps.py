from django.apps import AppConfig
"""
This module defines the configuration for the 'blogapi' application.

Classes:
    BlogapiConfig(AppConfig): Configuration class for the 'blogapi' application.
"""


class BlogapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapi'
