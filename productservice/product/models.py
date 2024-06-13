from django.db import models


class Product(models.Model):
    name        = models.CharField(max_length=128)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    stock       = models.IntegerField()

    def __str__(self):
        return self.name

