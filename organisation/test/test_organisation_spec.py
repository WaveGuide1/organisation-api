from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from user.models import User
from organisation.models import Organisation
from rest_framework_simplejwt.tokens import RefreshToken


class OrganisationTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'email': 'testuser@example.com',
            'firstName': 'Test',
            'lastName': 'User',
            'password': 'password123'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.org_data = {
            'name': 'Test Organisation'
        }
        self.organisation = Organisation.objects.create(name=self.org_data['name'])
        self.organisation.users.add(self.user)

        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        self.organisation_list_url = reverse('organisation-list')
        self.organisation_detail_url = lambda orgId: reverse('organisation-detail', kwargs={'orgId': orgId})
        self.organisation_add_user_url = lambda orgId: reverse('organisation-add-user', kwargs={'orgId': orgId})

    def test_list_organisations(self):
        response = self.client.get(self.organisation_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']['organisations']), 1)

    def test_create_organisation(self):
        response = self.client.post(self.organisation_list_url, self.org_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['name'], self.org_data['name'])

    def test_get_organisation_detail(self):
        response = self.client.get(self.organisation_detail_url(self.organisation.orgId))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], self.organisation.name)

    def test_add_user_to_organisation(self):
        new_user_data = {
            'email': 'newuser@example.com',
            'firstName': 'New',
            'lastName': 'User',
            'password': 'password123'
        }
        new_user = User.objects.create_user(**new_user_data)

        response = self.client.post(self.organisation_add_user_url(self.organisation.orgId), {
            'userId': str(new_user.userId)
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(new_user, self.organisation.users.all())
