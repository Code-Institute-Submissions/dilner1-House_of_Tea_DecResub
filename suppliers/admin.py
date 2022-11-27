from django.contrib import admin
from .models import Supplier


class SuppliersAdmin(admin.ModelAdmin):
    model = Supplier


admin.site.register(Supplier, SuppliersAdmin)
