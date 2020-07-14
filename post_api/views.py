from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


class PostView(APIView):
    """Output list of posts"""

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetailView(APIView):
    """Output details of single post"""

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

