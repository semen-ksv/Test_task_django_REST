from rest_framework import serializers

from .models import Post, Like, SimpleUser
from .services import check_was_post_liked


class PostSerializer(serializers.ModelSerializer):
    """List of Posts"""

    class Meta:
        model = Post
        fields = ('slug', 'title', 'date_posted', 'total_likes')
        read_only_fields = fields

    def check_liked_post(self, post) -> bool:
        """Check did `request.user` liked post"""
        user = self.context.get('request').user
        return check_was_post_liked(post, user)


class PostDetailSerializer(serializers.ModelSerializer):
    """Show full detail of single post with content"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'content', 'date_posted', 'author', 'total_likes')
        read_only_fields = fields


class PostCreateSerializer(serializers.ModelSerializer):
    """Create post"""

    class Meta:
        model = Post
        fields = ('title', 'content', 'author')


class PostUpdateSerializer(serializers.ModelSerializer):
    """Update post"""

    class Meta:
        model = Post
        fields = ('title', 'content')


class SimpleUserSerializer(serializers.ModelSerializer):
    """Show all users with last login and last request date"""

    class Meta:
        model = SimpleUser
        fields = ('id', 'username', 'last_login', 'last_request')
        read_only_fields = fields
