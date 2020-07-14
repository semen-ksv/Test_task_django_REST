from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """List of Posts"""

    class Meta:
        model = Post
        fields = ('slug', 'title', 'date_posted', 'like')


class PostDetailSerializer(serializers.ModelSerializer):
    """Full post with content"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    """Create post"""

    class Meta:
        model = Post
        fields = ('title', 'content', 'author')




class PostUpdateSerializer(serializers.ModelSerializer):
    """Create post"""

    class Meta:
        model = Post
        fields = ('title', 'content')



# {
# "title": "Third post from API",
# "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas pulvinar, quam sed viverra hendrerit, massa urna varius est, rutrum tempor ante justo et neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus nec sagittis justo, vel tincidunt sem. Etiam tincidunt bibendum molestie.",
# "author": "1"
# }