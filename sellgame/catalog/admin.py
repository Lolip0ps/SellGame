from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'is_published', 'time_create']
    list_filter = ['is_published', 'time_create']
    list_editable = ['price', 'stock', 'is_published']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
