from django.contrib import admin

from apps.business.models import Business, Category, BusinessDetail

# Register your models here.

admin.site.register(Business)
admin.site.register(Category)
admin.site.register(BusinessDetail)
