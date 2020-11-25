from django.test import TestCase
from .models import Article


# unit tests for views.py the blog app
class TestViewsBlog(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_about(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def test_subscribe(self):
        response = self.client.get('/subscribe')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/subscribe.html')

    def test_article_list(self):
        response = self.client.get('article_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_list/.html')

    def test_add_article(self):
        response = self.client.get('article/new/')
        self.assertRedirects(response, 'blog/article/<int:pk>/')

    def test_read_article(self):
        article = Article.objects.create('article/<int:pk>/')
        response = self.client.get(f'article/{article.id}')
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, 'blog/article_detail.html')

    def test_update_article(self):
        article = Article.objects.create()
        response = self.client.get(f'article/{article.id}/update')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_detail.html')

    def test_delete_article(self):
        article = Article.objects.create()
        response = self.client.get(f'article/{article.id}/delete')
        self.assertRedirects(response, '/')
        existing_articles = Article.objects.filter(id=article.id)
        self.assertEqual(len(existing_articles), 0)
