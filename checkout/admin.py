from django.contrib import admin
from checkout.models import Package, PackageLineItem


class PackageLineAdminInline(admin.TabularInline):
    model = PackageLineItem


class PackageAdmin(admin.ModelAdmin):
    inlines = (PackageLineAdminInline, )


admin.site.register(Package, PackageAdmin)
