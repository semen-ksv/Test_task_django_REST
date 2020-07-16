from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post, SimpleUser
from ..serializers import PostSerializer, PostDetailSerializer


client = Client()
user = SimpleUser()


class GetAllPostsTest(TestCase):
    """ Test module for GET all posts API """

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

class GetSinglePostTest(TestCase):
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

