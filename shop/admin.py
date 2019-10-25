from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ['name', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']


class WomenAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ['name', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']


class MenAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ['name', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',   'posted_date')
    list_filter = ("title",)
    search_fields = ['title', 'description']


admin.site.register(Men, MenAdmin)
admin.site.register(Women, WomenAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
