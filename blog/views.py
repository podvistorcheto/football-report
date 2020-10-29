from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Home Page</h2>')


def about(request):
    return HttpResponse('<h1>About Page</h2>')