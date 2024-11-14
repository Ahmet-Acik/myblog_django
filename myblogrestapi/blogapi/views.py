from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer


@api_view(['GET'])
def index(request):
    return Response({"message": "Welcome to the blog API!"})

@api_view(['GET'])
def get_posts(request):
    get_posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(get_posts, many=True)
    return Response(serializer.data, status=200)
