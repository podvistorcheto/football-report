from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from profiles.models import Profile
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
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content']

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)

        form.instance.author = profile
        return super().form_valid(form)



def newsletter(request):
    return render(request, 'blog/newsletter.html', {'title': 'Blog'})