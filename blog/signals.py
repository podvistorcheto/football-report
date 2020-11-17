import django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Article


@receiver(post_save, sender=User)
def create_article(sender, instance, created, **kwargs):
    if created:
        Article.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_article(sender, instance, **kwargs):
    instance.article.save()