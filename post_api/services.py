from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now

from .models import Like, SimpleUser


def add_like(post, user):
    """Make like for post"""

    obj_type = ContentType.objects.get_for_model(post)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, object_id=post.id, user=user)
    return like


def remove_like(post, user):
    """Remove like from post"""

    obj_type = ContentType.objects.get_for_model(post)
    Like.objects.filter(
        content_type=obj_type, object_id=post.id, user=user
    ).delete()


def is_fan(post, user) -> bool:
    """Check did `user` liked `post"""

    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(post)
    likes = Like.objects.filter(
        content_type=obj_type, object_id=post.id, user=user)
    return likes.exists()


def count_likes(all_likes, slug1, slug2) -> dict:
    """Count likes according provided days"""

    response = {}
    for like in all_likes:
        date_of_like = str(like.date_like)
        if date_of_like in response:
            response[date_of_like] += 1
        else:
            response.update({date_of_like: 1})

    all_likes = len(all_likes)  # show all number of likes for asked period

    return {f'all likes at {slug1} to {slug2}': all_likes,
            "daily likes": response}


def user_request_middleware(get_response):
    """middleware for checking action user and request to server"""

    def process_response(request):
        response = get_response(request)
        if request.user.is_authenticated:
            # Update last request time after request finished processing.
            SimpleUser.objects.filter(pk=request.user.pk).update(last_request=now())
        return response
    return process_response