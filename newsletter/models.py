from django.db import models


class Newsletter(models.Model):
    name = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name