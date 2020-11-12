import uuid
from django.db import models
from django.conf import settings
from subscription.models import Subscription
from django.contrib.auth.models import User


class Package(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    date = models.DateField(auto_now_add=True)

    def _generate_order_number(self):
        """
        a method to generate unique package number with UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ override teh save method to save uuid number
        if hasn't been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class PackageLineItem(models.Model):
    order = models.ForeignKey(Package, null=False, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, null=False, on_delete=models.CASCADE )
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.subscription.name, self.subscription.price)
