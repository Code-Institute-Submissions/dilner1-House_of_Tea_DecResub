from django.contrib import admin
from .models import Categories, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
        list_display = (
            'sku',
            'name',
        )

        ordering = ('sku',)

admin.site.register(Categories)
admin.site.register(Product, ProductAdmin)