from django.contrib import admin

from catalog.models import Product, Category, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'date_begin', 'activate')
    list_filter = ('date_begin', 'title', 'activate')
    search_fields = ('title', 'text')
