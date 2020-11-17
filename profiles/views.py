from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Profile
from checkout.models import Package, PackageLineItem
from blog.models import Article


@login_required
def profile(request):
    """ to display user's profile page """
    orders = Package.objects.all()
    subscriptions = PackageLineItem.objects.all()
    articles = Article.objects.all()

    template = "profiles/profile.html"
    context = {
        'profile': profile,
        'orders': orders,
        'articles': articles,
        'subscriptions': subscriptions,
        'from_profile': True,
    }
    return render(request, template, context)
