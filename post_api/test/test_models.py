from django.contrib.contenttypes.models import ContentType
from rest_framework.test import APITestCase
from time import time
from post_api.models import Post, SimpleUser, Like


class TestPostModel(APITestCase):
    """Post model testing fields, slug generations"""

    def setUp(self) -> None:
        self.user = SimpleUser.objects.create_user(
            username='sem',
            password='secretpas2000'
        )
        self.post = Post.objects.create(
            title='Test post',
            content='Content from post',
            author=self.user,
        )

    def test_post_fields(self):
        record_post = Post.objects.get(slug=self.post.slug)
        self.assertEqual(record_post, self.post)

        record2_post = Post.objects.get(id=self.post.id)
        self.assertEqual(record2_post, self.post)

        record3_post = Post.objects.get(title=self.post.title)
        self.assertEqual(record3_post, self.post)

    def test_generate_slug(self):
        self.assertEqual(Post.generate_slug('Test post'), f'test-post_{str(int(time()))}')

    def test_likes_fields(self):
        content = ContentType.objects.get(
            app_label='post_api',
            model='post'
        )
        like = Like.objects.create(
            user=self.user,
            content_type=content,
            object_id=self.post.id,
        )
        record_comment = Like.objects.get(pk=like.pk)
        self.assertEqual(record_comment, like)
