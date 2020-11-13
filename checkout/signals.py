from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import PackageLineItem

@receiver(post_save, sender=PackageLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.save()

@receiver(post_delete, sender=PackageLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.save()