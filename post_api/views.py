from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404

from .models import Post, Like, SimpleUser
from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, \
    PostUpdateSerializer, SimpleUserSerializer
from .services import add_like, remove_like, count_likes


class PostView(ListAPIView):
    """Output list of posts"""

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(APIView):
    """Output details of single post for all users"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class PostCreateView(APIView):
    """Add single post for authenticated users"""

    # authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create a new post
        data = request.data
        data.update({'author': str(request.user.id)})
        post = PostCreateSerializer(data=data)
        if post.is_valid(raise_exception=True):
            post.author_id = request.user.id
            saved_post = post.save()
            return Response({"success": f"Article '{saved_post.title}' created successfully"}, status=201)
        else:
            return Response(status=404)


class PostUpdateView(APIView):
    """Update single post for authenticated users"""

    # authentication_classes = (JWTAuthentication,)
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
            }, status=204)
        else:
            return Response(status=404)


class PostDeleteView(APIView):
    """Deleting single post for admin users """

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, slug):
        # Get post with this slug
        post = get_object_or_404(Post.objects.all(), slug=slug)
        post.delete()
        return Response({
            "message": f"Article with id `{post.title}` has been deleted."
        }, status=204)


class PostAddLikeView(APIView):
    """Add like for post using slug of post"""

    # authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        user = request.user
        if user.is_authenticated:
            add_like(post, user)
            return Response({"success": f"Post '{post.title}' added like from {user.username}"}, status=201)
        else:
            return Response({"success": f"Please login fo like the post"}, status=401)


class PostRemoveLikeView(APIView):
    """Delete like from post using slug of post"""

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        user = request.user
        if user.is_authenticated:
            remove_like(post, user.id)
            return Response({"success": f"From  '{post.title}' removed like by {user.username}"}, status=201)
        else:
            return Response({"success": f"Please login fo unlike the post"}, status=401)


class DayLikeAnalyticsView(APIView):
    """Output likes related with one day using rout 'date_YYYY-MM-DD'"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, slug):
        all_likes = Like.objects.filter(date_liked=slug).count()
        return Response({"daily likes": {
            slug: all_likes}},
            status=201)


class RangeDaysLikeAnalyticsView(APIView):
    """
    Output likes related with range of days what get from url slug using rout 'date-from_YYYY-MM-DD-date-to_YYYY-MM-DD'
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, slug1, slug2):
        all_likes = Like.objects.filter(date_liked__gte=slug1, date_liked__lte=slug2)
        response = count_likes(all_likes, slug1, slug2)
        return Response(response, status=201)


class SimpleUserListView(ListAPIView):
    """Show information about users id, username, last_login, last_request"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializer
