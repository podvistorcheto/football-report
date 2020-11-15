from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Profile
from checkout.models import Package


@login_required
class ProfileListView(ListView):
    model = Profile
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']  
