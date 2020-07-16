from rest_framework import serializers

from .models import Post, Like, SimpleUser
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


class SimpleUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = SimpleUser
        fields = ('id', 'username', 'last_login', 'last_request')




# from django.contrib.auth import authenticate, user_logged_in
#
# from rest_framework import serializers
# from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler
#
# class JWTSerializer(JSONWebTokenSerializer):
#     def validate(self, attrs):
#         credentials = {
#             self.username_field: attrs.get(self.username_field),
#             'password': attrs.get('password')
#         }
#
#         if all(credentials.values()):
#             user = authenticate(request=self.context['request'], **credentials)
#
#             if user:
#                 if not user.is_active:
#                     msg = 'User account is disabled.'
#                     raise serializers.ValidationError(msg)
#
#                 payload = jwt_payload_handler(user)
#                 user_logged_in.send(sender=user.__class__, request=self.context['request'], user=user)
#
#                 return {
#                     'token': jwt_encode_handler(payload),
#                     'user': user
#                 }
#             else:
#                 msg = 'Unable to log in with provided credentials.'
#                 raise serializers.ValidationError(msg)
#         else:
#             msg = 'Must include "{username_field}" and "password".'
#             msg = msg.format(username_field=self.username_field)
#             raise serializers.ValidationError(msg)