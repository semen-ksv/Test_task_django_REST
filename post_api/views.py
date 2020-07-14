from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer


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


class PostUpdateView(APIView):
    """Update single post for authenticated users"""
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, slug):
        # Get post with this slug
        saved_post = get_object_or_404(Post.objects.all(), slug=slug)
        updated_post_data = request.data
        serializer = PostUpdateSerializer(instance=saved_post, data=updated_post_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
            return Response({
                "success": f"Article '{post_saved}' updated successfully"
            })
        else:
            return Response(status=404)


class PostDeleteView(APIView):
    """Update single post for authenticated users"""
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, slug):
        # Get post with this slug
        article = get_object_or_404(Post.objects.all(), slug=slug)
        article.delete()
        return Response({
            "message": f"Article with id `{article.title}` has been deleted."
        }, status=204)
