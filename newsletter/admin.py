from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    model = Newsletter


admin.site.register(Newsletter, NewsletterAdmin)
