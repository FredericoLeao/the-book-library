from django.test import TestCase
from rest_framework.test import APIClient
from account.models import User
import json

class AccountAppTestCase(TestCase):
    def setUp(self) -> None:
        nu = User()
        nu.username='testuser'
        nu.email='testemail'
        nu.set_password('testpass')
        nu.is_superuser = True
        nu.save()
        return super().setUp()

    def test_api(self):
        client = APIClient()
        res = client.get('/api/accounts/')
        self.assertEqual(res.status_code, 401)

        # Test JWT Authorization
        # First authenticate and get the token
        res_login = client.post('/api/login/',
                                json.dumps({ 'email': 'testemail', 'password': 'testpass'}),
                                content_type='application/json')
        self.assertEqual(res_login.status_code, 200)
        access_token = res_login.json()['access']

        # Use the token to access protected endpoint
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        res = client.get('/api/accounts/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)
