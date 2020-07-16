from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json
from ..models import Post, SimpleUser
from ..serializers import PostSerializer, PostDetailSerializer
from rest_framework_simplejwt.tokens import RefreshToken

client = APIClient()
user = SimpleUser()

class GetAllPostsTest(APITestCase):
    """Test module for GET all posts API"""

    def setUp(self):
        self.new_user = SimpleUser.objects.create(username='Sem')
        self.post = Post()
        self.post.title = 'Test post'
        self.post.content = 'Content from post'
        self.post.author = self.new_user
        self.post.save()

    def test_get_all_post(self):
        # get API response
        response = client.get(reverse('all-post'))
        # get data from db
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePostTest(APITestCase):
    """ Test module for GET single post API """

    def setUp(self):
        self.new_user = SimpleUser.objects.create(username='Sem')
        self.post = Post()
        self.post.title = 'Test post'
        self.post.content = 'Content from post'
        self.post.author = self.new_user
        self.post.save()

    def test_get_single_post(self):
        response = client.get(reverse('post-detail', kwargs={'slug': self.post.slug}))
        post = Post.objects.get(slug=self.post.slug)
        serializer = PostDetailSerializer(post)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_post(self):
        # get wrong slug
        response = client.get(
            reverse('post-detail', kwargs={'slug': self.post.slug + "1"}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPostTest(APITestCase):
    """ Test module for creating and adding new post """

    def setUp(self):
        self.new_post = {
            "title": "new_post",
            "content": "text content",
            'author': 1
        }
        self.username = 'sem'
        self.password = 'secretpas2000'
        self.data = {
            'username': self.username,
            'password': self.password
        }

    def test_create_post(self):
        # Create a user and get token
        self.user = SimpleUser.objects.create_user(username=self.username, password=self.password)
        refresh = RefreshToken.for_user(self.user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        response = client.post(
            reverse('post-create'),
            data=json.dumps(self.new_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_unauthorized(self):
        response = client.post(
            reverse('post-create'),
            data=json.dumps(self.new_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UpdateSinglePostTest(APITestCase):
    """ Test module for updating an existing post """

    def setUp(self):
        self.updated_post = {
            "title": "new_post",
            "content": "text content",
        }
        self.username = 'sem'
        self.password = 'secretpas2000'
        self.data = {
            'username': self.username,
            'password': self.password
        }
        self.user = SimpleUser.objects.create_user(
            username=self.username,
            password=self.password
        )

        self.post = Post.objects.create(
            title='Test post',
            content='Content from post',
            author=self.user,
        )
        # get token
        refresh = RefreshToken.for_user(self.user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')


    def test_post_update(self):
        response = client.put(
            reverse('post-update', kwargs={'slug': self.post.slug}),
            data=json.dumps(self.updated_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_post_invalid(self):
        response = client.put(
            reverse('post-update', kwargs={'slug': self.post.slug + '1'}),
            data=json.dumps(self.updated_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DeleteSinglePostTest(APITestCase):
    """ Test module for deleting an existing post """

    def setUp(self):
        self.user = SimpleUser.objects.create_user(
            username='sem',
            password='secretpas2000'
        )
        self.post = Post.objects.create(
            title='Test post',
            content='Content from post',
            author=self.user,
        )
        # get token
        refresh = RefreshToken.for_user(self.user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_delete_post(self):
        response = client.delete(
            reverse('post-delete', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
