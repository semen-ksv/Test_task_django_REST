from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from post_api.models import SimpleUser


class AuthViewsTests(APITestCase):

    def setUp(self):
        self.username = 'sem'
        self.password = 'secretpas2000'
        self.data = {
            'username': self.username,
            'password': self.password
        }

    def test_current_user(self):

        # URL using path name
        url = reverse('token_obtain_pair')

        # Create a user in order to authentication works
        user = SimpleUser.objects.create_user(username='sem', email='sem@mail.com', password='secretpas2000')
        self.assertEqual(user.is_active, 1, 'Active User')

        # Get token
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

        token = response.data['access']
        print(token)
