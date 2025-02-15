from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name
    description = models.TextField()          # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    category = models.CharField(max_length=100)  # Product category

    def __str__(self):
        return self.name  # This will return the product name when you print the object
