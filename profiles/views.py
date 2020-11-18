from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Profile
from checkout.models import Package, PackageLineItem
from blog.models import Article
from django.core.paginator import Paginator


@login_required
def profile(request):
    """ to display user's profile page """
    profile = Profile.objects.get(user=request.user)
    author = Profile.objects.get(user=request.user)
    orders = Package.objects.filter(user=profile)
    subscriptions = PackageLineItem.objects.filter()
    articles = Article.objects.filter(author=profile)

    template = "profiles/profile.html"
    context = {
        'author': author,
        'profile': profile,
        'orders': orders,
        'articles': articles,
        'subscriptions': subscriptions,
        'from_profile': True,
    }
    return render(request, template, context)


