from django.contrib import admin
from .models import Categories, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
        list_display = (
            'sku',
            'name',
        )

admin.site.register(Categories)
admin.site.register(Product)