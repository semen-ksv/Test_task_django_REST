from rest_framework import serializers

from .models import Post, Like
from .services import is_fan


class PostSerializer(serializers.ModelSerializer):
    """List of Posts"""

    class Meta:
        model = Post
        fields = ('slug', 'title', 'date_posted', 'total_likes')

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`).
        """
        user = self.context.get('request').user
        return is_fan(obj, user)


class PostDetailSerializer(serializers.ModelSerializer):
    """Full post with content"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'content', 'date_posted', 'author', 'total_likes')


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


class LikeAnalyticsSerializer(serializers.ModelSerializer):
    """List of all Likes"""

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Like
        fields = '__all__'

# {
# "title": "Third post from API",
# "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas pulvinar, quam sed viverra hendrerit, massa urna varius est, rutrum tempor ante justo et neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus nec sagittis justo, vel tincidunt sem. Etiam tincidunt bibendum molestie.",
# "author": "1"
# }