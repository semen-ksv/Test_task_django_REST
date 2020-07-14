from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """List of Posts"""

    class Meta:
        model = Post
        fields = ('title', 'date_posted', 'author', 'like')


class PostDetailSerializer(serializers.ModelSerializer):
    """Full post with content"""

    class Meta:
        model = Post
        fields = '__all__'
