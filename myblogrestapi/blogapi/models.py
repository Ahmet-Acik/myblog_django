from django.db import models
"""
This module defines the models for the blog API.
Classes:
    BlogPost: A model representing a blog post with a title, body, and timestamps for creation and updates.
"""



# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    