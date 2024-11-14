from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
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
    