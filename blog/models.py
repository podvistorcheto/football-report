from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=100)
    article_image = models.ImageField(default="inthenet.jpg", upload_to="article_pics")
    content = models.TextField(blank=False, null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})
