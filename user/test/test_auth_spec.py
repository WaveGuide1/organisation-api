from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import User


class UserTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('user-login')
        self.user_detail_url = lambda userId: reverse('user-detail', kwargs={'userId': userId})
        self.user_data = {
            'email': 'testuser@example.com',
            'firstName': 'Test',
            'lastName': 'User',
            'password': 'password123'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_register_user(self):
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('accessToken', response.data['data'])
        self.assertIn('user', response.data['data'])

    def test_login_user(self):
        response = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('accessToken', response.data['data'])

    def test_user_detail(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.get(self.user_detail_url(self.user.userId))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['email'], self.user.email)
