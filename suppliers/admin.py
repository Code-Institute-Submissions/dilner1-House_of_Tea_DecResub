from django.contrib import admin
from .models import Suppliers


class SuppliersAdmin(admin.ModelAdmin):
    model = Suppliers


admin.site.register(Suppliers, SuppliersAdmin)
