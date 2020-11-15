from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
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
    template_name = 'blog/blogpage_html'
    context_object_name = 'articles'
    ordering = ['-date_posted']


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']


def newsletter(request):
    return render(request, 'blog/newsletter.html', {'title': 'Blog'})