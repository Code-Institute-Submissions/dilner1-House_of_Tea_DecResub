from django.contrib import admin
from .models import Categories, Product

class ProductAdmin(admin.ModelAdmin):
        list_display = (
            'sku',
            'name',
        )

        ordering = ('sku',)

admin.site.register(Categories)
admin.site.register(Product, ProductAdmin)