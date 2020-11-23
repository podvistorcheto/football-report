from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileAccessTests(TestCase):
    """
    a method to check is the cart template loads
    if the user is logged in
    """
    def initialise_user_session(self):
        self.credentials = {
            'user': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.client.post('/accounts/login/', self.credentials, follow=True)
    
    """
    testing load of pages in profiles app
    """
    def test_register_page_load(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/')

    def test_login_page_load(self):
        response = self.client.get('/accouts/login/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/')

    def test_logout_page_load(self):
        response = self.client.get('accounts/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/')
