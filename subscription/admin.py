from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'id',
    )

    ordering = ('id',)


admin.site.register(Subscription, SubscriptionAdmin)
