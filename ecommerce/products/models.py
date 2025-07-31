from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)  # or AutoField if IDs are not pre-defined
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    distribution_center_id = models.IntegerField()

    def __str__(self):
        return self.name
