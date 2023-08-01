from django.contrib import admin

from app_catalog.models import Category, Product, Version
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)  # В админке будет разбиение по столбикам. Имя столбиков берётся из verbose_name поля

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'number', 'is_active')
    list_filter = ('product', 'is_active')
    search_fields = ('name',)

