import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post, SimpleUser
from ..serializers import PostSerializer

client = Client()
user = SimpleUser()


class GetAllPostsTest(TestCase):
    """ Test module for GET all posts API """

    def setUp(self):
        Post.objects.create(
            title='First title', content='Some Text', author_id=1)
        Post.objects.create(
            title='Second title', content='Some Text', author_id=1)
        Post.objects.create(
            title='Third title', content='Some Text', author_id=1)

    def test_get_all_post(self):
        # get API response
        response = client.get(reverse('PostView'))
        # get data from db
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePuppyTest(TestCase):
    """ Test module for GET single puppy API """
    def setUp(self):
        self.first_post = Post.objects.create(
            title='First title', content='Some Text', author_id=1)
        self.second_post = Post.objects.create(
            title='Second title', content='Some Text', author_id=1)
        self.third_post = Post.objects.create(
            title='Third title', content='Some Text', author_id=1)

    def test_get_single_post(self):
        response = client.get(
            reverse('PostDetailView', kwargs={'slug': self.first_post.slug}))
        puppy = Post.objects.get(slug=self.first_post.slug)
        serializer = PostSerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_post(self):
        response = client.get(
            reverse('PostDetailView', kwargs={'slug': self.ten_post.slug}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)