from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer


class PostView(ListAPIView):
    """Output list of posts"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(APIView):
    """Output details of single post"""

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class PostCreateView(APIView):
    """Add single post for authenticated users"""
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):    #TODO:change saving for author
        post = PostCreateSerializer(data=request.data)
        print(post)
        print(post.is_valid(), 'crate')
        if post.is_valid(raise_exception=True):
            print(post, 'in if')
            # post = request.user.id
            saved_post = post.save()
            print(saved_post, 'save')
            return Response({"success": f"Article '{saved_post.title}' created successfully"}, status=201)
        else:
            return Response(status=404)

