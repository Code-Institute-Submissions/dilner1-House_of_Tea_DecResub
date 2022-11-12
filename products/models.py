from django.db import models

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.FloatField()
    info = models.TextField()
    category = models.ForeignKey('Categories', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField()
    image_url = models.URLField(null=True, blank=True)
    weight = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
