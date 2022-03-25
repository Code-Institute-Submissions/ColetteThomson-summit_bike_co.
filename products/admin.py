from django.contrib import admin
from .models import Product, Classification


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'classification',
        'bike_model',
        'price_now',
        'rating',
        'sku',
        'image',
    )

    ordering = ('classification',)


class ClassificationAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Classification, ClassificationAdmin)
