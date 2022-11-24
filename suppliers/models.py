from django.db import models


class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=60, null=True)
    location = models.CharField(max_length=60, null=True)
    info = models.TextField()
    image = models.ImageField()
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.supplier_name