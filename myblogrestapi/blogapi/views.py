from rest_framework.decorators import api_view

"""
    Views for the blog API.
    This module contains the following views:
    - index: A welcome message for the blog API.
    - get_posts: Retrieve all blog posts.
    - create_post: Create a new blog post (requires authentication).
    - post_detail: Retrieve, update, or delete a blog post by its primary key.
    Functions:
    - index(request): Returns a welcome message.
    - get_posts(request): Returns a list of all blog posts.
    - create_post(request): Creates a new blog post if the request data is valid.
    - post_detail(request, pk): Retrieves, updates, or deletes a blog post by its primary key.
    Dependencies:
    - rest_framework.decorators.api_view
    - rest_framework.response.Response
    - rest_framework.status
    - .models.BlogPost
    - .serializers.BlogPostSerializer
    - rest_framework.permissions.IsAuthenticated
    - rest_framework.decorators.permission_classes
"""
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import BlogPostSerializer


@api_view(["GET"])
def index(request):
    return Response({"message": "Welcome to the blog API!"})


@api_view(["GET"])
def get_posts(request):
    get_posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(get_posts, many=True)
    return Response(serializer.data, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
    try:
        post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BlogPostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
