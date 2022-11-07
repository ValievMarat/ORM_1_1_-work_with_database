from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

