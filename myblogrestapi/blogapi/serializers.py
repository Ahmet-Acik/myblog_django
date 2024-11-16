from rest_framework import serializers
from .models import BlogPost

"""
This module contains the serializer for the BlogPost model.
BlogPostSerializer inherits from rest_framework.serializers.ModelSerializer.
ModelSerializer is a shortcut for creating serializers for Django models.


Classes:
    BlogPostSerializer: A serializer for the BlogPost model that includes all fields.
    class Meta: Specifies the model and fields to include in the serializer.
    model: The model to serialize.
    fields: The fields to include in the serializer.
    
"""


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
