import pytest
from rest_framework.test import APITestCase, APIClient
from django.shortcuts import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

pytestmark = [pytest.mark.django_db]


class UsersTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        password = make_password('12345qwerty')
        self.user = get_user_model().objects.create(
            email='test@test.com',
            password=password,
            is_active=True
        )

        data = {
            "email": self.user.email,
            "password": "12345qwerty"
        }

        url = reverse('jwt-create')

        self.token = 'Bearer ' + self.client.post(
            url,
            data=data,
            format='json'
        ).data['access']

    def test_auth(self):
        url = reverse('some-view')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == 'User view works good'

