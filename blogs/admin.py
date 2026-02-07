from django.contrib import admin

from blogs.models import Category, Blog

admin.site.register(Category)
admin.site.register(Blog)