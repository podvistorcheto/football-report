from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from profiles.models import Profile
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Article


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def subscribe(request):
    return render(request, 'blog/subscribe.html', {'title': 'Subscribe'})


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 3
    ordering = ['-date_posted']


class UserArticleListView(ListView):
    model = Article
    template_name = 'blog/user_articles.html'
    context_object_name = 'articles'
    paginate_by = 3


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'article_image', 'content']

    def form_valid(self, form):
        author = Profile.objects.get(user=self.request.user)

        form.instance.author = author
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'article_image', 'content']

    def form_valid(self, form):
        author = Profile.objects.get(user=self.request.user)

        form.instance.author = author
        return super().form_valid(form)

    def test_func(self):
        author = Profile.objects.get(user=self.request.user)

        article = self.get_object()
        print(article.author)
        print(self.request.user)
        if self.request.user == article.author.user:
            return True
        else:
            return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/'

    def test_func(self):
        author = Profile.objects.get(user=self.request.user)

        article = self.get_object()
        print(article.author)
        print(self.request.user)
        if self.request.user == article.author.user:
            return True
        else:
            return False
