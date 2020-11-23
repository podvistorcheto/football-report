from django.test import TestCase
from .forms import PackageForm


class PackageFormTest(TestCase):
    """ method to check if the form has valid input"""
    def test_create_order_with_required_fields_filled(self):
        form = PackageForm({
            'full_name': 'test',
            'email': 'test@expample.com',
            'phone_number': '0123456789'})
        self.assertTrue(form.is_valid())

    """method to check if the form has just one missing field"""
    def test_feedback_error_field_empty(self):
        form = PackageForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])
