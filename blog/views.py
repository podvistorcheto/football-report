from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def subscribe(request):
    return render(request, 'blog/subscribe.html', {'title': 'Subscribe'})


def blogpage(request):
    return render(request, 'blog/blogpage.html', {'title': 'Blog'})


def newsletter(request):
    return render(request, 'blog/newsletter.html', {'title': 'Blog'})