from django.test import TestCase


# unit tests for the blog app
class TestDjango(TestCase):

    def test_this_thing1(self):
        self.assertEqual(1, 1)

    def test_this_thing2(self):
        self.assertEqual(1, 0)

    def test_this_thing3(self):
        self.assertEqual(1, )

    def test_this_thing4(self):
        self.assertEqual(1, 4)
