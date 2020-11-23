from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class CartViewTest(TestCase):
    '''
    a method to test cart page doesnt appert for not logged in user
    '''
    def test_view_cart_page(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 302)


class AddToCartTestView(TestCase):
    """
    a method to check is the cart template loads
    if the user is logged in
    """

    def initialise_user_session(self):
        self.credentials = {
            'user': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.client.post('/login/', self.credentials, follow=True)

    """ method to load the card if session initialised"""
    def test_add_to_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 302)


