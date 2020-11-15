from django.shortcuts import render
from blog.models import Article


def home(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'homepage/index.html', context)