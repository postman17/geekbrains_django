from django.contrib import admin
from .models import Product, Category
from django.template.loader import render_to_string
from datetime import datetime


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'picture',
        'cost', 'modified', 'created',
        'is_new'
    ]
    list_filter = [
        'category', 'image',
        'modified', 'created'
    ]
    search_fields = [
        'title', 'snippet'
    ]
    fieldsets = (
        (
            None, {
                'fields': ('title', 'category')
            },
        ),
        (
            'Context', {
                'fields': ('image', 'snippet', 'cost')
            }
        ),
    )

    def picture(self, obj):
        return render_to_string(
            'product/components/picture.html',
            {'url': obj.image.url}
        )

    def is_new(self, obj):
        return datetime.now().date() == obj.created.date()


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'modified', 'created',
        'is_new',
    ]
    list_filter = [
        'modified', 'created',
    ]
    search_fields = [
        'title', 'snippet'
    ]

    def is_new(self, obj):
        return datetime.now().date() == obj.created.date()


admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)
