from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article

    readonly_fields = (
            'author',
            'date_posted',)

    list_display = (
            'title', 'author',
            'date_posted', 'content',)


admin.site.register(Article, ArticleAdmin)
