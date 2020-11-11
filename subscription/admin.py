from django.contrib import admin
from .models import Subscription

# Register your models here.

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'id',
    )

    ordering = ('id',)
    
admin.site.register(Subscription, SubscriptionAdmin)

