from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = (
        'title',
        'urgent',
    )


admin.site.register(Contact, ContactAdmin)
