from django.contrib import admin
from checkout.models import Package, PackageLineItem


class PackageLineAdminInline(admin.TabularInline):
    model = PackageLineItem


class PackageAdmin(admin.ModelAdmin):
    inlines = (PackageLineAdminInline, )

    readonly_fields = (
        'order_number', 'user', 'email',
        'price', 'date', 'original_cart',
        'stripe_pid',)

    list_display = (
        'order_number', 'full_name',
        'phone_number', 'user', 'email',
        'price', 'date', 'original_cart',
        'stripe_pid',)

    ordering = ('-date',)


admin.site.register(Package, PackageAdmin)
