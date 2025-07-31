from django.db import models

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.IntegerField(primary_key=True)  # Keep this if IDs are coming from CSV
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=255, unique=True)
    distribution_center_id = models.IntegerField()
    
    # Only keep this one:
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
